---
title: "PostToLeaderboards script"
date: "2018-08-17"
---

### Purpose

This script allows you to efficiently post to multiple leaderboards.

### Script

Click [PostToLeaderboards.ccjs.zip](https://staging.getbraincloud.com/apidocs/wp-content/uploads/2022/10/PostToLeaderboards.ccjs_.zip) to download the file.

### Usage / Setup

To configure this script, simply import it into your app.

Then call it from your app via the [RunScript()](https://staging.getbraincloud.com/apidocs/apiref/index.html#capi-script-runscript) API call.

The script takes the following parameters:

- leaderboards - Ids of leaderboards to post to.
- score - new score being posted.
- extra - extra data attached on leaderboard entry.

// Example Parameters
{
   "leaderboards": \["regular", "alltime"\],
   "score": 1000,
   "extras": {}
}
