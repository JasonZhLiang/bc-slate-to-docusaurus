# ExtendUserStatus
Stack user's statuses

<PartialServop service_name="playerState" operation_name="EXTEND_USER_STATUS" />

## Method Parameters
Parameter | Description
--------- | -----------
statusName | Name of the status.
additionalSecs | Add time to existing expiry time.
details | Json String to add additional details.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string statusName = "theStatusName";
int additionalSecs = 1000;
string details = "{}";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstateService.ExtendUserStatus(statusName, additionalSecs, details, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *statusName = "theStatusName";
int additionalSecs = 1000;
const char *details = "{}";
<%= data.branding.codePrefix %>.getPlayerstateService().extendUserStatus(statusName, additionalSecs, details, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *statusName = @"theStatusName";
int additionalSecs = 1000;
NSString *details = @"{}";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStateService] extendUserStatus:
                   statusName:statusName
               additionalSecs:additionalSecs
                      details:details
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
String statusName = "theStatusName";
int additionalSecs = 1000;
String details = "{}";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstateService.extendUserStatus(statusName, additionalSecs, details, this);

public void serverCallback(ServiceName serviceName, ServiceOperation serviceOperation, JSONObject jsonData)
{
    System.out.print(String.format("Success | %s", jsonData.toString()));
}
public void serverError(ServiceName serviceName, ServiceOperation serviceOperation, int statusCode, int reasonCode, String jsonError)
{
    System.out.print(String.format("Failed | %d %d %s", statusCode,  reasonCode, jsonError.toString()));
}
```

```mdx-code-block
</TabItem>
<TabItem value="js" label="JavaScript">
```

```javascript
var statusName = "theStatusName";
var additionalSecs = 1000;
var details = {};
<%= data.branding.codePrefix %>.playerState.extendUserStatus(statusName, additionalSecs, details, result =>
{
  var status = result.status;
  console.log(status + " : " + JSON.stringify(result, null, 2));
});
```

```mdx-code-block
</TabItem>
<TabItem value="dart" label="Dart">
```

```dart
var statusName = "theStatusName";
var additionalSecs = 1000;
var details = {};
ServerResponse result = await <%= data.branding.codePrefix %>.playerStateService.extendUserStatus(statusName:statusName, additionalSecs:additionalSecs, details:details);

if (result.statusCode == 200) {
    print("Success");
} else {
    print("Failed ${result.error['status_message'] ?? result.error}");
}
```

```mdx-code-block
</TabItem>
<TabItem value="lua" label="Roblox">
```

```lua
local statusName = "theStatusName"
local additionalSecs = 1000
local details = {}
<%= data.branding.codePrefix %>.playerStateService:extendUserStatus(statusName, additionalSecs, details)

if result.status == 200 then
    print("Success")
else
    print("Failed " .. tostring(result.error.status_message or result.error))
end
```

```mdx-code-block
</TabItem>
<TabItem value="cfs" label="Cloud Code">
```

```cfscript
var statusName = "theStatusName";
var additionalSecs = 1000;
var details = {};
var playerStateProxy = bridge.getPlayerstateServiceProxy();

var postResult = playerStateProxy.extendUserStatus(statusName, additionalSecs, details);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerState",
    "operation":"EXTEND_USER_STATUS",
    "data":{
        "statusName":"theStatusName",
        "additionalSecs":1000,
        "details":{}
    }
}
```

```mdx-code-block
</TabItem>
</Tabs>
</BrowserWindow>
```
<details>
<summary>JSON Response</summary>

```json
{
  "status" : 200,
  "data" : {}
}
```

</details>
