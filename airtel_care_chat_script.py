import requests
import pandas as pd

from chat_inv_manage import *



def bot_reply(dict):
   
    try:
        incoming_msg=dict.get('text')
        chat_type=dict.get('chat_type')
        message_from=dict.get('message_from_first_name')
        chat_id=dict.get('chat_id')
        text=""
        if chat_type=='private':
            
            if "hi there" or "how are you" or "is anyone there?" or "hey" or "hola" or "hello" or "good day" in incoming_msg:
                print("reached")
                text="Hi,Welcome \n please use #help or help to use sevice"

            if "bye" or "see you later" or "goodbye" or "nice chatting to you, bye" or "till next time" in incoming_msg:
                text="See you!,Have a nice day"
            
            if "Thanks" or "Thank you" or "That's helpful" or "Awesome, thanks" or "Thanks for helping me" in incoming_msg:
                text="Happy to help!"
               
            if "#help" or "/start" or "help" in incoming_msg:
                 text='''
                    Hi,This is a bot which tells you all available things required Durring Covid\n
                    a:medicine and injection\n
                    b:Hospital Beds\n
                    c:Oxygen Supplies\n
                    d:Plasma\n
                    e:Others\n
                    
                    So,please write your city and above option:
                    ex:delhi a
                    

                     '''  
            if "delhi a" in incoming_msg or "Delhi a" in incoming_msg:
                text="""For Remdesivir:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Medicines%20and%20Injections&widgetId=60851974e301077967f25725   \n
                For Tocilzumab:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Medicines%20and%20Injections&widgetId=608c0e461e0f1b3803a08cc7  \n
                For Fabiflu:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Medicines%20and%20Injections&widgetId=608c0ed0b7cd1c7c449c90dd  \n
                For Favipiravir: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Medicines%20and%20Injections&widgetId=608c0effb7cd1c7c449ca2d5
                """
            if ("delhi b" in incoming_msg) or "Delhi b" in incoming_msg:
                text="""For OXYGEN Beds:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Hospital%20Beds&widgetId=608c15d870e27e2f0d040248   \n
                For ICU Beds:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Hospital%20Beds&widgetId=608c160470e27e2f0d041253  \n
                For Ventilator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Hospital%20Beds&widgetId=608c166370e27e2f0d0433e9  \n
                For Home Ventilator: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Hospital%20Beds&widgetId=608c16a370e27e2f0d044afb
                """
            if "delhi c" in incoming_msg or "Delhi c" in incoming_msg:
                text="""For OXYGEN Cylinder: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Oxygen%20Supplies&widgetId=608c0f23b7cd1c7c449cb1cc   \n
                For OXYGEN Regulator:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Oxygen%20Supplies&widgetId=608c0f5e81b8c80c6a75ff28  \n
                For OXYGEN Concentrator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Oxygen%20Supplies&widgetId=608c15a270e27e2f0d03effd  \n
                For Oximeter:https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Oxygen%20Supplies&widgetId=608c17be70e27e2f0d04bcb1
                """
            if "delhi d" in incoming_msg or "Delhi d" in incoming_msg:
                text="""For PLASMA:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Plasma&widgetId=608c16ed70e27e2f0d0466e2   \n
                    """
            if "delhi e" in incoming_msg or "Delhi e" in incoming_msg:
                text="""For Govenment Links:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Others&widgetId=60896b1cd5ecb727f9d9b249   \n
                For Food:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Others&widgetId=608c172470e27e2f0d047ad7  \n
                For Provide Help:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Others&widgetId=608c174e70e27e2f0d04897f  \n
                For Ambulance: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/1?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=1%241_Others&widgetId=608c177470e27e2f0d0498f1
                """
                
                
            if "gurgaon a" in incoming_msg or "Gurgaon a" in incoming_msg:
                text="""For Remdesivir:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Medicines%20and%20Injections&widgetId=608c1e3cfce18a42ebf9583c   \n
                For Tocilzumab: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Medicines%20and%20Injections&widgetId=608c1e45fce18a42ebf95b47  \n
                For Fabiflu:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Medicines%20and%20Injections&widgetId=608c1e4ffce18a42ebf95f07  \n
                For Favipiravir: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Medicines%20and%20Injections&widgetId=608c1e5ffce18a42ebf96745
                """
            if ("gurgaon b" in incoming_msg) or "Gurgaon b" in incoming_msg:
                text="""For OXYGEN Beds:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Hospital%20Beds&widgetId=608c1e92fce18a42ebf97f3d   \n
                For ICU Beds:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Hospital%20Beds&widgetId=608c1e9bfce18a42ebf9831c  \n
                For Ventilator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Hospital%20Beds&widgetId=608c1eaffce18a42ebf98c2b  \n
                For Home Ventilator: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Hospital%20Beds&widgetId=608c1ec0fce18a42ebf994dd
                """
            if "gurgaon c" in incoming_msg or "Gurgaon c" in incoming_msg:
                text="""For OXYGEN Cylinder: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Oxygen%20Supplies&widgetId=608c1e68fce18a42ebf96b43   \n
                For OXYGEN Regulator:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Oxygen%20Supplies&widgetId=608c1e75fce18a42ebf97274  \n
                For OXYGEN Concentrator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Oxygen%20Supplies&widgetId=608c1e7efce18a42ebf9759c  \n
                For Oximeter:https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Oxygen%20Supplies&widgetId=608c1ef8fce18a42ebf9acf1
                """
            if "gurgaon d" in incoming_msg or "Gurgaon d" in incoming_msg:
                text="""For PLASMA:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Plasma&widgetId=608c1eccfce18a42ebf99a84  \n
                    """
            if "gurgaon e" in incoming_msg or "Gurgaon e" in incoming_msg:
                text="""For Govenment Links:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Others&widgetId=60896a22d5ecb727f9d95c52   \n
                For Food:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Others&widgetId=608c1ed7fce18a42ebf99ed8  \n
                For Provide Help:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Others&widgetId=608c1ee2fce18a42ebf9a3cb  \n
                For Ambulance: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/5?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=5%245_Others&widgetId=608c1eedfce18a42ebf9a83e
                """
                

            if "bangalore a" in incoming_msg or "Bangalore a" in incoming_msg:
                text="""For Remdesivir:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Medicines%20and%20Injections&widgetId=608c1c1cfce18a42ebf872d9 \n
                For Tocilzumab: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Medicines%20and%20Injections&widgetId=608c1c26fce18a42ebf876b7 \n
                For Fabiflu: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Medicines%20and%20Injections&widgetId=608c1c2efce18a42ebf879cf \n
                For Favipiravir: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Medicines%20and%20Injections&widgetId=608c1c3cfce18a42ebf87eb7
                """
            if ("bangalore b" in incoming_msg) or "Bangalore b" in incoming_msg:
                text="""For OXYGEN Beds:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Hospital%20Beds&widgetId=608c1c70fce18a42ebf89406 \n
                For ICU Beds:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Hospital%20Beds&widgetId=608c1c79fce18a42ebf89724 \n
                For Ventilator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Hospital%20Beds&widgetId=608c1c85fce18a42ebf89c29 \n
                For Home Ventilator: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Hospital%20Beds&widgetId=608c1c8ffce18a42ebf89eee
                """
            if "bangalore c" in incoming_msg or "Bangalore c" in incoming_msg:
                text="""For OXYGEN Cylinder: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Oxygen%20Supplies&widgetId=608c1c44fce18a42ebf88311 \n
                For OXYGEN Regulator:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Oxygen%20Supplies&widgetId=608c1c57fce18a42ebf88a4c \n
                For OXYGEN Concentrator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Oxygen%20Supplies&widgetId=608c1c61fce18a42ebf88e95 \n
                For Oximeter:https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Oxygen%20Supplies&widgetId=608c1cc0fce18a42ebf8b28d
                """
            if "bangalore d" in incoming_msg or "Bangalore d" in incoming_msg:
                text="""For PLASMA:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Plasma&widgetId=608c1c98fce18a42ebf8a304  \n
                    """
            if "bangalore e" in incoming_msg or "Bangalore e" in incoming_msg:ttps://external.sprink
                text="""For Govenment Links:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Others&widgetId=60896a5ad5ecb727f9d97186 \n
                For Food:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Others&widgetId=608c1ca1fce18a42ebf8a67a  \n
                For Provide Help: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Others&widgetId=608c1cacfce18a42ebf8aa78  \n
                For Ambulance: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/4?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=4%244_Others&widgetId=608c1cb5fce18a42ebf8ade7
                """





            if "indore a" in incoming_msg or "Indore a" in incoming_msg:
                text="""For Remdesivir:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Medicines%20and%20Injections&widgetId=608c470c011fb174c4e7f1e9 \n
                For Tocilzumab: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Medicines%20and%20Injections&widgetId=608c470c011fb174c4e7f1eb \n
                For Fabiflu: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Medicines%20and%20Injections&widgetId=608c470c011fb174c4e7f1ed \n
                For Favipiravir:https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Medicines%20and%20Injections&widgetId=608c470c011fb174c4e7f1ef
                """
            if ("indore b" in incoming_msg) or "Indore b" in incoming_msg:
                text="""For OXYGEN Beds:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Hospital%20Beds&widgetId=608c470c011fb174c4e7f1f7 \n
                For ICU Beds:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Hospital%20Beds&widgetId=608c470c011fb174c4e7f1f9 \n
                For Ventilator:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Hospital%20Beds&widgetId=608c470c011fb174c4e7f1fb \n
                For Home Ventilator: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Hospital%20Beds&widgetId=608c470c011fb174c4e7f1fe
                """
            if "indore c" in incoming_msg or "Indore c" in incoming_msg:
                text="""For OXYGEN Cylinder: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Oxygen%20Supplies&widgetId=608c470c011fb174c4e7f1f1 \n
                For OXYGEN Regulator:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Oxygen%20Supplies&widgetId=608c470c011fb174c4e7f1f3 \n
                For OXYGEN Concentrator:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Oxygen%20Supplies&widgetId=608c470c011fb174c4e7f1f5 \n
                For Oximeter:https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Oxygen%20Supplies&widgetId==608c470c011fb174c4e7f20b
                """
            if "indore d" in incoming_msg or "Indore d" in incoming_msg:
                text="""For PLASMA:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Plasma&widgetId=608c470c011fb174c4e7f203  \n
                    """
            if "indore e" in incoming_msg or "Indore e" in incoming_msg:ttps://external.sprink
                text="""For Govenment Links:   https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Others&widgetId=608c470c011fb174c4e7f1e7 \n
                For Food:  https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Others&widgetId=608c470c011fb174c4e7f205  \n
                For Provide Help: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Others&widgetId=608c470c011fb174c4e7f207  \n
                For Ambulance: https://external.sprinklr.com/insights/explorer/dashboard/601b9e214c7a6b689d76f493/tab/14?id=DASHBOARD_601b9e214c7a6b689d76f493&tabId=14%2414_Others&widgetId=608c470c011fb174c4e7f209
                """

                
    
                                                                  


    except Exception as err:
        print("",err)      
        text="Currently faceing issue ,Please try again later!"
    finally:
        return text
        print("msg",text)

def new_member_greet(dict):
    text=""
    #new_member_dict={'update_id':update_id,'chat_id':chat_id,'chat_first_name':None,'new_member_chat_id':member_chat_id,'member_is_bot':member_is_bot,'member_name':member_name,'chat_type':chat_type,'date':date_time}
    try:
        message_from=dict.get('member_name')
        chat_first_name=dict.get('chat_first_name')
        text=f'''Welcome {message_from} !!\nThanks for joining "{chat_first_name}" Telegram Group!!'''
    except Exception as err:
        print(err)
    finally:
        return text
    

# def chat_forward_msg(dict,dbname,inv_tablename):
#     try:
#         chat_type=dict.get('chat_type')
#         chat_id_support=""
#         custom_forward_msg=""
#         if (chat_type=='group' or chat_type=='supergroup') :
#             message_from=dict.get('message_from_first_name')
#             cust_incoming_msg=dict.get('text')
#             chat_first_name=dict.get('chat_first_name')
#             custom_forward_msg=f"Hi,You have new request from {message_from} in {chat_first_name}!\n Customer message is:\n\n{cust_incoming_msg}."
#             if "#support" in cust_incoming_msg and len(cust_incoming_msg)>12:
#                 inv_dict=get_support_member_details(dbname,inv_tablename,'#support',chat_first_name)
#                 print(inv_dict)
#                 chat_id_support=inv_dict.get('chat_id')
#                 # chat_id_support="1285170009"
#                 # return custom_forward_msg,chat_id_support
#             if "#requirenment" in cust_incoming_msg and len(cust_incoming_msg)>15:
#                 inv_dict=get_support_member_details(dbname,inv_tablename,'#requirenment',chat_first_name)
#                 chat_id_support=inv_dict.get('chat_id')
#                 # chat_id_support="1285170009"
#                 # return custom_forward_msg,chat_id_support
#             if "#complaint" in cust_incoming_msg and len(cust_incoming_msg)>12:
#                 inv_dict=get_support_member_details(dbname,inv_tablename,'#complaint',chat_first_name)
#                 chat_id_support=inv_dict.get('chat_id')
#                 # chat_id_support="1285170009"
#                 # return custom_forward_msg,chat_id_support
#     except Exception as err:
#         print(err)
#     finally:
#         return custom_forward_msg,chat_id_support

        
def chat_reply_handler(update_dict):
    reply_msg=""
    try:
        if 'new_member_chat_id' in update_dict:
            reply_msg=new_member_greet(update_dict)
        else:
            reply_msg=bot_reply(update_dict)
            print(reply_msg)
    except Exception as err:
        print(err)
    finally:
        return reply_msg




"""

def chat_reply_handler(update_dict):
    reply_msg=""
    text=update_dict.get('text')
    try:
        if 'new_member_chat_id' in update_dict:
            reply_msg=new_member_greet(update_dict)
        
        if "#b" in text:
            reply_msg=text
        else:
            reply_msg=bot_reply(update_dict)
            print(reply_msg)
    except Exception as err:
        print(err)
    finally:
        return reply_msg

"""



def main():
    chat_reply_handler(update_dict)

if __name__ == "__main__":
    main()
    
    
    





            # if ('quote' in incoming_msg) or ('Quote' in incoming_msg):
            #     # return a quote
            #     r = requests.get('https://api.quotable.io/random')
            #     if r.status_code == 200:
            #         data = r.json()
            #         text = f'{data["content"]} ({data["author"]})'
            #     else:
            #         text = 'I could not retrieve a quote at this time, sorry.'
 
            # if ('joke' in incoming_msg) or ('jokes' in incoming_msg):
            #     # return a quote
            #     r = requests.get("https://indian-jokes-api.herokuapp.com/jokes/random")
            #     #print(r)
            #     if r.status_code == 200:
            #         data = r.json()
            #         #print(data)
            #         text = f'({data["text"]})'
            #     else:
            #         text = 'I could not retrieve a quote at this time, sorry.'   


