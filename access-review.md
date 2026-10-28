\# IAM Access Review Report



\## Project

Northstar Solutions — Identity and Access Management Lab



\## Review Purpose

Review user account status and assigned roles to identify inappropriate or unnecessary access.



\## Access Review Results



| User | Assigned Role | Account Status | Access Decision | Reason |

|---|---|---|---|---|

| alice.hr | hr | Disabled | Retain record; deny new login | Account deactivated for offboarding simulation |

| ben.finance | finance | Enabled | Retain Finance access | Role matches the user's assigned function |

| chris.it | it\_admin | Enabled | Retain privileged access for lab testing | IT administrator role grants access to HR, Finance, and IT areas |



\## Validation Evidence

\- Alice's disabled account was rejected during a new login attempt.

\- Ben's Finance access was tested.

\- Chris's access to all three application areas was tested.

\- Alice's HR access was allowed before account deactivation.

\- Unauthorized access attempts by Alice returned HTTP 403 before her account was disabled.



\## Findings and Recommendations

1\. Disabled accounts should not be able to authenticate.

2\. Access should follow the principle of least privilege.

3\. Privileged roles such as `it\_admin` should be restricted, reviewed periodically, and justified by business need.

4\. Offboarding procedures should include disabling the identity and reviewing existing application sessions and tokens.

5\. Access reviews should be documented and repeated periodically.



\## Scope and Limitations

This is a simulated local IAM lab using fictional users and a local Keycloak and Flask application. The results are not evidence of a production enterprise access review.



\## Review Outcome

The tested role-based access rules behaved as expected for the documented scenarios. Alice's disabled account was rejected during a new login attempt. Existing sessions and immediate token revocation require separate validation.



