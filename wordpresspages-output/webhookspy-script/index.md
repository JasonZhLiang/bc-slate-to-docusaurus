---
title: "WebHookSpy script"
date: "2018-08-29"
---

## Purpose

Used to discover and/or confirm the parameters being sent to a webhook.

The script simply:

- returns the parameters sent to it via the web response
- writes an info-level log record, viewable via the _Recent Errors_ section of _Monitoring_

## Script

Click [WebHookSpy.ccjs.zip](images/WebHookSpy.ccjs_.zip) to download the file.

## Usage / Setup

To configure this script, you must:

- First import it into your app
- Then go to **Design | Cloud Code | WebHooks**, and link this script into a new or existing webhook

You can test calling the script using a browser, [Postman](https://www.getpostman.com), or something similar - just to confirm that the logging is working.

You will then to go to the external system (the one that is calling the webhook), and do whatever is required to get it to invoke the webhook.

Finally, go to **Quick | Recent Errors** to view the results of invocation:

- _change the filter to show info messages_ - enable the \[x\] checkbox by the **green "i"** and hit **\[Refresh\]**
- click on a log line to view the details. The parameters will be displayed in the _Context_ field, which you can expand by dragging the bottom-right corner of the dialog
