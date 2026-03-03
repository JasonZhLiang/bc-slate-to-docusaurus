# UpdateIsTester
Update flag indicating player is a tester or not.

<PartialServop service_name="playerState" operation_name="UPDATE_IS_TESTER" />

## Method Parameters
Parameter | Description
--------- | -----------
isTester | Boolean flag to indicate if the profile belongs to a test account.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
bool isTester = True;

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstateService.UpdateIsTester(isTester, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
bool isTester = True;
<%= data.branding.codePrefix %>.getPlayerstateService().updateIsTester(isTester, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
BOOL isTester = True;
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStateService] updateIsTester:
                     isTester:isTester
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
bool isTester = True;
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstateService.updateIsTester(isTester, this);

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
var isTester = True;
<%= data.branding.codePrefix %>.playerState.updateIsTester(isTester, result =>
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
var isTester = True;
ServerResponse result = await <%= data.branding.codePrefix %>.playerStateService.updateIsTester(isTester:isTester);

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
local isTester = true
<%= data.branding.codePrefix %>.playerStateService:updateIsTester(isTester)

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
var isTester = True;
var playerStateProxy = bridge.getPlayerstateServiceProxy();

var postResult = playerStateProxy.updateIsTester(isTester);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerState",
    "operation":"UPDATE_IS_TESTER",
    "data":{
        "isTester":true
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
