# UpdateTimeZoneOffset
Update user's time zone offset preference on their profile.

<PartialServop service_name="playerState" operation_name="UPDATE_TIMEZONE_OFFSET" />

## Method Parameters
Parameter | Description
--------- | -----------
timeZoneOffset | New offset value

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
var timeZoneOffset = -2;

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstateService.UpdateTimeZoneOffset(timeZoneOffset, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
var timeZoneOffset = -2;
<%= data.branding.codePrefix %>.getPlayerstateService().updateTimeZoneOffset(timeZoneOffset, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
var timeZoneOffset = -2;
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStateService] updateTimeZoneOffset:
               timeZoneOffset:timeZoneOffset
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
var timeZoneOffset = -2;
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstateService.updateTimeZoneOffset(timeZoneOffset, this);

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
var timeZoneOffset = -2;
<%= data.branding.codePrefix %>.playerState.updateTimeZoneOffset(timeZoneOffset, result =>
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
var timeZoneOffset = -2;
ServerResponse result = await <%= data.branding.codePrefix %>.playerStateService.updateTimeZoneOffset(timeZoneOffset:timeZoneOffset);

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
local timeZoneOffset = -2
<%= data.branding.codePrefix %>.playerStateService:updateTimeZoneOffset(timeZoneOffset)

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
var timeZoneOffset = -2;
var playerStateProxy = bridge.getPlayerstateServiceProxy();

var postResult = playerStateProxy.updateTimeZoneOffset(timeZoneOffset);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerState",
    "operation":"UPDATE_TIMEZONE_OFFSET",
    "data":{
        "timeZoneOffset":-2
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
