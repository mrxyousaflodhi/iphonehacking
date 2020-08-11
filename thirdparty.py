Apple Support iOS Application - Unencrypted Third Party Analytics (CVE-2017-7147)
 
Overview
 
"Need help? Apple Support app is your personalized guide to the best options from Apple. Find answers with articles tailored to your products and questions. Call, chat or email with an expert right away, or schedule a callback when itas convenient. Get a repair at an Apple Store or a nearby Apple Authorized Service Provider. Apple Support is here to help."
 
(https://itunes.apple.com/us/app/apple-support/id1130498044)
 
Issue
 
The Apple Support iOS application (version 1.1.1 and below) sends potentially sensitive information such as mobile carrier, install date and time, number of app launches, device model, iOS version and screen resolution, unencrypted to a third party site (Adobe Marketing Cloud).
 
Impact
 
An attacker who can monitor network traffic could capture potentially sensitive information about the iOS device without the user's knowledge.
 
Timeline
 
June 16, 2017 - Notified Apple via product-security@apple.com
June 16, 2017 - Apple sent an auto acknowledgment
June 16, 2017 - Apple responded stating that they are investigating
July 10, 2017 - Asked for a status update
July 10, 2017 - Apple responded stating that they are still investigating
August 21, 2017 - Asked for a status update
August 21, 2017 - Apple responded stating that they are still investigating
August 30, 2017 - Apple released version 1.2 which sends the analytics data over an encrypted connection
October 17, 2017 - Apple published a security advisory to document the issue
 
Solution
 
Upgrade to version 1.2 or later
 
https://support.apple.com/en-ca/HT208201
https://support.apple.com/en-us/HT201222
 
CVE-ID: CVE-2017-7147
 
#  0day.today [2020-08-11]  #