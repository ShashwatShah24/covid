import json
import requests
import time
import urllib
import requests
from chat_inv_manage import *
from airtel_care_chat_script import *
import time
import datetime

               
now = datetime.datetime.now()
date_time= (now.strftime("%Y-%m-%d %H:%M:%S"))
print("$$$Program Initiated,Welcome Current Time: ",date_time,"$$$")

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(chat_id,URL,text):
    if chat_id!="" or chat_id!=None:
        text = urllib.parse.quote_plus(text)
        # print("Message Reply",text)
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        get_url(url)

def get_new_members_details_and_updates(updates):
    new_member_dict={'update_id':None,'chat_id':None,'chat_first_name':None,'new_member_chat_id':None,'member_is_bot':None,'member_name':None,'chat_type':None,'date':None}
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_type=updates["result"][last_update]["message"]["chat"]["type"]
    try:
        if (chat_type=="supergroup") or (chat_type=="group"):
            update_id=updates["result"][last_update]["update_id"]
            member_chat_id=updates["result"][last_update]["message"]["new_chat_participant"]["id"]
            member_is_bot=updates["result"][last_update]["message"]["new_chat_participant"]["is_bot"]
            member_name=updates["result"][last_update]["message"]["new_chat_participant"]["first_name"]
            chat_id = updates["result"][last_update]["message"]["chat"]["id"]
            chat_first_name=updates["result"][last_update]["message"]["chat"]["title"]
            date = updates["result"][last_update]["message"]["date"]
            datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date))

            print("New Chat Members",chat_type)
            new_member_dict={'update_id':update_id,'chat_id':chat_id,'chat_first_name':chat_first_name,'new_member_chat_id':member_chat_id,'member_is_bot':member_is_bot,'member_name':member_name,'chat_type':chat_type,'date':datetime}

    except Exception as err:
        print(err)
    finally:
        print(new_member_dict)
        return new_member_dict

def get_last_chat_details_and_text(updates):
    datetime=""

    update_dict={'update_id':None,'message_id':None,'chat_id':None,'message_from_id':None,'chat_first_name':None,'message_from_first_name':None,'chat_type':None,'date':None,'text':None}

    try:  
        # print(updates)
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        # last_msg=updates["result"][last_update]
        # print(last_msg)
        chat_type=updates["result"][last_update]["message"]["chat"]["type"]

        if chat_type=="private":

            message_id=updates["result"][last_update]["message"]["message_id"]
            update_id=updates["result"][last_update]["update_id"]
            chat_type=updates["result"][last_update]["message"]["chat"]["type"]
            text = updates["result"][last_update]["message"]["text"]
            date = updates["result"][last_update]["message"]["date"]
            datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date))
            chat_id = updates["result"][last_update]["message"]["chat"]["id"]
            chat_first_name=updates["result"][last_update]["message"]["chat"]["first_name"]
            message_from_id=updates["result"][last_update]["message"]["from"]["id"]
            message_from_first_name=updates["result"][last_update]["message"]["from"]["first_name"]
        
            update_dict={'update_id':update_id,'message_id':message_id,'chat_id':chat_id,'message_from_id':message_from_id,'chat_first_name':chat_first_name,'message_from_first_name':message_from_first_name,'chat_type':chat_type,'date':datetime,'text':text}
            # print(update_dict)
            # return chat_type,text, chat_id,date,chat_id,chat_first_name,message_from_id,message_from_first_name

        if (chat_type=="supergroup") or (chat_type=="group"):
            message_id=updates["result"][last_update]["message"]["message_id"]
            update_id=updates["result"][last_update]["update_id"]
            chat_type=updates["result"][last_update]["message"]["chat"]["type"]
            text = updates["result"][last_update]["message"]["text"]
            date = updates["result"][last_update]["message"]["date"]
            datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date))
            chat_id = updates["result"][last_update]["message"]["chat"]["id"]
            chat_first_name=updates["result"][last_update]["message"]["chat"]["title"]
            message_from_id=updates["result"][last_update]["message"]["from"]["id"]
            message_from_first_name=updates["result"][last_update]["message"]["from"]["first_name"]
            # print(chat_type,text, chat_id,date,chat_id,chat_first_name,chat_from_id,chat_from_first_name)

            update_dict={'update_id':update_id,'message_id':message_id,'chat_id':chat_id,'message_from_id':message_from_id,'chat_first_name':chat_first_name,'message_from_first_name':message_from_first_name,'chat_type':chat_type,'date':datetime,'text':text}
            # print(update_dict)

    except Exception as err:
        print(err)

    finally:
        return update_dict ##Returns Updates chats and parameters dict and chat id 


def chatHandler(updates,URL,dbname,tablename):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    inv_tablename=tablename+"_support_inv"
    try:
        if 'new_chat_participant' in (updates["result"][last_update]["message"]).keys():
        # if  in (updates["result"][last_update]):
            print("New Member Found")
            tablename=tablename+'_members_db'
            new_member_dict=get_new_members_details_and_updates(updates)
            if new_member_dict.get('update_id')!=None:
                print("New Member Details",new_member_dict)
                reply_msg=chat_reply_handler(new_member_dict)
                send_message(new_member_dict.get('chat_id'),URL,reply_msg)  #### Send reply 
                chat_to_db(new_member_dict,dbname,tablename)
        else:
            print("@@@ New text Message Found @@@")
            chat_updates_dict=get_last_chat_details_and_text(updates) ####Get latest Message and Parameters  / chat id
            if chat_updates_dict.get('update_id')!=None:
                chat_to_db(chat_updates_dict,dbname,tablename)
                reply_msg=chat_reply_handler(chat_updates_dict) ###Get Response message based on user message ,If Required 
                print("###--- Incoming Message:",chat_updates_dict.get('text'),"---###")
                print("###--- Current Time:",date_time,"---###")
                print("###--- chat_id:",chat_updates_dict.get('chat_id'),"---###")
                print("###--- Name:",chat_updates_dict.get('message_from_first_name'),"---###")
                print("###--- reply_msg:",reply_msg,"---###")
                if (chat_updates_dict.get('chat_type'))=='group' or (chat_updates_dict.get('chat_type'))=='supergroup':
                    if ("need" in chat_updates_dict.get('text')) or ("not working" in chat_updates_dict.get('text')) or ("down" in chat_updates_dict.get('text')) or ("slow" in chat_updates_dict.get('text')) or ("new" in chat_updates_dict.get('text')) or ("bad" in chat_updates_dict.get('text')) or ("connection" in chat_updates_dict.get('text')) or ("add" in chat_updates_dict.get('text')) or ("bill" in chat_updates_dict.get('text')) or ("price" in chat_updates_dict.get('text')) or ("service" in chat_updates_dict.get('text')):
                        send_message(chat_updates_dict.get('chat_id'),URL,reply_msg) #### Send reply
                        send_message(chat_updates_dict.get('message_from_id'),URL,help_message)

                     
                else:
                    send_message(chat_updates_dict.get('message_from_id'),URL,reply_msg) #### Send reply

    except Exception as err:
        print(err)
        pass


def main():
    chatHandler(updates,URL,dbname,tablename)

if __name__ == "__main__":
    main()

