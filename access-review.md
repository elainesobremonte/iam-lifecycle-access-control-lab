# IAM Access Review Report

**Project:** Northstar Solutions — IAM Lifecycle & Access Control Lab  
**Review Type:** Simulated User Access Review  
**Environment:** Local Keycloak and Flask Application

## 1. Review Objective

Evaluate user account status and assigned roles to verify that access permissions align with each user's intended responsibilities. The review also documents account deactivation testing and identifies areas requiring further validation.

## 2. Access Review Results

| User | Assigned Role | Account Status | Review Decision | Justification |
|---|---|---|---|---|
| `alice.hr` | `hr` | Disabled | Maintain disabled status | Account deactivated for the offboarding simulation; new login attempts were rejected. |
| `ben.finance` | `finance` | Enabled | Retain Finance access | Assigned role matches the user's intended function in the lab. |
| `chris.it` | `it_admin` | Enabled | Retain for lab testing | Elevated role provides access to HR, Finance, and IT areas. Privileged access should be justified and reviewed. |

## 3. Validation Evidence

The following scenarios were tested in the local environment:

- **HR authorization:** `alice.hr` successfully accessed the HR area before account deactivation.
- **Unauthorized access:** Requests from `alice.hr` to Finance and IT returned HTTP 403 before the account was disabled.
- **Finance authorization:** Access permissions for `ben.finance` were tested.
- **Privileged access:** `chris.it` was tested against all three application areas.
- **Offboarding:** After `alice.hr` was disabled in Keycloak, a new login attempt was rejected.

These results reflect the specific test scenarios performed and do not constitute a comprehensive security assessment.

## 4. Findings & Recommendations

1. **Account deactivation:** Disabled accounts should be prevented from initiating new authenticated sessions.
2. **Least privilege:** Users should receive only the permissions necessary for their assigned responsibilities.
3. **Privileged access management:** The `it_admin` role should be limited to authorized users and periodically reviewed.
4. **Offboarding controls:** The process should include identity deactivation and validation of existing application sessions and token behavior.
5. **Access review documentation:** Reviews should record assigned roles, account status, decisions, justifications, and follow-up actions.

## 5. Scope & Limitations

This review was conducted as part of a simulated IAM portfolio project using fictional accounts in a local Keycloak and Flask environment.

The review does not represent a production enterprise access review. Existing-session invalidation, immediate token revocation, and production-grade session controls have not been fully validated.

## 6. Review Conclusion

The tested role-based access rules behaved as expected for the documented scenarios. Unauthorized requests from the HR user were denied, and the disabled account was rejected during a new login attempt.

Further validation is required to establish how existing sessions and tokens behave after account deactivation. The results demonstrate foundational IAM testing and access review documentation practices within a controlled lab environment.

