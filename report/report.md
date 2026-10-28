# IAM Lifecycle & Access Control Lab — Technical Report

## 1. Objective

Build and validate a local Identity and Access Management (IAM) environment that demonstrates centralized authentication, role-based authorization, and account deactivation.

The lab uses Keycloak as the identity provider and a Flask application as the protected resource.

## 2. Environment and Tools

| Component | Purpose |
|---|---|
| Keycloak 26.8.1 | Identity provider and user management |
| Python 3.11 | Application runtime |
| Flask | Web application and authorization logic |
| Authlib | OpenID Connect integration |
| OpenID Connect (OIDC) | Authentication protocol |
| Windows 11 | Local testing environment |

## 3. Architecture

The application uses the following authentication and authorization flow:

1. A user opens the Flask application.
2. The application redirects the user to Keycloak to authenticate.
3. Keycloak authenticates the user and returns identity and role information.
4. Flask evaluates the user's assigned roles against the requested route.
5. The application grants access or returns an HTTP 403 response.
6. A disabled account is tested to verify that a new login attempt is rejected.

## 4. Identity and Role Configuration

The lab uses a Keycloak realm named `northstar` and an OIDC client named `northstar-flask`.

The application uses three fictional user accounts:

| User | Assigned Role | Intended Access |
|---|---|---|
| `alice.hr` | `hr` | HR |
| `ben.finance` | `finance` | Finance |
| `chris.it` | `it_admin` | HR, Finance, and IT |

A Keycloak role mapper was configured to include realm roles in the authentication claims consumed by the application.

The `it_admin` role has elevated access across all three application areas. This is a lab-specific configuration used to demonstrate privileged access.

## 5. Test Cases and Results

| Test ID | Scenario | Expected Result | Observed Result |
|---|---|---|---|
| IAM-01 | HR user accesses HR area | Access granted | Passed |
| IAM-02 | HR user accesses Finance area | Access denied | Passed — HTTP 403 |
| IAM-03 | HR user accesses IT area | Access denied | Passed — HTTP 403 |
| IAM-04 | Finance user permissions | Match assigned role | Tested |
| IAM-05 | IT administrator accesses HR, Finance, and IT | Access granted | Passed |
| IAM-06 | Disabled HR user attempts a new login | Authentication rejected | Passed |

The Finance user's permissions were tested. The report should be updated if additional test results or screenshots become available.

## 6. Account Deactivation and Offboarding

The HR test account, `alice.hr`, was disabled in Keycloak to simulate offboarding.

A subsequent login attempt was rejected. This demonstrates the behavior observed when a disabled account attempts to establish a new authenticated session.

However, this test does not establish whether existing application sessions or previously issued tokens are invalidated immediately after account deactivation.

## 7. Findings and Security Recommendations

- **Least privilege:** Assign only the access needed for each user's responsibilities.
- **Privileged access:** Restrict and periodically review accounts assigned elevated roles.
- **Offboarding:** Disable identities promptly when access is no longer required.
- **Session management:** Validate existing-session invalidation and token revocation behavior.
- **Access reviews:** Document account status, assigned roles, review decisions, and justifications.
- **Secret management:** Keep application secrets in environment variables and out of source control.

## 8. Limitations

This is a simulated local IAM environment using fictional accounts and a development configuration.

The testing does not represent a production security assessment. Existing-session invalidation, immediate token revocation, and production-grade session management have not been fully validated.

## 9. Conclusion

The lab demonstrated a working OIDC authentication flow, role-based authorization for protected application routes, denial of unauthorized requests, and rejection of a new login attempt for a disabled account.

The project provided practical experience with IAM configuration, access validation, account lifecycle concepts, and access review documentation.

## 10. Evidence
Screenshots supporting the documented scenarios will be organized in the evidence/ directory.
- [Evidence and Screenshots](../evidence/README.md)


