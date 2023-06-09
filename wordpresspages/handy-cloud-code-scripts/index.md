---
title: "Handy Cloud Code Scripts"
date: "2018-08-17"
---

### Scripts

The following scripts implement common operations that may be handy for your app.

- [BlockIfBanned](https://staging.getbraincloud.com/apidocs/example-blockifbanned-script/) - blocks banned users from logging into your app
- [DeleteListOfUsers](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/deletelistofusers-script/) - deletes a list of provided users
- [OnRegisterNewUser](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/onregisternewuser-script/) - ensures registration calls will fail if the user already exists. Offers a place to put first-time signup logic
- [PostToLeaderboards](https://staging.getbraincloud.com/apidocs/example-posttoleaderboards-script/) - efficiently post to multiple leaderboards
- [RankGame\_AutoJoinMatch](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/rankgame_autojoinmatch/) - pair two players looking for an async match
- [RankGame\_FinishMatch](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/rankgame_finishmatch/) - handle the conclusion of a match. Adjust player ratings based on winner/loser
- [RestrictClientCalls](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/restrictclientcalls-script/) - restricts the client's ability to call brainCloud APIs. Provides additional security.
- [ScriptScheduler](https://staging.getbraincloud.com/apidocs/scriptscheduler-script/) - helper script for regularly recurring cloud code jobs
- [SharedScripts](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/sharedscripts/) - example of sharing scripts between cloud code with Global Properties
- [UniqueGroups\_AcceptGroupMember](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/uniquegroups_acceptgroupmember-script/) - enforce new group members to exist in only one group at a time
- [WebHookSpy](https://staging.getbraincloud.com/apidocs/webhookspy-script/) - view the parameters being sent to a webhook
- [ValidateContactEmail](https://staging.getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/validatecontactemail-script/)\- example of validating user's contact Email

### Importing Scripts

To import a script into your app:

- Download the script to your computer
- Go to the [Design | Cloud Code | Scripts](https://portal.braincloudservers.com/admin/dashboard#/development/serverscripts-edit) page of the portal
- Choose _Import Scripts_ from the **\[Import / Export\]** button
    - Click **\[Select\],** choose the script to import from the file selector
    - Click **\[Import\]**
