---
title: "Cloud Code"
date: "2014-09-09"
---

BRAINCLOUD allowsÂ developers to write custom [Cloud Code](/api/cc) routinesÂ in JavaScript, that reside and run on the BRAINCLOUD servers, allowing execution of code more securely and efficiently than if it were run client-side.

Advantages of Cloud Code scripts include:

- Better performance when calling multiple API calls in a row
- Lower BRAINCLOUD costs (the first 3 API calls are free, and each one after is 1/2 a count)
- More secure
- Ability to change logic server-side without a client update
- Ability to call out to [external web services](/api/cc/httpclient)
- Ability to perform certain operations that are not enabled in the client API

Cloud Code scripts can be called from:

- client appsÂ - via the [Script Service](/api/capi/script)Â APIs
- developer-operated servers - via theÂ [Server-to-Server](/api/s2s) API
- third-party services - via BRAINCLOUD'sÂ [WebHooks](/api/cc/ccscripts/webhooks) interface
- triggered via other operations ([API Hooks](/api/cc/ccscripts/apihooks)) - scripts can be configured to be triggered automatically as pre- or post- conditions for other API operations
- scheduled - scripts [scheduled](/api/cc/ccscripts/scheduledscripts) to execute in the future

Cloud Code scripts are written using BRAINCLOUD's web-based script editor, located in the Portal under **Design | Cloud Code | Scripts**.

For more information, check out:

- [Writing Scripts](/api/cc/ccscripts) section ofÂ the API Reference
- [Cloud Code Tutorials](/learn/sdk-tutorials/cloud-code-tutorials/) section ofÂ SDK Tutorials
