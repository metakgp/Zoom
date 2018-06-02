# email_functions.py

import Logger
import os
import requests

logger = Logger.Logger(name='RunLog')
key = os.getenv('MAILGUN_API_KEY')
sender = os.getenv('SENDER_EMAIL_ID')
recipient = os.getenv('RECIPIENT_EMAIL_ID')
sandbox = os.getenv('MAILGUN_DOMAIN')


def send_mail(mail_subject, mail_body) :
    #sending mail
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)

    try:
        request = requests.post(request_url, auth=('api', key), data={
            'from': sender,
            'to': recipient,
            'subject': mail_subject,
            'text': mail_body
        })

        return request.status_code

    except requests.exceptions.RequestException as e:
        return e
