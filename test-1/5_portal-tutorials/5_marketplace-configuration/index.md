---
title: "Marketplace Configuration"
date: "2015-08-10"
---

BRAINCLOUD allows the developer to create and customize their marketplace. By defining a set of products, you can administer which products are available, for which users, and for what price. BRAINCLOUD also allows you to integrate with third-party store systems such as iTunes, Google Play, Facebook, Steam, Microsoft Store (Phone and Desktop/Tablet).

Below is a quick guide to configuring the BRAINCLOUD marketplace.

### CreateÂ a Virtual Currency

In order to create a product in the marketplace, you need to have a virtual currency to award the player. Let's start by creating a virtual currency.

- Navigate to the "Marketplace | Virtual Currencies" page in the design tab of the BRAINCLOUD portal  
    [](images/BRAINCLOUD_dashboard_marketTab.jpg)
- Click the + icon in the top right corner  
    [](images/BRAINCLOUD_dashboard_addVC.jpg)
- Enter a name for your virtual currency (it can be anything you want) and click Save  
    [](images/BRAINCLOUD_dashboard_addVC2.jpg)
- You should now see your virtual currency listed in the table  
    [](images/BRAINCLOUD_dashboard_addVC3.jpg)

### Create a Product

Now that you have a virtual currency defined, it's time to create a product so that users can purchase that virtual currency! To create a marketplace product do the following:

- Navigate to the "Marketplace | Products" page in the design tab of the BRAINCLOUD portal  
    [](images/BRAINCLOUD_dashboard_productsTab.jpg)
- Click the "Add Product" button in the top right  
    [](images/BRAINCLOUD_dashboard_addProduct1.jpg)
- In the Create Product dialog enter the following information:
    - **Item Id** -Â This is a unique idÂ for your product. You will use this id within the BRAINCLOUD APIs to identify your product.
    - Â **Title** - The title of your product
    - **Category** - An optional field that allows you to categorize your products. When communicating with BRAINCLOUD you can ask for only a certain category of product (for cases where you have many products defined)
    - **Description** \- Description of your product
    - **Product Type**Â - Configures what type of product you are defining. This is mostly related to the third party store that you are linking to the product.
        - **Consumable** - A one-time consumable product. Once purchased, this product will be consumed once and only once. Most products fall into this product type
        - **Non-consumable** - A product which can never be consumed. Buying an item in your gameÂ that can never be used up (say a special sword) might be an example of a non-consumable.
        - **Subscription** - A subscription to something in your app. Again this is mostly determined by the third party store item configuration as subscriptions generally incur some sort of regular charge to the end user.
    - **Currency Type** - The type of virtual currency to award
    - **Currency Value** - The amount of virtual currency to award
    - **Prices** - A list of prices for the item. We will configure this in the next section so you can leave it blank for now.
    - **Extra Data** - Any custom key/value data pairs you'd like to attach to the product.
- Click Save

### Add Prices to Your Product

After havingÂ created a product, you'll want to attach some prices to it so that users can see and purchase it. Products by default are created with a "Not for sale" price which means they won't show up in any of the BRAINCLOUD API requests for products. Let's add a price so we can see our product.

#### Add a defaultÂ price

- If you just created the product, you should already see the "Add Price" button for your product. If not, select a product in the marketplace product table and make sure the product is inÂ "Edit" mode.  
    [](images/BRAINCLOUD_dashboard_addProduct2.jpg)
- Click the Add Price button  
    [](images/BRAINCLOUD_dashboard_addProduct3.jpg)
- Enter a default price which will be used to calculate internal BRAINCLOUD analytics such as daily/total revenue. Note this is NOT the actual price charged to the user. That information is defined elsewhere depending on the third party store being integrated. At this time you can also enter your third-party store information. If you're unsure of what to enter here please refer to the "Third Party Store Integration" tutorials in the portal section for your appropriate third-party store.  
    [](images/BRAINCLOUD_dashboard_addProduct4.jpg)
- Click Save.
- Next, we canÂ select our newly created price as the default. Note you may have to hit the "Edit" button at the top of the product dialog.  
    [](images/BRAINCLOUD_dashboard_addProduct5.jpg)
- Click Save and that's it!
- For the more curious amongst you, you can also verifyÂ that your product is coming back in the Product "GetInventory" APIÂ call using the Cloud Code API Explorer  
    [](images/BRAINCLOUD_dashboard_addProduct6.jpg)

#### Add an "on sale"Â price

The marketplace allows for multiple prices to be attached to a product. This allows you to put certain items on sale - say for instance a 50% sale. In fact, because multiple prices can be entered, your product could have a 25% and 75% off sale too!

[![BRAINCLOUD](images/BRAINCLOUD_dashboard_addProduct7.jpg)](images/BRAINCLOUD_dashboard_addProduct7.jpg)

In order to add another price to your product, you can basically follow the steps above and then enter a different reference price and third party store id.
