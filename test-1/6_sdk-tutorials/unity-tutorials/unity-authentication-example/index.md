---
title: "Unity Authentication Example"
date: "2015-02-13"
---

This example shows how to use several of the authentication types in BRAINCLOUD. Specifically, we illustrate how to authenticate using the following authentication types:Â 

- Email and Password
- Universal
- Anonymous
- AdvancedÂ 
- Google (Android Devices only)

## **Prerequisites**

In order to get started, you will need Unity installed. Please download the example project by following the link below:Â 

[Unity Authentication Example Download](https://github.com/getbraincloud/UnityExamples)

You can also download the stand-alone BRAINCLOUD Unity library here:

[BRAINCLOUD Unity Client](https://github.com/getbraincloud/Unity-Csharp)

## **Running the Project**

To try out the example project you must:

- Download the examples-unity repo.Â 
- Unzip the examples-unity folder.
- Open the âAuthenticationâ project in unity.
- Open the âMainâ scene in the âScenesâ folder.
- Follow the steps under âPointing to your own gameâ to point to your BRAINCLOUD app.
- Click Unityâs play button.

You should see the following screen.

![](images/AuthPage1-1024x576.jpg)

Feel free to test out the various authentication types. Authentication types can be changed by clicking the dropdown menu next to âSelect Auth Typeâ. You can also toggle âAdvanced Authâ which allows you to send extra JSON data along with your authentication. This extra JSON data can be used for things like account validation. In this example, we use the extra data to create a user entity of type âplayerâ for new users.Â 

![](images/AuthPage2-1024x575.jpg)

### **Pointing to your own game**

Follow these steps in order to test different authentication methods against your own BRAINCLOUD game:

1. Open the BRAINCLOUD settings menu option.

![](https://lh5.googleusercontent.com/yaelBFzJm7rpXcrbgRyF7Q0PJvuKgRK0BwdduU2TM9OeMRIuxfMceYI54jw5A6oZgatp6-zn1uLItdsN2-E9y_CsuPehlhJCMF8m4NNf5OFj-LlgYtK0WPEbJ3ItE1BwpR29eioGUMaf6eW8IQ)

2. Login to BRAINCLOUD and select your game.

- ![](images/SignIn2-1.png)
    
- ![](images/SignIn3-2.png)
    

Ensure that the correct platforms have been enabled in the BRAINCLOUD Portal, under **Design | Core App Info | Platforms**

4. Import the app data from the âImportDataâ folder.Â 

See [Import/Export Game Data](/learn/portal-tutorials/importexport-game-data/) in the portal tutorial section for more information.Â 

The Authentication app also features the following BRAINCLOUD functionality:

- [User Entities](/api/capi/entity)
- [Custom Entities](/api/capi/customentity)
- [Player XP and Player Leveling](/api/capi/playerstats)
- [Virtual Currencies](/api/capi/virtualcurrency)
- [Player Stats](/api/capi/playerstats)
- [Global Stats](/api/capi/globalstats)
- [Cloud Code scripting](/api/capi/script)Â 
- [Identity Attaching / Merging](/api/capi/identity)

Enjoy interacting with this example project and getting an idea for some of the features BRAINCLOUD has to offer.Â 

### **Code Overview**

First, we initialize the BRAINCLOUD Wrapper in a script called BCConfig.cs
```js
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class BCConfig : MonoBehaviour {
 
    private BrainCloudWrapper _bc;
 
    public BrainCloudWrapper GetBrainCloud()
    {
        return _bc;
    }
    
    // Use this for initialization
    void Awake ()
    {
        DontDestroyOnLoad(gameObject);
        _bc = gameObject.AddComponent<BrainCloudWrapper>();
        
        _bc.WrapperName = gameObject.name;    // Optional: Set a wrapper name
        _bc.Init();      // Init data is taken from the BRAINCLOUD Unity Plugin
    }
}
```
Next, we create a BCConfig GameObject and attach the BCConfig script as a component.

![](images/BCConfig-1024x674.png)

We have a script called BrainCloudInterface.cs which is used to interface between the BRAINCLOUD Wrapper and our game-related classes. This script handles all of our BRAINCLOUD Authentication methods and all of our calls and callbacks from our BRAINCLOUD wrapper.Â 

Email Authentication:
```js
public void AuthenticateEmail()
{
    m_emailId = DataManager.instance.EmailID;
    m_emailPwd = DataManager.instance.EmailPass; 
 
    _bc.ResetStoredProfileId();
    _bc.ResetStoredAnonymousId();
    _bc.AuthenticateEmailPassword(m_emailId, m_emailPwd, true, OnSuccess_Authenticate, 
                                  OnError_Authenticate);
}
```
Universal Authentication:
```js
public void AuthenticateUniversal()
{
    m_universalUserId = DataManager.instance.UniversalUserID;
    m_universalPwd = DataManager.instance.UniversalPass;
 
    _bc.ResetStoredProfileId();
    _bc.ResetStoredAnonymousId();
    _bc.AuthenticateUniversal(m_universalUserId, m_universalPwd, true, OnSuccess_Authenticate, 
                              OnError_Authenticate);
}
```
Anonymous Authentication:
```js
public void AuthenticateAnonymous()
{
    _bc.AuthenticateAnonymous(OnSuccess_Authenticate, OnError_Authenticate);
}
```
Google Authentication
```js
public void AuthenticateGoogle()
{
    _bc.AuthenticateGoogle(m_googleId, m_serverAuthCode, true, OnSuccess_Authenticate, OnError_Authenticate);
}
```
Authentication Success and Failure Callbacks
```js
public void OnSuccess_Authenticate(string responseData, object cbObject)
{
    m_authStatus = "Authenticate successful!";
    Debug.Log(m_authStatus);
 
    ScreenManager.instance.ActivateMainScreen();
}
public void OnError_Authenticate(int statusCode, int reasonCode, string statusMessage, object cbObject)
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", statusCode, reasonCode, statusMessage));
}
```
This example also features advanced authentication. We are able to send extra Json data in the form of a <string, object> dictionary.Â 
```js
public void AuthenticateAdvanced(AuthenticationType authType, BrainCloud.AuthenticationIds ids, Dictionary<string, object> extraJson)
{
    SuccessCallback successCallback = (response, cbObject) => 
    { ScreenManager.instance.ActivateMainScreen(); };
 
    FailureCallback failureCallback = (status, code, error, cbObject) => 
    { Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error)); };
 
    _bc.AuthenticateAdvanced(authType, ids, true, extraJson, successCallback, failureCallback);
}
```
## **Further Reading**

You can find more information on the Authentication methods by visiting this section of the API reference:Â 

[Authentication APIs](/api/capi/authenticationentication)

The code in the example project that deals with authentication is located in âScripts/BrainCloudInterface.csâ.