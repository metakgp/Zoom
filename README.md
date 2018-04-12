# Zoom

This script sends an email when a new post is posted on the Facebook page
[Metakgp](https://www.facebook.com/metakgp) to
`metakgp-announce@googlegroups.com`. It will also update the
`#recent-changes` slack channel on the [Metakgp Slack](https://metakgp.slack.com).

## Usage

* Create a file CONFIG in the root diretory as follows:

```sh
{
	"email":"FROM_EMAIL",
	"pass":"FROM_EMAIL_PASSWORD",
	"to":"TO_EMAIL"
}
```

For the script to work please ensure that access to less secure apps is enabled
for `FROM_EMAIL`. It can be done by going
[here](https://www.google.com/settings/security/lesssecureapps).

* Get a Facebook API token and save it in a file caled
`ACCESS_TOKEN`. See this [StackOverflow
Answer](http://stackoverflow.com/a/16054555/1780891)

* Create a
file named `SLACK_URL` and update it with your webhook url

**Note:** This script requires python 3 or higher.

## License 

GNU LGPL.

