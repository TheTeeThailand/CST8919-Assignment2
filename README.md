# CST8919-Assignment2
# Anomaly Detection Techniques for Security Log Analysis

Anomaly detection techniques are vital for identifying abnormal behavior within security logs, which can signify potential security threats or breaches. This document outlines common anomaly detection techniques applicable to security log analysis.

## Rule-Based Approaches

- Number of Failed Login Attempts
Set a threshold for the maximum allowed failed login attempts within a specific time frame. Flag users exceeding this threshold as potential anomalies.

- Unusual File Access Patterns
Define thresholds for file access frequency or volume (reads, writes, deletes). Flag unusually high or low access rates as anomalies.

- Network Traffic Volume
Monitor network traffic and set thresholds for data volume or packet counts. Flag sudden spikes or drops as anomalous activity.

- Resource Utilization
Define thresholds for CPU, memory, disk usage, etc. Flag abnormal spikes or prolonged high utilization as potential issues.

## Statistical Methods

- Standard Deviation Analysis: Calculate standard deviation and flag deviations exceeding a threshold.
- Moving Averages: Use moving averages to detect deviations from expected patterns.
- Z-Score Analysis: Calculate Z-scores and flag anomalies beyond a threshold.

## Machine Learning-Based Techniques

- Supervised Learning: Train a model to classify log entries as normal or anomalous based on historical data.
- Unsupervised Learning: Use clustering algorithms to identify clusters deviating from the norm.
- Semi-Supervised Learning: Combine labeled and unlabeled data to detect anomalies with fewer false positives.

## Behavioral Analysis

- User and Entity Behavior Analytics (UEBA): Monitor behavior for deviations like unusual access times or locations.
- Session Analysis: Detect anomalies such as long-duration sessions, multiple failed login attempts, or concurrent logins from different locations.

Feel free to customize and expand upon these techniques based on your specific security log analysis needs.
