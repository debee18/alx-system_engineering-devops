
Postmortem: The Great Web Service Outage - September 14, 2023

Outage Diagram

Summary:

Duration:
Start: September 14, 2023, 11:30 AM WAT (West Africa Time)
End: September 14, 2023, 12:45 PM WAT
Impact:
Approximately 30% of our users experienced slow response times and errors during the outage.
Root Cause:
The outage was attributed to an unexpected surge in database connections that overwhelmed the database server.
🌩️ The Storm Hits 🌩️

Imagine this: You're sipping your coffee, enjoying a sunny day in Nigeria when suddenly, BAM! The storm of database connections hit our web service like a tidal wave. But don't worry; we've got the umbrellas (and solutions) ready!

Timeline:

11:30 AM WAT: Issue was initially detected as monitoring alerts indicated a significant increase in response latency and error rates. We realized our servers were not just taking a coffee break.
11:35 AM WAT: Our valiant engineering team sprang into action like caped crusaders, ready to save the day.
11:40 AM WAT: Initial suspicion centered around a recent code deployment, but deployment logs showed no irregularities. We ruled out the caffeine shortage in the code.
11:50 AM WAT: Attention shifted to the database, and logs revealed an unprecedented spike in connection attempts. We found out our database was the cool kid everyone wanted to hang out with.
12:00 PM WAT: The possibility of a Distributed Denial of Service (DDoS) attack was considered, but traffic analysis did not align with typical attack patterns. Our servers just threw a surprise party!
12:15 PM WAT: It was determined that the problem stemmed from a surge in legitimate user traffic, not a malicious attack. Our servers apologized for the confusion.
12:30 PM WAT: The incident was escalated to the database administration team, who swiftly addressed the database connection overload. The database team became the real heroes, wielding connection pooling magic.
12:45 PM WAT: The issue was successfully resolved through optimization of database connection pooling settings. Our servers calmed down and went back to work.
Root Cause and Resolution:

The root cause of the outage was identified as an abrupt and substantial increase in database connection attempts, primarily due to higher-than-anticipated user traffic. This surge overwhelmed the database server's capacity to handle incoming connections. We had a "too many friends at the party" situation.

To resolve the issue, the following corrective action was taken:

Database Connection Pooling Optimization: We reconfigured the database connection pooling settings to efficiently manage and recycle connections, thus preventing the database from becoming overburdened during peak traffic periods. We taught our servers some manners and how to handle popularity.
Corrective and Preventative Measures:

In light of this incident, we are implementing the following measures:

Capacity Planning: A comprehensive analysis of traffic patterns will be conducted, including a crash course on predicting surges in user activity, leading to the expansion of our infrastructure.
Enhanced Monitoring: We're bringing in the best surveillance equipment (monitoring systems) to promptly identify abnormal traffic patterns and database connection issues in real-time. Sherlock Holmes would be proud.
Auto-Scaling: The exploration of auto-scaling capabilities for both web and database servers to dynamically adjust resources based on fluctuating traffic demands. Our servers will become shape-shifters.
User Communication: Improved communication strategies will be implemented, including cute cat GIFs during outages, thereby mitigating user frustration. We know the way to your hearts!
In conclusion, the recent outage, though unexpected, has provided valuable insights into enhancing our system's resilience. We've not only identified the root cause and implemented immediate solutions but also sprinkled some humor into the mix. We deeply appreciate your patience and understanding as we continue to elevate the reliability of our services and entertain you along the way. 🚀






