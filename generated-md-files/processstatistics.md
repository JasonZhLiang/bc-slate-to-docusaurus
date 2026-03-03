# ProcessStatistics
Apply statistics grammar to a partial set of statistics.

<PartialServop service_name="playerStatistics" operation_name="PROCESS_STATISTICS" />

## Method Parameters
Parameter | Description
--------- | -----------
statistics | The stats data to be passed to the method.

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string statistics = "{\"DEAD_CATS\": \"RESET\", \"LIVES_LEFT\": \"SET#9\", \"MICE_KILLED\": \"INC#2\", \"MICE_MULTIPLIER\": \"INC_TO_LIMIT#2#20\", \"DOG_SCARE_BONUS_POINTS\": \"MAX#20\", \"TREES_CLIMBED_REQ\": \"MIN#5\"}";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.PlayerstatisticsService.ProcessStatistics(statistics, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *statistics = "{\"DEAD_CATS\": \"RESET\", \"LIVES_LEFT\": \"SET#9\", \"MICE_KILLED\": \"INC#2\", \"MICE_MULTIPLIER\": \"INC_TO_LIMIT#2#20\", \"DOG_SCARE_BONUS_POINTS\": \"MAX#20\", \"TREES_CLIMBED_REQ\": \"MIN#5\"}";
<%= data.branding.codePrefix %>.getPlayerstatisticsService().processStatistics(statistics, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *statistics = @"{\"DEAD_CATS\": \"RESET\", \"LIVES_LEFT\": \"SET#9\", \"MICE_KILLED\": \"INC#2\", \"MICE_MULTIPLIER\": \"INC_TO_LIMIT#2#20\", \"DOG_SCARE_BONUS_POINTS\": \"MAX#20\", \"TREES_CLIMBED_REQ\": \"MIN#5\"}";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> playerStatisticsService] processStatistics:
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
String statistics = "{\"DEAD_CATS\": \"RESET\", \"LIVES_LEFT\": \"SET#9\", \"MICE_KILLED\": \"INC#2\", \"MICE_MULTIPLIER\": \"INC_TO_LIMIT#2#20\", \"DOG_SCARE_BONUS_POINTS\": \"MAX#20\", \"TREES_CLIMBED_REQ\": \"MIN#5\"}";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getPlayerstatisticsService.processStatistics(statistics, this);

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
    "DEAD_CATS": "RESET",
    "LIVES_LEFT": "SET#9",
    "MICE_KILLED": "INC#2",
    "MICE_MULTIPLIER": "INC_TO_LIMIT#2#20",
    "DOG_SCARE_BONUS_POINTS": "MAX#20",
    "TREES_CLIMBED_REQ": "MIN#5"
};
<%= data.branding.codePrefix %>.playerStatistics.processStatistics(statistics, result =>
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
    "DEAD_CATS": "RESET",
    "LIVES_LEFT": "SET#9",
    "MICE_KILLED": "INC#2",
    "MICE_MULTIPLIER": "INC_TO_LIMIT#2#20",
    "DOG_SCARE_BONUS_POINTS": "MAX#20",
    "TREES_CLIMBED_REQ": "MIN#5"
};
ServerResponse result = await <%= data.branding.codePrefix %>.playerStatisticsService.processStatistics(statistics:statistics);

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
    "DEAD_CATS": "RESET",
    "LIVES_LEFT": "SET#9",
    "MICE_KILLED": "INC#2",
    "MICE_MULTIPLIER": "INC_TO_LIMIT#2#20",
    "DOG_SCARE_BONUS_POINTS": "MAX#20",
    "TREES_CLIMBED_REQ": "MIN#5"
};
var playerStatisticsProxy = bridge.getPlayerstatisticsServiceProxy();

var postResult = playerStatisticsProxy.processStatistics(statistics);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"playerStatistics",
    "operation":"PROCESS_STATISTICS",
    "data":{
        "statistics":{
            "DEAD_CATS":"RESET",
            "LIVES_LEFT":"SET#9",
            "MICE_KILLED":"INC#2",
            "MICE_MULTIPLIER":"INC_TO_LIMIT#2#20",
            "DOG_SCARE_BONUS_POINTS":"MAX#20",
            "TREES_CLIMBED_REQ":"MIN#5"
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
