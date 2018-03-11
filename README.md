# Zoom
This script sends an email when a new post is posted on the Facebook page <a href="https://www.facebook.com/metakgp">MetaKGP</a> to metakgp-announce@googlegroups.com. It will also update the #recent-changes in slack channel of MetaKGP.

## How to use 
* Create a file CONFIG in the root diretory as follows : <br>
{"email":"FROM_EMAIL","pass":"FROM_EMAIL_PASSWORD" ,"to":"TO_EMAIL"} <br><br>
For the script to work please ensure that access to less secure apps is enabled for `FROM_EMAIL` 
It can be done by going <a href="https://www.google.com/settings/security/lesssecureapps">here</a>. 
<br><br>
* Get a Facebook API token and save it in file name `ACCESS_TOKEN`. See this [StackOverflow Answer](http://stackoverflow.com/a/16054555/1780891).
<br>
* Create a file named `SLACK_URL` and update it with your webhook url. 
<br>
<br>
Note that this script requires python 3 or higher to run.
