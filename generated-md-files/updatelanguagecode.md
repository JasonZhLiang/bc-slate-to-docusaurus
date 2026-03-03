# UpdateLanguageCode
Update user's language code preference on their profile.

<PartialServop service_name="playerState" operation_name="UPDATE_LANGUAGE_CODE" />

## Method Parameters
Parameter | Description
--------- | -----------
languageCode | New language code

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string languageCode = "fr";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstateService.UpdateLanguageCode(languageCode, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *languageCode = "fr";
<%= data.branding.codePrefix %>.getPlayerstateService().updateLanguageCode(languageCode, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *languageCode = @"fr";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStateService] updateLanguageCode:
                 languageCode:languageCode
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
String languageCode = "fr";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstateService.updateLanguageCode(languageCode, this);

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
var languageCode = "fr";
<%= data.branding.codePrefix %>.playerState.updateLanguageCode(languageCode, result =>
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
var languageCode = "fr";
ServerResponse result = await <%= data.branding.codePrefix %>.playerStateService.updateLanguageCode(languageCode:languageCode);

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
local languageCode = "fr"
<%= data.branding.codePrefix %>.playerStateService:updateLanguageCode(languageCode)

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
var languageCode = "fr";
var playerStateProxy = bridge.getPlayerstateServiceProxy();

var postResult = playerStateProxy.updateLanguageCode(languageCode);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerState",
    "operation":"UPDATE_LANGUAGE_CODE",
    "data":{
        "languageCode":"fr"
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
