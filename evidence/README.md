# IAM Lab — Evidence

This directory contains screenshots documenting the configuration and validation of the Northstar Solutions IAM Lifecycle and Access Control Lab.

The evidence supports the technical report and access review by showing the Keycloak configuration, role assignments, authorization results, and account deactivation test.

## Evidence Index

| Evidence ID | Description |
|---|---|
| E01 | Keycloak Admin Console |
| E02 | `northstar` realm configuration |
| E03 | HR user account configuration |
| E04 | Realm roles: `hr`, `finance`, and `it_admin` |
| E05 | IT administrator role assignment |
| E06 | `northstar-flask` client configuration |
| E07 | HR user successfully accessing the HR area |
| E08 | HR user denied access to the Finance and IT area |
| E09 | Disabled HR account rejected during a new login attempt |

## Notes

- Screenshots document a simulated local IAM environment using fictional accounts.
- Access results reflect the specific test scenarios performed.
- The disabled-account test validates a new login attempt; it does not establish immediate invalidation of existing sessions or tokens.

For configuration details and test results, see the [Technical Report](../report/report.md) and [Access Review Report](../access-review.md).

