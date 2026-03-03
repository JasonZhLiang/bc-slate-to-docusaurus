# RemoveAttributes
Remove player attributes.

<PartialServop service_name="playerState" operation_name="REMOVE_ATTRIBUTES" />

## Method Parameters
Parameter | Description
--------- | -----------
attributes | Array of attribute names.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string attributes = "[\"key1\", \"key2\"]";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstateService.RemoveAttributes(attributes, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *attributes = "[\"key1\", \"key2\"]";
<%= data.branding.codePrefix %>.getPlayerstateService().removeAttributes(attributes, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *attributes = @"[\"key1\", \"key2\"]";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStateService] removeAttributes:
                   attributes:attributes
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
String attributes = "[\"key1\", \"key2\"]";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstateService.removeAttributes(attributes, this);

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
var attributes = [
    "key1",
    "key2"
];
<%= data.branding.codePrefix %>.playerState.removeAttributes(attributes, result =>
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
var attributes = [
    "key1",
    "key2"
];
ServerResponse result = await <%= data.branding.codePrefix %>.playerStateService.removeAttributes(attributes:attributes);

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
local attributes = [
    "key1",
    "key2"
]
<%= data.branding.codePrefix %>.playerStateService:removeAttributes(attributes)

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
var attributes = [
    "key1",
    "key2"
];
var playerStateProxy = bridge.getPlayerstateServiceProxy();

var postResult = playerStateProxy.removeAttributes(attributes);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerState",
    "operation":"REMOVE_ATTRIBUTES",
    "data":{
        "attributes":[
            "key1",
            "key2"
        ]
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
