---
title: "Compatibility Settings"
date: "2016-08-23"
---

brainCloud is constantly improving. We work very hard to ensure that your apps still work even as the platform evolves.

To achieve this, we sometimes introduce _compatibility settings_ that preserve legacy behaviours for older apps. These settings are configured on the **Design | Core App Info | Advanced Settings** page of the portal.

As new compatibility settings are added, they normally:

- Default to _**enabled**_ for _existing apps_ to ensure compatibility
- Default to _**disabled**_ for _new apps_, so that they aren't subject to legacy system limitations

It is best for overall behaviour and performance if the compatibility settings are \*not\* enabled. It is therefore recommended that app developers periodically review these settings, to ensure that _only required compatibility settings are enabled_.

* * *

### Use legacy Cloud Code result format

In [brainCloud 2.10](https://staging.getbraincloud.com/apidocs/release-2-10-0/) we adjusted the JSON returns from Cloud Code scripts to align them better with the returns from regular API calls. This setting allows older scripts to still run.

### Enable checking of Incoming Events with each API message

brainCloud includes an [Events](https://staging.getbraincloud.com/apidocs/apiref/#capi-event) system that can be used to send messages (events) to individual users. This is useful for sending chat messages, awards, gifts, challenges and the like. Earlier builds of brainCloud would automatically check for any incoming events for a user during the processing of each and every API call. This processing has a server toll, and as most apps aren't using events, unnecessarily slowed down processing for everyday apps. Apps can instead use the [GetEvents()](https://staging.getbraincloud.com/apidocs/apiref/#capi-event-getevents) method to poll for new events.

This behavior is now turned off by default since [brainCloud 2.14](https://staging.getbraincloud.com/apidocs/release-2-14-0/), and can only be enabled for Business Plan (or above) apps. _Note that enabling this feature incurs an additional 1/2 point bulk API count per brainCloud API method call._

### Return User Entities during Authenticate and ReadPlayerState methods

Prior to [Release 2.22](https://staging.getbraincloud.com/apidocs/release-2-22-0/), brainCloud used to return all of a user's User Entities in response to Authenticate() and ReadPlayerState() methods. This was pretty convenient for quickly launching and logging into apps - but didn't scale when some apps started storing thousands of entities per user!

brainCloud no longer does this by default.

### Return legacy-format Social Leaderboard results

brainCloud added support for manually managed friends in [Release 2.22](https://staging.getbraincloud.com/apidocs/release-2-22-0/) - the implementation of which forced some changes to the JSON-data returned from the social leaderboard APIs. This flag should only be enabled if your app pre-dates 2.22 and depends upon the details of the old format.

### Enable legacy Currency handling (balance not enforced for Consume)

In [brainCloud 2.25](https://staging.getbraincloud.com/apidocs/release-2-25-0/) we fixed a defect where the server was not correctly enforcing currency balances under all scenarios in currency consumption. This has since been addressed, but the compatibility flag exists in case some apps were depending upon the prior behaviour.

### Default to returning full Entity contents for create and update operations

Prior to [Release 2.25](/apidocs/release-2-25-0/), brainCloud always returned the full contents of an entity object after Create() and Update() operations. This seemed to make sense at the time, but as some customers expanded to writing objects of 100K or more, it became painfully obvious that this was a waste of bandwidth.

### Funnel Custom and User File retrieval through app servers (slower)

Enabling this setting disables the Content Distribution Network (CDN) optimizations that were introduced in [brainCloud 2.25](https://staging.getbraincloud.com/apidocs/release-2-25-0/). The main reason you might want to do this is because your client doesn't properly handle the HTTP-based Redirects that are part of CDN processing. \[Basically, your app asks us for a particular file, and we redirect the request to the appropriate CDN server. Older versions of Unity in particular do not support redirects - so this \*should\* be enabled for existing Unity-based apps.\]

_Work-around: Apps without redirect support should use the [`GetCDNUrl()`](/apidocs/apiref/#capi-s3-getcdnurl) method to retrieve the CDN version of a file's URL for faster downloads (instead of enabling this setting)._

_**For best results, the file retrieval compatibility flag should be left un-checked.**_

### Allow Currency Calls from Client

In brainCloud 3.2, as a security + anti-fraud measure, we removed \[by default\] the ability for client apps to directly manage virtual currency balances. The effected methods, `AwardCurrency()`, `ConsumeCurrency()` and `ResetCurrency()` are still callable from server-side Cloud Code, which is much more secure.

Enabling this compatibility flag overrides this new restriction, and allows these calls to continue to be called from the client libraries.

### Generate Legacy Event Ids

Prior to release 3.2, the brainCloud Event System used numeric event ids: `eventId`. These ids had some significant limitations, including being slow to generate. The system has now been refactored to use a new-and-improved id: `evId`.

Enabling this compatibility flag tells the system to continue to create (at some performance penalty) the old `eventId` for Events. This is required if your app is still using the older API methods. _It is recommended that all apps move to the newer APIs, and the new `evId`, at their earliest convenience._
