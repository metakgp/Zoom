from fbscraper import get_aggregated_feed as get_id
import json
import requests
import email_functions
import Logger

logger = Logger.Logger(name='RunLog')

def slack_notification(data):
    with open('./SLACK_URL', 'r') as f:
        url = f.readline().rstrip('\n')
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(
        url, headers=headers, data=data)

def message_sender(curr_id, flag):
    posts = json.load(open('metakgp.json', 'r'))

    mail_msg = ""
    post_no = 1
    
    old_id = curr_id['last_post']

    for post in posts:
        if post['id'] == old_id:
            break
        else:
            mail_msg += "Post No. {}\n{}\n\nPosted On : {} at {}\nLink to the post : https://www.facebook.com/{}\n\n".format(str(post_no),post['message'],post['real_date'],post['real_time'],post['id'] )
            post_no += 1

            # for subscribers in page['subs'] :
            try:
                pic = post['pic']
            except KeyError:
                print("KeyError")
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


        if post_no == 2 and flag :
            break 

    if mail_msg is not "" :
        mail_status = email_functions.send_mail("New Post on MetaKGP facebook page" , mail_msg)
        if mail_status :
            old_id = posts[0]['id']
            logger.addLog("New posts sent successfully")
            json.dump(curr_id,open('lastid.json' , 'w'))
        else :
            logger.addLog("There was error in sending mail" , "error")
    else :
        logger.addLog("No new post")

def main():
    try:
        lastid = json.load(open('lastid.json', 'r'))
        flag = False

    except (FileNotFoundError, IOError) as err:
        lastid = {'last_post': None}
        flag = True

    new_id = get_id("metakgp")

    if new_id != lastid['last_post']:  # It means something new was posted
        message_sender(lastid, flag)
        lastid['last_post'] = new_id

    json.dump(lastid, open('lastid.json', 'w'))

main()
