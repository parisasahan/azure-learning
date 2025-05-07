# Azure Logic App Lab Guide: Sending Email Using Recurrence Trigger

## Objective

Create an Azure Logic App that triggers on a schedule (recurrence) and sends an email using a Gmail account.

---

## Prerequisites

* Azure subscription
* Gmail account
* Basic knowledge of Azure Portal

---

## Step-by-Step Instructions

### Step 1: Sign In to Azure Portal

1. Go to [https://portal.azure.com](https://portal.azure.com)
2. Sign in with your Azure credentials

   ![](image/16.png)




   ![Azure Login Page](image/pass.png)
   
### Step 2: Create a Logic App

1. In home page we will be seeing an search bar in that
2. Search for **Logic App** and select **Logic App (Consumption)**

 ![Azure Login Page](image/search.png)
 
3. Click **Create**

 ![Azure Login Page](image/add.png)
 
4. Fill in the details:

   * **Subscription**: Select your subscription
   * **Resource Group**: Create or select an existing group
   * **Logic App Name**: e.g., `RecurringEmailApp`
   * **Region**: Choose a region close to you
   * **Enable Log Analytics**: Optional
5. Click **Review + Create**, then **Create**

![Azure Login Page](image/first.png)

### Step 3: Define the Trigger (Recurrence)

1. Once deployed, click **Go to resource**

![Azure Login Page](image/goto.png)

2. In the Logic App Designer, choose **Recurrence** as the trigger

![Azure Login Page](image/tri.png)

3. Set the interval:

   * **Frequency**: Minute/Hour/Day (e.g., Minute)
   * **Interval**: 5 (for every 5 minutes)

![Azure Login Page](image/addtri.png)

### Step 4: Add Gmail Email Action

1. Click **+ New Step**

![Azure Login Page](image/13.png)

2. Search for **Gmail**

![Azure Login Page](image/2025-05-07_15-26-12.png)

3. Select **Send email (V2)**
4. Sign in with your Gmail account and authorize the connection

![Azure Login Page](image/emailv2.png)

5. Configure the action:

   * **To**: Enter your email address (e.g., `example@gmail.com`)
   * **Subject**: Hello from Azure Logic App
   * **Body**: Hello from Azure

![Azure Login Page](image/15.png)

### Step 5: Save and Run

1. Click **Save**
2. Your Logic App is now live and will send an email based on the defined recurrence

### Step 6: Monitor the Run

1. In the Logic App blade, click **Runs history**
2. Check for success/failure of each run
3. Click on individual runs for detailed input/output logs

---

## Summary

You have successfully created a Logic App that triggers on a schedule and sends an email using Gmail. This is useful for automating alerts, reminders, or notifications.

---

## Optional Enhancements

* Add dynamic date/time to the email body
* Log emails to a storage account or database
* Add conditions or branching logic

