---
title: "DeleteListOfUsers script"
date: "2019-09-12"
---

### Purpose

ThisÂ scriptÂ deletesÂ aÂ listÂ ofÂ usersÂ basedÂ onÂ aÂ providedÂ listÂ ofÂ profileIdsÂ andÂ universalIds.

### Script

Click [DeleteListOfUsers.ccjs.zip](script/DeleteListOfUsers.ccjs.zip) to download the file.

### Usage / Setup

ToÂ configureÂ thisÂ script,Â simplyÂ importÂ itÂ intoÂ yourÂ app.  
CompileÂ aÂ listÂ ofÂ usersÂ youÂ wishÂ toÂ deleteÂ andÂ passÂ itÂ intoÂ theÂ script.  

_ExampleÂ scriptÂ parameters_
```js
{
	"profileIds": ["the-profile-id", "a8d86270-c95b-4ea7-a545-46bf27e7f94e"],
	"universalIds": ["the-universal-id", "tester_12", "admin_42"]
}
```