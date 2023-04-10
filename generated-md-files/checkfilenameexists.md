# CheckFilenameExists
## Overview
Check if filename exists for provided path and name.

<PartialServop service_name="groupFile" operation_name="CHECK_FILENAME_EXISTS" />

## Usage

```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```

```csharp
string groupId = "dfsfsffsd";
string folderPath = "";
string filename = "cccc";

SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};

<%= data.branding.codePrefix %>.GroupfileService.CheckFilenameExists(groupId, folderPath, filename, successCallback, failureCallback);
```

```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```

```cpp
const char *groupId = "dfsfsffsd";
const char *folderPath = "";
const char *filename = "cccc";
<%= data.branding.codePrefix %>.getGroupfileService().checkFilenameExists(groupId, folderPath, filename, this);
```

```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```

```objectivec
NSString *groupId = @"dfsfsffsd";
NSString *folderPath = @"";
NSString *filename = @"cccc";
BCCompletionBlock successBlock; // define callback
BCErrorCompletionBlock failureBlock; // define callback
[[<%= data.branding.codePrefix %> groupFileService] CheckFilenameExists:
                      groupId:groupId
                   folderPath:folderPath
                     filename:filename
              completionBlock:successBlock
         errorCompletionBlock:failureBlock
                     cbObject:nil]
```

```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```

```java
String groupId = "dfsfsffsd";
String folderPath = "";
String filename = "cccc";
this; // implements IServerCallback
<%= data.branding.codePrefix %>.getGroupfileService.CheckFilenameExists(groupId, folderPath, filename, this);

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
var groupId = "dfsfsffsd";
var folderPath = "";
var filename = "cccc";
<%= data.branding.codePrefix %>.groupFile.CheckFilenameExists(groupId, folderPath, filename, result =>
{
  var status = result.status;
  console.log(status + " : " + JSON.stringify(result, null, 2));
});
```

```mdx-code-block
</TabItem>
<TabItem value="cfs" label="Cloud Code">
```

```cfscript
var groupId = "dfsfsffsd";
var folderPath = "";
var filename = "cccc";
var groupFileProxy = bridge.getGroupfileServiceProxy();

var postResult = groupFileProxy.CheckFilenameExists(groupId, folderPath, filename);
```

```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```

```r
{
    "service":"groupFile",
    "operation":"CHECK_FILENAME_EXISTS",
    "data":{
        "groupId":"dfsfsffsd",
        "folderPath":"",
        "filename":"cccc"
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
  "data" : null
}
```

</details>

## Method Parameters
Parameter | Description
--------- | -----------
