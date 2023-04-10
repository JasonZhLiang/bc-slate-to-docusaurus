---
title: "Getting Started With C#"
date: "2016-05-30"
---

This tutorial goes over the basics of using BRAINCLOUD in C#. Â This applies to .NET applications, Xamarin, and even Unity.

### Accessing BRAINCLOUD

All of BRAINCLOUD's features are accessible through the BrainCloudClient class. Typically you will only ever need one instance of the BrainCloudClient in your application. Â For this reason, the BrainCloudClient can function as a singleton, and can be accessed through theÂ **BrainCloudClient.Instance** property.

### Initializing

Before you can do anything with BRAINCLOUD the BrainCloudClient must be initialized. Â This is accomplished by providing your Appâs details to the Client via the Initialize function.
```js
BrainCloudClient.Instance.Initialize(
    "https://sharedprod.braincloudservers.com/dispatcherv2",
    "49e1d5ad-12345-4144-ac59-6e02c64f1b12",
    "123456",
    "1.0.0");
```
### Updating the Client

To ensure callbacks are executed on the main thread you must call the Update method of the BrainCloudClient. Â Typically you will want to set up some version of an Update loop in your app that will constantly update the client every so often (ex. every 100ms).
```js
void MyUpdateMethod()
{
    BrainCloudClient.Instance.Update();
}
```
### Authenticating

Once a method is in place to run the callbacks via the Update() method you can start making API calls. Â The first call you'll likely need to make is one of the authentication methods to get an active session.

All API methods in BRAINCLOUD that contact the BRAINCLOUD server take callbacks as parameters, one for success and one for failure. Â These will get called when a response is received from the server, or the request times out. Â Here is a simple example of the authentication process in a console application:
```js
private void Authenticate()
{
    // Get username
    Console.WriteLine("Enter your username: ");
    string username = Console.ReadLine();

    // Get password
    Console.WriteLine("Enter your password: ");
    string password = Console.ReadLine();

    //Authenticate
    BrainCloudClient.Instance.AuthenticationService.AuthenticateUniversal(
        username,
        password,
        true,
        ApiSuccess,
        ApiError);
}

private void ApiSuccess(string jsonResponse, object cb)
{
    Console.WriteLine("Authenticate Success!");
}

private void ApiError(int statusCode, int reasonCode, string statusMessage, object cb)
{
    Console.WriteLine("Authenticate Failed!");
}
```