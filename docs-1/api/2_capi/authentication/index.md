# Authentication
## Overview



This section describes the key methods for implementing basic authentication in your app. These methods are all you'll need if you:

- Just want to use anonymous authentication for all users
- Want to use a single authentication type (which is required) for all users â i.e. like forced Facebook or GameCenter
- Want to get authentication going quickly during development, and will flesh out more of the authentication details later

Consult the advanced (Identity) section if/when you want to get even more flexible with authentication (giving users more flexibility to choose their preferred authentication method, merging of profiles, etc.)  When implementing <%= data.branding.productName %> authentication, there are some key things to keep in mind:

<%= data.branding.productName %> uses an anonymous installation ID (commonly referred to as the anonymous ID) to identify individual devices.  This ID must be generated for first use, and saved by the client application. <%= data.branding.productName %> provides a convenient method for generating the ID â or the developer can generate it themselves.
<%= data.branding.productName %> also requires the client to keep track of the most recent profile ID.  This, together with the anonymous ID, provides additional security and allows <%= data.branding.productName %> to better understand user intent during logins/reconnections.  If the user has never connected before the profile ID should be null.

:::tip
The <em>optional</em> [<code><%= data.branding.codeWrapper %></code>](/api/wrapper) class will automatically persist your anonymousId and profileId as required. <strong>We highly recommend that you use it!</strong>
:::

If you are using the API Explorer, the list of valid Platform IDs can be found [here](/api/appendix/platformids).

Handy tip: To log a user out of <%= data.branding.productName %>, use the [Logout](/api/capi/playerstate/logout) method in [<code>Player State</code>](/api/capi/playerstate). Note that you don't absolutely *need* to log users out â their sessions will timeout on the server automatically anyway.

By default, the timeout length for authenticated users is 20 minutes. This timeout length can be lowered on the <%= data.branding.productName %> Dashboard. [Core App Info | Advance Settings > Session Timeout]

:::caution
You must authenticate and ensure it succeeds before attempting to call any other APIs that require authentication! Calling other APIs before authenticate successfully returns can cause the authenticate operation to fail.
:::

### Version Enforcement ###

<%= data.branding.productName %>'s authentication mechanisms allow you to enforce minimum client version requirements â forcing users with obsolete versions of your client app to upgrade before continuing within your application. This is especially useful for scenarios where you've fixed critical client errors, made significant changes to the server-side data structures, or generally just want to ensure that your users all have the best possible experience.

The client app version (sometimes referred to as the `gameVersion`) is sent to the server during authentication. It is a string of format "X.X" or "X.X.X" â for example, "1.0.0".  The app version is set via the [<code>Client</code>](/api/capi/client/initialize) or [<code><%= data.branding.codeWrapper %></code>](/api/wrapper/initialize) `Initialize()` methods.

The minimum versions that your app supports can be configured on the [Core App Info | Platforms](https://portal.braincloudservers.com/admin/dashboard#/development/core-settings-supportedversions) page of the design portal.

If the client app is older than the minimum version specified, authenticate will return a result similar to:

```
{
    "status": 400,
    "reason_code": 40322,
    "upgradeAppId": "http://itunes.com/apps/myappname",
    "status_message": "Processing exception (message): App version 1.0.0 is obsolete."
}
```

Recommended behavior of the client is to pop up a dialog inviting the user to upgrade the client, and then redirect them to the appropriate software update page.  Note that an upgrade URL may be data-filled with the minimum version # in the server portal.

### Disabled Apps ###

<%= data.branding.productName %> allows you to easily control whether your app is *enabled* or *disabled* via the [Core App Info | Advanced Settings](https://portal.braincloudservers.com/admin/dashboard#/development/core-settings-advanced-settings) page of the portal.

If for some reason you *do* decide to disable your app, you are able to configure a custom JSON object to be returned to apps that attempt to login. This JSON is set via the **[Edit Disabled Reason]** button on that same portal page.
```
{
    "message": "Apologies - we will be right back!"
}
```

Once disabled, your provided JSON-data will be returned within an element called `disabledReason` within the error response. For example:
```
{
    "reason_code": 40330,
    "status": 403,
    "status_message": "Processing exception (bundle): App is disabled.",
    "disabledReason": {
        "message": "Apologies - we will be right back!"
    },
    "severity": "ERROR"
}
```

### System Disabled ###

If for some reason your app is *System Disabled* by <%= data.branding.productName %> operations, your app will receive a `disabledReason` with two elements: `sysDisabled: true` and `message`.

```
{
    "reason_code": 40330,
    "status": 403,
    "status_message": "Processing exception (bundle): App is disabled.",
    "disabledReason": {
        "sysDisabled": true,
        "message": "This app has been system disabled. Please contact support."
    },
    "severity": "ERROR"
}
```


### API Summary

### Initialization

* [Initialize](/api/capi/authenticationentication/initialize)
* [GenerateAnonymousId](/api/capi/authenticationentication/generateanonymousid)

### Authentication

* [AuthenticateAnonymous](/api/capi/authenticationentication/authenticateanonymous)
* [AuthenticateApple](/api/capi/authenticationentication/authenticateapple)
* [AuthenticateEmailPassword](/api/capi/authenticationentication/authenticateemailpassword)
* [AuthenticateExternal](/api/capi/authenticationentication/authenticateexternal)
* [AuthenticateFacebook](/api/capi/authenticationentication/authenticatefacebook)
* [AuthenticateFacebookLimited](/api/capi/authenticationentication/authenticatefacebooklimited)
* [AuthenticateGameCenter](/api/capi/authenticationentication/authenticategamecenter)
* [AuthenticateGoogle](/api/capi/authenticationentication/authenticategoogle)
* [AuthenticateGoogleOpenId](/api/capi/authenticationentication/authenticategoogleopenid)
* [AuthenticateHandoff](/api/capi/authenticationentication/authenticatehandoff)
* [AuthenticateNintendo](/api/capi/authenticationentication/authenticatenintendo)
* [AuthenticateParse](/api/capi/authenticationentication/authenticateparse)
* [AuthenticatePlaystation5](/api/capi/authenticationentication/authenticateplaystation5)
* [AuthenticatePlaystationNetwork](/api/capi/authenticationentication/authenticateplaystationnetwork)
* [AuthenticateOculus](/api/capi/authenticationentication/authenticateoculus)
* [AuthenticateSettopHandoff](/api/capi/authenticationentication/authenticatesettophandoff)
* [AuthenticateSteam](/api/capi/authenticationentication/authenticatesteam)
* [AuthenticateTwitter](/api/capi/authenticationentication/authenticatetwitter)
* [AuthenticateUltra](/api/capi/authenticationentication/authenticateultra)
* [AuthenticateUniversal](/api/capi/authenticationentication/authenticateuniversal)

### Utility
* [ResetEmailPasswordWithExpiry](/api/capi/authenticationentication/resetemailpasswordwithexpiry)
* [ResetEmailPasswordAdvancedWithExpiry](/api/capi/authenticationentication/resetemailpasswordadvancedwithexpiry)
* [ResetUniversalIdPasswordWithExpiry](/api/capi/authenticationentication/resetuniversalidpasswordwithexpiry)
* [ResetUniversalIdPasswordAdvancedWithExpiry](/api/capi/authenticationentication/resetuniversalidpasswordadvancedwithexpiry)
* [ClearSavedProfileId](/api/capi/authenticationentication/clearsavedprofileid)



<DocCardList />