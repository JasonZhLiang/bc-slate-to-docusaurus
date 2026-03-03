# ReadUserStatsSubset
Reads a subset of user statistics as defined by the input JSON.

<PartialServop service_name="playerStatistics" operation_name="READ_SUBSET" />

## Method Parameters
Parameter | Description
--------- | -----------
statistics | A collection containing the statistics to read.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string statistics = "[\"LIVES\"]";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstatisticsService.ReadUserStatsSubset(statistics, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *statistics = "[\"LIVES\"]";
<%= data.branding.codePrefix %>.getPlayerstatisticsService().readUserStatsSubset(statistics, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *statistics = @"[\"LIVES\"]";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStatisticsService] readUserStatsSubset:
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
String statistics = "[\"LIVES\"]";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstatisticsService.readUserStatsSubset(statistics, this);

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
var statistics = [
    "LIVES"
];
<%= data.branding.codePrefix %>.playerStatistics.readUserStatsSubset(statistics, result =>
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
var statistics = [
    "LIVES"
];
ServerResponse result = await <%= data.branding.codePrefix %>.playerStatisticsService.readUserStatsSubset(statistics:statistics);

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
var statistics = [
    "LIVES"
];
var playerStatisticsProxy = bridge.getPlayerstatisticsServiceProxy();

var postResult = playerStatisticsProxy.readUserStatsSubset(statistics);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerStatistics",
    "operation":"READ_SUBSET",
    "data":{
        "statistics":[
            "LIVES"
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
