# IAM Lifecycle & Access Control Lab

**Project Type:** Hands-on IAM Portfolio Project  
**Environment:** Local Development  
**Technologies:** Keycloak · Python · Flask · Authlib · OpenID Connect (OIDC)

## Overview

This project demonstrates core Identity and Access Management (IAM) concepts through a simulated organization called Northstar Solutions. Using Keycloak for identity authentication and Flask for application access control, the lab explores how user identities, assigned roles, and account status affect access to protected resources.

The project focuses on authentication, role-based access control (RBAC), access validation, account deactivation, and access review documentation.

## Project Files

- [Technical Lab Report](report/report.md) — configuration, test scenarios, results, and limitations.
- [Evidence & Screenshots](evidence/README.md) — screenshots documenting the Keycloak configuration and validation tests.
- [Access Review Report](access-review.md) — account status, assigned roles, review decisions, and recommendations.
- [Application Source Code](app/app.py) — Flask application and role-based access control logic.

## Objectives

- Configure centralized authentication using Keycloak and OIDC.
- Implement role-based authorization in a Flask application.
- Validate permitted and denied access to protected application routes.
- Simulate user offboarding by disabling an account.
- Document access decisions, test results, and security recommendations.

## Technology Stack

| Technology | Purpose |
|---|---|
| Keycloak | Identity management and authentication |
| OpenID Connect | Authentication protocol |
| Python and Flask | Web application and access-control logic |
| Authlib | OIDC integration |
| GitHub | Source code and project documentation |

## Architecture & Workflow

1. The user opens the Flask web application.
2. The application redirects the user to Keycloak for authentication.
3. Keycloak authenticates the user and provides identity and role information.
4. Flask evaluates the user's assigned roles against the requested application area.
5. Access is granted or denied according to the configured authorization rules.
6. A disabled account is tested to verify that a new login attempt is rejected.

## Role-Based Access Control

The lab uses three fictional user roles:

| Role | Authorized Areas |
|---|---|
| `hr` | HR |
| `finance` | Finance |
| `it_admin` | HR, Finance, IT |

The `it_admin` role has elevated access across all three areas. This configuration illustrates why privileged accounts require appropriate authorization, least-privilege controls, and periodic access reviews.

## Testing & Validation

The following scenarios were tested:

- **Authorized access:** The HR user accessed the HR area.
- **Unauthorized access:** The HR user received HTTP 403 responses when accessing Finance and IT areas.
- **Finance access:** The Finance user's access permissions were tested.
- **Privileged access:** The IT administrator's access to all three application areas was tested.
- **Account deactivation:** A disabled HR account was rejected during a new login attempt.

The results reflect the specific scenarios tested in the local environment. See the [Technical Lab Report](report/report.md) for the documented test cases and the [Access Review Report](access-review.md) for review decisions and recommendations.

## Evidence & Screenshots

Screenshots documenting the Keycloak configuration, role assignments, authorization results, and account deactivation test are organized in the [`evidence/`](evidence/README.md) directory.

The evidence index describes the purpose of each screenshot and links the visual documentation to the corresponding lab activities.

## Access Review & Offboarding

The access review documents each fictional user's role, account status, access decision, and justification.

Key security considerations include:

- Applying least privilege when assigning access.
- Reviewing privileged accounts and their business justification.
- Disabling accounts during offboarding.
- Reviewing existing sessions and token revocation behavior.
- Maintaining documentation of access decisions and test results.

## Running the Application

This lab is intended for local development and testing.

**Prerequisites**

- Python 3.11 or a compatible version
- Keycloak
- Required Python packages for the Flask application

**Setup**

1. Start Keycloak in development mode, configured to listen on `127.0.0.1:8080`.
2. Configure the `northstar` realm, the `northstar-flask` client, OIDC redirect URIs, role mappings, and fictional test users.
3. Set the following environment variables in your terminal:
   - `FLASK_SECRET_KEY`
   - `KEYCLOAK_CLIENT_SECRET`
4. Install the application's required Python dependencies.
5. From the project root, start the Flask application:

   ```cmd
   python app\app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser and test the configured accounts and access permissions.

**Security Note:** Never publish actual credentials, passwords, tokens, or secret values. Use fictional accounts and local development credentials only.

## Scope & Limitations

This is a simulated IAM lab using a local Keycloak instance and Flask application. It is not a production deployment.

Existing-session behavior, immediate token revocation, production-grade session management, and hardened deployment settings require additional testing before the design could be considered for production use.

## Skills Demonstrated

- IAM fundamentals and identity lifecycle concepts
- OIDC authentication configuration
- Role-based access control and least privilege
- Access testing and authorization validation
- Account deactivation and offboarding simulation
- Access review and security documentation
- Secure handling of application secrets
