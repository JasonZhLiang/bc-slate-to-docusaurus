# SetExperiencePoints
Sets the user's experience to an absolute value. Note that this is simply a set and will not reward the user if their level changes as a result.

<PartialServop service_name="playerStatistics" operation_name="SET_XPPOINTS" />

## Method Parameters
Parameter | Description
--------- | -----------
xp_points | The amount to set the user's experience to.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
int xp_points = 1;

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstatisticsService.SetExperiencePoints(xp_points, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
int xp_points = 1;
<%= data.branding.codePrefix %>.getPlayerstatisticsService().setExperiencePoints(xp_points, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
int xp_points = 1;
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStatisticsService] setExperiencePoints:
                    xp_points:xp_points
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
int xp_points = 1;
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstatisticsService.setExperiencePoints(xp_points, this);

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
var xp_points = 1;
<%= data.branding.codePrefix %>.playerStatistics.setExperiencePoints(xp_points, result =>
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
var xp_points = 1;
ServerResponse result = await <%= data.branding.codePrefix %>.playerStatisticsService.setExperiencePoints(xp_points:xp_points);

if (result.statusCode == 200) {
    print("Success");    
} else {
    print("Failed ${result.error['status_message'] ?? result.error}");
}
```

```mdx-code-block
</TabItem>
<TabItem value="cfs" label="Cloud Code">
```

```cfscript
var xp_points = 1;
var playerStatisticsProxy = bridge.getPlayerstatisticsServiceProxy();

var postResult = playerStatisticsProxy.setExperiencePoints(xp_points);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerStatistics",
    "operation":"SET_XPPOINTS",
    "data":{
        "xp_points":1
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
