---
title: "Profiles and Identity"
date: "2014-09-08"
---

A cloud-service such as BRAINCLOUD is only as flexible as itâs identity system â and BRAINCLOUD is very flexible indeed. Â BRAINCLOUD separates the concepts of a UserâsÂ _Profile_Â from theirÂ _Identity_ **User Profile** _(also known asÂ **Player Profile**)_

- Contains all the information about the user and their state/progress in the app or game
- Includes statistics, entities, attributes, virtual currency balances, the state of milestones, quests, achievements, etc.
- Is local to an App/Game âÂ notÂ shared across games in BRAINCLOUD\*

_\* See details on ourÂ [Shared Accounts](/learn/key-concepts/authentication/shared-accounts/)Â service for ways to share a single user identity across multiple apps._ **User Identity**

- Is used to identify a user in the system, and look up their Profile
- Maybe unauthenticated (anonymous) or authenticated (GameCenter id, Facebook id, E-mail, etc.)
- A player will often have multiple identities associated with their User Profile â just as in real life, your data may be associated with your driver's license, health number, phone number, etc.

BRAINCLOUD currently supports the following identity types:

- Anonymous
- E-mail â e-mail address + password
- Facebook id â facebook identity
- Twitter id â twitter identity
- Google Play â Google identity
- GameCenter id â iOS GameCenter identity
- Steam id â steam identity
- Universal â userid + password <- convenient during development

In addition to the above, BRAINCLOUD now supports two advanced forms of authentication:

- [External Authentication](/learn/key-concepts/authentication/external-authentication/)Â â allows you to authenticate your users using an external (custom) directory service
- [Shared Accounts](/learn/key-concepts/authentication/shared-accounts/)Â â allows user accounts to be shared across BRAINCLOUD apps

For more information, refer to theÂ **[Authentication API](/learn/key-concepts/authentication/)**Â docs.
