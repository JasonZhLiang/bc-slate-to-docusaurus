# UpdateSummaryFriendData
Update summary friend data.

<PartialServop service_name="playerState" operation_name="UPDATE_SUMMARY" />

## Method Parameters
Parameter | Description
--------- | -----------
summaryFriendData | A JSON string defining the summary data. For example `{ "xp":123, "level":12, "highScore":45123 }`

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string summaryFriendData = "{\"xp\": 12, \"attributeName\": \"value\"}";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstateService.UpdateSummaryFriendData(summaryFriendData, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *summaryFriendData = "{\"xp\": 12, \"attributeName\": \"value\"}";
<%= data.branding.codePrefix %>.getPlayerstateService().updateSummaryFriendData(summaryFriendData, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *summaryFriendData = @"{\"xp\": 12, \"attributeName\": \"value\"}";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStateService] updateSummaryFriendData:
            summaryFriendData:summaryFriendData
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
String summaryFriendData = "{\"xp\": 12, \"attributeName\": \"value\"}";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstateService.updateSummaryFriendData(summaryFriendData, this);

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
var summaryFriendData = {
    "xp": 12,
    "attributeName": "value"
};
<%= data.branding.codePrefix %>.playerState.updateSummaryFriendData(summaryFriendData, result =>
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
var summaryFriendData = {
    "xp": 12,
    "attributeName": "value"
};
ServerResponse result = await <%= data.branding.codePrefix %>.playerStateService.updateSummaryFriendData(summaryFriendData:summaryFriendData);

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
local summaryFriendData = {
    xp= 12,
    attributeName= "value"
}
<%= data.branding.codePrefix %>.playerStateService:updateSummaryFriendData(summaryFriendData)

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
var summaryFriendData = {
    "xp": 12,
    "attributeName": "value"
};
var playerStateProxy = bridge.getPlayerstateServiceProxy();

var postResult = playerStateProxy.updateSummaryFriendData(summaryFriendData);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerState",
    "operation":"UPDATE_SUMMARY",
    "data":{
        "summaryFriendData":{
            "xp":12,
            "attributeName":"value"
        }
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
