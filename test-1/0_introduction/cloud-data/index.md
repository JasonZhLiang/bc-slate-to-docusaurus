---
title: "Cloud Data"
date: "2014-09-08"
---

BRAINCLOUD provides very robust and specialized APIs for dealing with cloud data.

In regard to User (Player) data, BRAINCLOUD provides the following mechanisms:

- **User \[Player\] Statistics** - advanced API for managing numeric stats on the server. Â Statistics are defined ahead-of-time on the server and are concurrency-safe. Â User statistics are a key building block for BRAINCLOUD's Gamification features, and therefore developers are encouraged to take advantage of the facilityÂ where appropriate
- **User Entities** - entities are used to store more complex (i.e. json) objects on the server.Â The BRAINCLOUD API has been optimized to allow retrieval of all entities via a single read operation, with support for a continuous stream of incremental updates.
- **User Attributes** - BRAINCLOUD also provides support for free-form attributes (key+value pairs). Â Attributes are useful for simple, less rigid data - and can be used to simplify the creation of complex user segments (for promotions targeting)

_Note - BRAINCLOUD's Gamification feature provides direct support for player XP, player XP level, achievements, etc - so you do not need to model these concepts directly in your cloud data._

BRAINCLOUD also provides support for **Global** data elements:

- **Global Statistics** - similar to user statistics, but with global scope - global statistics are useful for managing key metrics across your player population
- **Global Entities** - like User Entities, except global in scope. Â Global Entities support ACL for permissions. Â Global Entities can also be written with a TTL (time to live) attribute so that they automatically delete themselves after a given time period.
- **Global Properties** - finally, BRAINCLOUD supports Global Properties (key+value pairs) which areÂ very handy as global tuning parameters for your app or game (especially since they're directly editable via the design portal).

_Note that BRAINCLOUD's Design Portal provides support for viewing (and in someÂ cases editing) all User and Global data._

[![BRAINCLOUD Portal](images/BRAINCLOUD_dashboard_userStatsMonitoring.jpg)](images/BRAINCLOUD_dashboard_userStatsMonitoring.jpg)

For a more detailedÂ overview of BRAINCLOUD's Cloud Data features, see the introductory section of the [Cloud Data APIs](/learn/key-concepts/data/).
