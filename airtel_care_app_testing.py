import json
import requests
import time
from chat_handler import *

TOKEN= "1736303811:AAGqweb5JQ63Oo4Drs1OINTQt7ZMUzeNlVQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
dbname ="telemedia_db"
tablename ='testing_chat_bot'

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)



def internetcheck():
	success = False
	attempts = 0
	while not success and attempts < 15: # or however many times you want to attempt
		#print("00000000 success:",success,attempts)
		try:
			js=get_updates(offset=None)
			print('internetcheck js',js)
			success = True
		except:
			time.sleep(5)
			print("---url attempts:",attempts)
			attempts+=1
		
	return js

def main():
	try:
		count=0
		last_update_id = None
		#print("main coreapp stage1")
		while True:
			count+=1;print(count,end=",")
			if count==100:
				text=" bot Status : Running"
				send_message(751552666,URL,text)
				print("###---Server is running Current Time",datetime.datetime.now(),"---###")
				count=0

			try:
				updates = get_updates(last_update_id)
			except:
				updates =internetcheck()
				
			if len(updates["result"]) > 0:
				last_update_id = get_last_update_id(updates) + 1
				chatHandler(updates,URL,dbname,tablename)
			time.sleep(0.1)
   
			

	except Exception as err:
		print("---main function implementation failed(66,CoreApp.py)---",err)
		pass

if __name__ == '__main__':
    main()

