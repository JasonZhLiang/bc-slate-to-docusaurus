---
title: "RankGame_AutoJoinMatch"
date: "2018-09-05"
---

### Purpose

Starts a ranked match with a player looking for a match. Otherwise, will indicate that the current player is looking for a ranked match.

Based on the brainCloud [TicTacToe](https://github.com/getbraincloud/examples-unity) example.

### Script

Click [RankGame\_AutoJoinMatch.ccjs.zip](script/RankGame_AutoJoinMatch.ccjs.zip) to download the file.

### Usage / Setup

To configure this script, simply import it into your app.

The script is expected to be called when a player is trying to auto join an async match.

You call the script in the app via the [RunScript()](/api/capi/script/runscript) API call.

The script takes the following parameters:

- rankRangeDelta - Elo range delta we will accept. A player will 1200 Elo and a delta of 200, will accept matches of players between 1000-1400
- pushNotificationMessage - Notification opposing player will see. Note: you must first set your app up with push notifications

_Example script parameters_
```js
{ 
   "rankRangeDelta":200,
   "pushNotificationMessage":"You are now in a ranked match!"
}
```