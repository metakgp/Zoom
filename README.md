# Zoom
This script sends an email when a new post is posted on the Facebook page <a href="https://www.facebook.com/metakgp">MetaKGP</a> to metakgp-announce@googlegroups.com. It will also update the #recent-changes in slack channel of MetaKGP.

## How to use 
Create a file CONFIG in the root diretory as follows : <br>
{"email":"FROM_EMAIL","pass":"FROM_EMAIL_PASSWORD" ,"to":"TO_EMAIL"} <br><br>
For the script to work please ensure that access to less secure apps is enabled for FROM_EMAIL 
It can be done by going <a href="https://www.google.com/settings/security/lesssecureapps">here</a>. 
<br><br>
Get your facebook app access token and save it to a file named FB_ACCESS_TOKEN.
<br>
Create a file named SLACK_URL and update it with your webhook url.
<br>
Note that this script requires python 3 or higher to run.
