# CHANGELOG


## v0.1.0-alpha.3 (2025-05-05)

### Bug Fixes

- Enable persist-credentials in release workflow for better authentication
  ([`5947ff4`](https://github.com/kensolfar/apigee-client/commit/5947ff43f9dd0053588e65d3a0b6973a73dde9a0))

- Ensure full commit history is fetched in release workflow
  ([`98e0c33`](https://github.com/kensolfar/apigee-client/commit/98e0c337afd1cb14ff438a4a82696413beed4679))

- Refactor release workflow to streamline semantic versioning and remove GitHub release step
  ([`eaf8fe5`](https://github.com/kensolfar/apigee-client/commit/eaf8fe52572260d5ebc2a5bb53c49c58d799b947))


## v0.1.0-alpha.2 (2025-05-05)

### Bug Fixes

- Update pyproject.toml with new version after release
  ([`c523892`](https://github.com/kensolfar/apigee-client/commit/c5238925555b1752f6b1cb510805b66e837f2e3e))


## v0.1.0-alpha.1 (2025-05-05)

### Bug Fixes

- Add setuptools configuration for apigee_sdk package in pyproject.toml
  ([`72bed18`](https://github.com/kensolfar/apigee-client/commit/72bed18cb20cd9a48608af9697dced0311ec0cdb))

- Add type hints to client classes and implement test job in release workflow
  ([`bb7998e`](https://github.com/kensolfar/apigee-client/commit/bb7998e4596f62e62318cf12465349145b953c75))

- Add verbose flag to TestPyPI publish step and update dependency constraints
  ([`2b81797`](https://github.com/kensolfar/apigee-client/commit/2b81797550e3287cd3895a27e4fa10e0930348d7))

- Change license from GPL-3.0-or-later to MIT in pyproject.toml
  ([`33fc301`](https://github.com/kensolfar/apigee-client/commit/33fc301f725b5fc5ac33738167cd4fa933b28004))

- Ensure test job completion before publishing to TestPyPI and PyPI
  ([`bfe3b55`](https://github.com/kensolfar/apigee-client/commit/bfe3b55e0ec5267a216e2e93fe13a8210c8caa73))

- Remove redundant license classifier from pyproject.toml
  ([`53f627f`](https://github.com/kensolfar/apigee-client/commit/53f627f08a584f8181f6078a53c483b58bb6a579))

- Remove semantic-release configuration from pyproject.toml
  ([`f91e2ba`](https://github.com/kensolfar/apigee-client/commit/f91e2bab448b6ce6056ad04646db2a703149c2c3))

- Remove unnecessary metadata section from setup.cfg
  ([`7f9e5fc`](https://github.com/kensolfar/apigee-client/commit/7f9e5fce120a9b31c9e1ae8684d2928963fc4fd6))

- Update dependency installation for semantic-release in release workflow
  ([`a163bd3`](https://github.com/kensolfar/apigee-client/commit/a163bd3a8850ab563244a387b3e4c1c0c91b2a5e))

- Update environment name from test-pypi to pypi-test in release workflow
  ([`334238b`](https://github.com/kensolfar/apigee-client/commit/334238b42668b3bee0cb19d78026fe26f27832bf))

- Update environment names in release workflow for consistency
  ([`dc09759`](https://github.com/kensolfar/apigee-client/commit/dc09759caac8c2207525895c8891f8b2df0d2dcb))

- Update job dependencies in release workflow and restore semantic versioning actions
  ([`5bdff48`](https://github.com/kensolfar/apigee-client/commit/5bdff48a6c8213e292aa66d807fa4348783505e1))

- Update license classifier from GPLv3 to MIT in pyproject.toml
  ([`085acf1`](https://github.com/kensolfar/apigee-client/commit/085acf1581fe0db462157b5e2e53d68674498728))

- Update license field to GPL-3.0-or-later in pyproject.toml
  ([`2d58801`](https://github.com/kensolfar/apigee-client/commit/2d58801c2e6e96653d6401a8893503af5a2f7514))

- Update TestPyPI publish step to use the correct API token
  ([`57189a3`](https://github.com/kensolfar/apigee-client/commit/57189a3a1a044827ac9d059eb2032d7cccd0d240))

### Features

- Add metadata section to setup.cfg for package information
  ([`6010569`](https://github.com/kensolfar/apigee-client/commit/6010569bd542cfa77c0935fed1c7448850c0c7ea))

- Enhance API client documentation across multiple modules
  ([`04e6c06`](https://github.com/kensolfar/apigee-client/commit/04e6c060a1e98ff9081af367172e89d534968b8e))

- Added detailed docstrings to the CachesClient, DeveloperAppClient, DevelopersClient,
  KeystoresClient, KVMClient, ProductsClient, ProxyClient, SharedFlowsClient, UserRolesClient, and
  UsersClient classes. - Each method now includes descriptions of parameters, return values, and
  exceptions raised. - Improved overall readability and maintainability of the codebase by providing
  clear documentation for API interactions.

- Implement versioning and release workflow with Commitizen integration
  ([`c38bdae`](https://github.com/kensolfar/apigee-client/commit/c38bdae14d11871626839caf298b31d9325dda9e))

- Refactor release workflow and reintroduce pyproject.toml for project metadata
  ([`93bd7e9`](https://github.com/kensolfar/apigee-client/commit/93bd7e9ae890e4ad30e06fb6680e01bbaa3dddca))

- Update project metadata in pyproject.toml and remove setup.py
  ([`2f8c603`](https://github.com/kensolfar/apigee-client/commit/2f8c60319e0fd77ef48605c230a76fa454cee41e))

- Update release process to use semantic-release for automated versioning and publishing
  ([`99e0842`](https://github.com/kensolfar/apigee-client/commit/99e084227966f055af13fcb9a03ca93b06d1d001))

- Update release workflow and add semantic release configuration in pyproject.toml
  ([`e15adba`](https://github.com/kensolfar/apigee-client/commit/e15adbaf9f68d15b067e121d5155b02ad2107f86))

- Update release workflow to include package building and publishing to Test PyPI
  ([`9187e57`](https://github.com/kensolfar/apigee-client/commit/9187e57c6cf0362690f55cc0419b6554d0cf11e6))
