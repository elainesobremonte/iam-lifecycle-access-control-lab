
import os
from functools import wraps

from flask import Flask, redirect, render_template_string, session, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)

# Local development only. Set a private value before running the app.
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("Set the FLASK_SECRET_KEY environment variable first.")

KEYCLOAK_URL = "http://127.0.0.1:8080"
REALM = "northstar"
CLIENT_ID = "northstar-flask"
CLIENT_SECRET = os.environ.get("KEYCLOAK_CLIENT_SECRET")

if not CLIENT_SECRET:
    raise RuntimeError("Set the KEYCLOAK_CLIENT_SECRET environment variable first.")

oauth = OAuth(app)

oauth.register(
    name="keycloak",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    server_metadata_url=(
        f"{KEYCLOAK_URL}/realms/{REALM}/.well-known/openid-configuration"
    ),
    client_kwargs={"scope": "openid profile email"},
)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


def role_required(required_role):
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapped(*args, **kwargs):
            roles = session.get("roles", [])
            if required_role not in roles and "it_admin" not in roles:
                return (
                    render_template_string(
                        "<h1>403 — Access denied</h1>"
                        "<p>Your account does not have the required role.</p>"
                        '<p><a href="/">Return home</a></p>'
                    ),
                    403,
                )
            return view(*args, **kwargs)
        return wrapped
    return decorator


@app.route("/")
def home():
    user = session.get("user")
    if not user:
        return render_template_string(
            "<h1>Northstar Solutions</h1>"
            "<p>IAM access-control lab</p>"
            '<p><a href="/login">Sign in with Keycloak</a></p>'
        )

    roles = session.get("roles", [])
    return render_template_string(
        """
        <h1>Northstar Solutions</h1>
        <p>Signed in as: {{ username }}</p>
        <p>Assigned roles: {{ roles }}</p>
        <ul>
          <li><a href="/hr">HR area</a></li>
          <li><a href="/finance">Finance area</a></li>
          <li><a href="/it">IT administration area</a></li>
        </ul>
        <p><a href="/logout">Sign out</a></p>
        """,
        username=user.get("preferred_username", "unknown"),
        roles=", ".join(roles) if roles else "No application roles found",
    )


@app.route("/login")
def login():
    redirect_uri = url_for("callback", _external=True)
    return oauth.keycloak.authorize_redirect(redirect_uri)


@app.route("/callback")
def callback():
    token = oauth.keycloak.authorize_access_token()
    userinfo = token.get("userinfo")
    if not userinfo:
        userinfo = oauth.keycloak.userinfo()

    # Read realm roles from the signed ID token's claims.
    # Keycloak must include realm_access.roles in the ID token.
    claims = token.get("userinfo") or userinfo or {}
    roles = claims.get("realm_access", {}).get("roles", [])

    session.clear()
    session["user"] = dict(userinfo)
    session["roles"] = roles
    return redirect(url_for("home"))


@app.route("/hr")
@role_required("hr")
def hr():
    return "<h1>HR area</h1><p>Access granted to HR or IT administrators.</p>"


@app.route("/finance")
@role_required("finance")
def finance():
    return "<h1>Finance area</h1><p>Access granted to Finance or IT administrators.</p>"


@app.route("/it")
@role_required("it_admin")
def it():
    return "<h1>IT administration area</h1><p>Access granted to IT administrators.</p>"


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/logout"
        f"?post_logout_redirect_uri=http%3A%2F%2F127.0.0.1%3A5000"
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
