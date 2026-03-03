# IncrementUserStats
Atomically increment user statistics.

<PartialServop service_name="playerStatistics" operation_name="UPDATE" />

## Method Parameters
Parameter | Description
--------- | -----------
statistics | The data to be passed to method.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string statistics = "{\"LIVES\": 1}";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstatisticsService.IncrementUserStats(statistics, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *statistics = "{\"LIVES\": 1}";
<%= data.branding.codePrefix %>.getPlayerstatisticsService().incrementUserStats(statistics, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *statistics = @"{\"LIVES\": 1}";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStatisticsService] incrementUserStats:
                   statistics:statistics
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
String statistics = "{\"LIVES\": 1}";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstatisticsService.incrementUserStats(statistics, this);

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
var statistics = {
    "LIVES": 1
};
<%= data.branding.codePrefix %>.playerStatistics.incrementUserStats(statistics, result =>
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
var statistics = {
    "LIVES": 1
};
ServerResponse result = await <%= data.branding.codePrefix %>.playerStatisticsService.incrementUserStats(statistics:statistics);

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
var statistics = {
    "LIVES": 1
};
var playerStatisticsProxy = bridge.getPlayerstatisticsServiceProxy();

var postResult = playerStatisticsProxy.incrementUserStats(statistics);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerStatistics",
    "operation":"UPDATE",
    "data":{
        "statistics":{
            "LIVES":1
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
