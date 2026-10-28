\# Northstar Solutions — IAM Lifecycle and Access Control Lab



\## Project Overview



This project is a simulated Identity and Access Management (IAM) environment built with Keycloak and Flask. It demonstrates identity authentication, role-based access control (RBAC), account deactivation, and access review documentation.



The lab uses fictional users and a local development environment to model common IAM tasks relevant to entry-level IAM and security roles.



\## Objectives



\- Configure centralized authentication using Keycloak and OpenID Connect (OIDC).

\- Assign application permissions through role-based access control.

\- Test authorized and unauthorized access to application areas.

\- Simulate an employee offboarding scenario by disabling an account.

\- Document access review results, findings, and limitations.



\## Tools and Technologies



\- \*\*Keycloak:\*\* Identity and access management and OIDC authentication

\- \*\*Python and Flask:\*\* Web application and authorization logic

\- \*\*Authlib:\*\* OIDC integration

\- \*\*Git and GitHub:\*\* Version control and project documentation



\## Lab Architecture



1\. A user opens the Flask application.

2\. The application redirects the user to Keycloak to authenticate.

3\. Keycloak authenticates the user and returns identity and role information.

4\. Flask checks the user's assigned roles before granting access to protected routes.

5\. Unauthorized requests are denied.

6\. A disabled account is tested to confirm that a new login is rejected.



\## Roles and Access Rules



| Role | Intended Access |

|---|---|

| `hr` | HR area |

| `finance` | Finance area |

| `it\_admin` | HR, Finance, and IT areas |



The `it\_admin` role has elevated access in this lab. In a real environment, privileged access should be restricted, justified by business need, and reviewed regularly.



\## Validation Summary



\- HR access was granted to the HR test user.

\- Unauthorized HR user requests to Finance and IT returned HTTP 403.

\- Finance user access was tested.

\- IT administrator access to all three application areas was tested.

\- A disabled HR account was rejected during a new login attempt.

\- Results were documented in `access-review.md`.



See the `evidence/` folder for screenshots of the configuration and test results once the evidence files have been added.



\## Access Review



The `access-review.md` file records the fictional users' assigned roles, account status, access decisions, and recommendations.



The review emphasizes least privilege, periodic access reviews, privileged account oversight, and offboarding controls.



\## Running the Lab



This project is designed for local testing, not production deployment.



1\. Install Python 3.11 or a compatible version, Keycloak, and the required Python packages.

2\. Start Keycloak in development mode on `127.0.0.1:8080`.

3\. Configure a Keycloak realm, application client, OIDC redirect URI, role mapper, and test users.

4\. Set the required environment variables in your local terminal:

&#x20;  - `FLASK\_SECRET\_KEY`

&#x20;  - `KEYCLOAK\_CLIENT\_SECRET`

5\. Install the Python dependencies required by the Flask application.

6\. Start the application from the project root:



&#x20;  ```cmd

&#x20;  python app\\app.py

&#x20;  ```



7\. Open `http://127.0.0.1:5000` in your browser and test the configured users and access rules.



\*\*Security note:\*\* Use only fictional test accounts and local development credentials. Never commit actual secrets, passwords, tokens, or production credentials to GitHub.



\## Scope and Limitations



This is a simulated local IAM lab. It is not a production deployment or evidence of professional enterprise IAM experience. Existing sessions, immediate token revocation, production-grade session management, and secure production configuration require additional validation.



\## Skills Demonstrated



\- IAM fundamentals and identity lifecycle concepts

\- OIDC authentication configuration

\- Role-based access control and least privilege

\- Access testing and authorization failure validation

\- Account deactivation and offboarding simulation

\- Access review documentation

\- Security-conscious project documentation



