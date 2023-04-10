---
title: "SharedScripts"
date: "2019-05-31"
---

## Purpose

Script shows how you can use brainCloud properties to share scripts between cloud code.

## Warning

This has been tested with up to 30k bytes of code.

That said, isn't an officially sanctioned approach. We don't recommend putting more thanÂ **20-25kb**Â in the shared code string.

## Script

ClickÂ [TestSharedFunctions.ccjs.zip](script/TestSharedFunctions.ccjs.zip)Â to download the file.

## Usage / Setup

Add a Global Property with the scripts you want to share.

Properties can be set on theÂ **Design | Custom Config |Â [Global Properties](https://portal.braincloudservers.com/admin/dashboard#/development/global-properties)**Â page.

The example test script assumes aÂ `getFuzz`Â andÂ `addTwoNums`Â functions exist.
```js
function getFuzz() {
    return 'Fuzz';
}

function addTwoNums( a, b ) {
    return a + b;
}
```
![](images/image-1.png)

To configure this script, simply import it into your app.

Authenticate, and run the script.

This is the response you should get.
```js
{
  "data": {
    "response": {
      "getFuzz": "Fuzz",
      "sum": 15
    },
    "success": true
  },
  "status": 200
}
```