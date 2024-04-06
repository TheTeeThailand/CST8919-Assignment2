# CST8919-Assignment2

# Group Members
- Parvezbhai Malek
- Yash Solanki
- Thep Rungpholsatit
  
# Part-1: Understanding Anomaly Detection
# Anomaly Detection Techniques for Security Log Analysis

Anomaly detection techniques are vital for identifying abnormal behavior within security logs, which can signify potential security threats or breaches. This document outlines common anomaly detection techniques applicable to security log analysis.

## Statistical Anomaly Detection

- **Mean and Standard Deviation Method**: This method calculates the mean and standard deviation of a metric (e.g., number of login attempts per hour) and flags data points that fall significantly outside of these parameters as anomalies.
  
- **Z-Score Method**: Similar to the mean and standard deviation method, the Z-score measures how many standard deviations a data point is from the mean. Data points with high Z-scores are considered anomalies.

## Machine Learning-Based Anomaly Detection

- **Unsupervised Learning**: Techniques like clustering (e.g., k-means clustering) can be used to identify groups of similar log entries and flag outliers as anomalies.
  
- **Supervised Learning**: Anomalies can be detected using supervised learning algorithms like decision trees, random forests, or support vector machines trained on labeled data with both normal and abnormal behavior.

## Rule-Based Anomaly Detection

- **Threshold-Based Rules**: Setting thresholds for specific log metrics (e.g., number of failed login attempts) and flagging any values that exceed these thresholds as anomalies.
  
- **Pattern-Based Rules**: Creating rules based on known attack patterns or suspicious activities and using these rules to detect anomalies in logs.



# Part 2: Preparing for Automation

## In this step, we created azure automation account named as "assignment2".


![Screen Shot 2567-04-05 at 12 41 21](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/955bb191-a2b9-4848-a0ad-c3177e5fc471)


![Screen Shot 2567-04-05 at 12 43 07](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/5f774c2a-a0f9-488b-8300-5358e51e51f7)


## Powershell Runbook created:

- Runbooks are scripts (PowerShell or Python) that automate repetitive tasks or workflows within Azure. They can be manually executed, scheduled to run at specific times, or triggered by events.
 
![Screen Shot 2567-04-05 at 12 44 22](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/2538974a-0a6f-440b-8bdc-834242a25085)

![Screen Shot 2567-04-05 at 12 44 49](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/7d1b6a11-ace6-497c-bf15-e0d461114601)

 
 ## Connect to Azure Log Analytics:

![WhatsApp Image 2024-04-05 at 8 57 11 PM (1)](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/49e43aeb-939e-4eef-a418-3bd4c1aaa963)

![WhatsApp Image 2024-04-05 at 8 57 11 PM](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/3e95d80d-de36-4401-ad61-c26b8b1636e1)

## logs

![Screen Shot 2567-04-05 at 13 32 13](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/17b55327-b51a-417f-977d-171deb527e35)

## Creating an Azure Logic App

- Configure the Logic App trigger to activate every two minutes, ensuring that the app consistently checks for new data or carries out its assigned tasks at this interval, thus maintaining up-to-date functionality.

![Screen Shot 2567-04-05 at 16 14 08](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/469ff894-888f-4d81-a584-d5e84568e887)

- Add an Action:

![Screen Shot 2567-04-05 at 19 01 35](https://github.com/TheTeeThailand/CST8919-Assignment2/assets/157184669/3d60bbc5-45f9-4cf4-9e54-d202d2e3b352)

  


