---
title: "User Summary"
date: "2015-08-20"
---

This tab displays a summary of key information about the selected User. You can even flag users and add notes to make them easier to look up later. We will go through all the features of this page from top to bottom.

[![](images/2018-06-20_20-20-33.png)](images/2018-06-20_20-20-33.png)

Right at the top, you can see the User's profile picture (or a placeholder if they have none), their unique Profile ID, and their Profile Name (which is editable from here). Â 

Right next to this field is a checkbox marked **Is Tester**. This is a very useful tool for testing your App and debugging many issues. For example, it can be used in yourÂ app to enable/disable features specificÂ for testers. The isTesterÂ value can be found from theÂ [ReadUserState](/api/capi/playerstate/readuserstate) API Call.

After checking the Is Tester box on the user Profile, you will notice small pencil icons appear next to many pieces of information on the page.

[![](images/2018-06-20_20-33-58.png)](images/2018-06-20_20-33-58.png)

Clicking on those icons allows you to directly edit those fields. To save your changes click the greenÂ **Save User** button in the upper right of the page.

[![](images/2018-06-20_20-25-07.png)](images/2018-06-20_20-25-07.png)

Other than the **Save User** button (which as described above will save any edits you have made to the User) there are two other buttons at the top of the page. Â TheÂ **Reset User** button will delete all user dataÂ **except** User Currency,Â User Credentials, andÂ User Transactions (i.e. Product Purchases). Â TheÂ **Delete User** button will **permanently** delete the User (this action cannot be undone!).

TheÂ **Login As User** button under the profile picture, will take you to theÂ **API Explorer** page and automatically authenticate you as the current user. This makes debugging API calls as a specific user very easy to do.

The next section,Â **Account Information**, contains some key information about the User. Â If **Is Tester** is enabled many of these fields can be edited.

[![](images/2018-06-20_20-28-29.png)](images/2018-06-20_20-28-29.png)

Below that is theÂ **Account Details** section which displays a summary of the User's currencies and stats.

[![](images/2018-06-20_20-30-12.png)](images/2018-06-20_20-30-12.png)

TheÂ **Annotations** section allows you to flag the user for easier locating in the future. Â You can also add notes to refer to at a later time. Â After you're done adding notes be sure to click theÂ **Save Notes** button. Â If you want to discard your notes click theÂ **Delete Notes** button.

![](images/credentials-1024x176.jpg)

The next section isÂ the **Credentials**. From here you can see all the User's attached Identities including the Authentication Type and the corresponding ID. Â 

![](images/deviceToken-1024x245.jpg)

The final section isÂ the **Device Tokens** (only shows up when you registered a notification device to this user). At the bottom of this section are two more buttons. Â **Send Notification** allows you to send a custom push notification message to all the User's registered notification methods.Â  **Reset Device Tokens** allows you to delete all the registered device tokens.
