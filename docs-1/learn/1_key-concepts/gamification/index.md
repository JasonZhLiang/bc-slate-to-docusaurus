---
title: "Gamification"
date: "2014-09-09"
---

brainCloud's Gamification features provide server-side support common metagame elements, including:

- Experience Points (XP) and Levels
- Achievements
- Milestones
- Quests
- Stats Events

TheseÂ features build upon theÂ Statistics APIs and a concept of Player Rewards.

_**Player Rewards**_

brainCloud provides an ability to reward players for completing meta-goals: leveling up, completing a milestone and/or completing quests. Â Rewards can consist of:

- Achievements
- Experience Points
- Currencies
- User Statistics
- Global Statistics

* * *

## XPÂ Levels

brainCloud can manage experience points (XP) and levels, and reward the player for leveling up. A player's XP starts at 0 and is incremented using methods of theÂ [Player Statistics](/api/capi/playerstats)Â service.Â A list of player XP levels can be read from the client usingÂ [ReadXPLevelsMetaData()](/api/capi/gamification/readxplevelsmetadata). Â 

* * *

## Achievements

Achievements can be triggered manually, or as the result of player rewards. Achievements can be data filled with the ids for platform achievements (on iOS, Steam, etc.) so that they may automatically be triggered in sync with brainCloud achievements.

Achievements can be awarded directly using the [AwardAchievements()](/api/capi/gamification/awardachievements) API. Â There are also API calls for retrieving the full list of achievements, and the list of achievements that have already been awarded for the player.

* * *

## Milestones

Milestones are used to define conditions under which rewards are to be delivered. Â Milestones must first be unlocked before they can be completed and then awarded.

[![brainCloud Milestone](images/brainCloud-Milestone-1024x798.png)](images/brainCloud-Milestone-1024x798.png)

* * *

## Quests

Quests are essentially compound Milestones. The completion status of the QuestÂ is derived from the completion status of the Milestones (Tasks) that it is composed of.

[![brainCloud Quest](images/brainCloud-Quest-174x300.png)](images/brainCloud-Quest-174x300.png)

* * *

## Stats Events

Stats Events are essentially Stats Macros. Â The Macro is defined on the server and triggered by id from the client.

For the same flexibility, but controlled directly from the client, try using the [ProcessStatistics()](/api/capi/playerstats/processstatistics) API.

<DocCardList />