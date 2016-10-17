from fbscraper import get_aggregated_feed as get_id
import json
import requests


def slack_notification(data):
    with open('./SLACK_URL', 'r') as f:
        url = f.readline().rstrip('\n')
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(
        url, headers=headers, data=data)


def message_sender(old_id):
    posts = json.load(open('metakgp.json', 'r'))
    for post in posts:
        if post['id'] == old_id:
            break
        else:
            # for subscribers in page['subs'] :
            try:
                pic = post['pic']
            except KeyError:
                pic = False
                #msg = "<strong>{}</strong>{}\nPosted on : {} at {} \n<a href='https://www.facebook.com/{}'>View the post</a>".format(page['name'],post['message'],post['real_date'],post['real_time'],post['id'])
            if pic:
                data = json.dumps(
                    {
                        "img_url": pic,
                        "text": "*{}*\n{}\nPosted on : {} at {} \n<https://www.facebook.com/{}|View the post>".format(
                            'MetaKGP',
                            post['message'],
                            post['real_date'],
                            post['real_time'],
                            post['id'])})

            else:
                data = json.dumps({"text": "*{}*\n{}\nPosted on : {} at {} \n<https://www.facebook.com/{}|View the post>".format(
                    'MetaKGP', post['message'], post['real_date'], post['real_time'], post['id'])})
            slack_notification(data)


def main():
    try:
        lastid = json.load(open('lastid.json', 'r'))
    except FileNotFoundError:
        lastid = {'last_post': None}
    new_id = get_id("metakgp")
    if new_id != lastid['last_post']:  # It means something new was posted
        message_sender(lastid['last_post'])
        lastid['last_post'] = new_id
    json.dump(lastid, open('lastid.json', 'w'))
main()
