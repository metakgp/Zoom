# email_functions.py

import Logger
import os
import requests

logger = Logger.Logger(name='RunLog')
key = os.getenv('MAILGUN_API_KEY')
recipient = os.getenv('SENDEE_EMAIL_ID')
sandbox = 'zoom.metakgp.org'


def send_mail(mail_subject, mail_body) :
	#sending mail
	try:
		request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)

        request = requests.post(request_url, auth=('api', key), data={
            'from': 'zoom@zoom.metakgp.org',
            'to': recipient,
            'subject': mail_subject,
            'text': mail_body
        })

        print('Status: {0}'.format(request.status_code))
        print('Body:   {0}'.format(request.text))

		return True

	except :
		return False
