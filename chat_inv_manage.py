import json
import requests
import time
import urllib
from sqlalchemy import create_engine
import pandas as pd

def db_connection(dbname):
    try:
        engine = create_engine(f"mysql+pymysql://@localhost/{dbname}")
        db_conn = engine.connect()
    except Exception as err:
        print(err)
        db_conn=False
    finally:
        return db_conn

def chat_to_db(dict,dbname,tablename):
    try:
        dict_df=pd.DataFrame([dict])
        con=db_connection(dbname)
        if con!=False:
            dict_df.to_sql(con=con, name=tablename, if_exists='append',index = False)
            #print("Appended to db!!!")
    except Exception as err:
        print("--- chat_to_db function implementation failed --- ",err)


def df_return_table(dbname,tablename):
    print(dbname,tablename)
    try:
        con=db_connection(dbname)
        df = pd.read_sql_query(f"select * from {tablename}", con)
        print(df)
        return df
    except Exception as err:
        print(err)

def get_support_member_details(dbname,tablename,tag,group_name):

    try:
        df=df_return_table(dbname,tablename)
        df1=df.loc[((df['allocation_tag'] == tag) & (df['group'] == group_name))]
        print(df1)
        for row_dict in df1.to_dict(orient="row"):
            #print(row_dict)
            return row_dict

    except Exception as err:
        print(err)


def flatten_dict(dd, separator ='_', prefix =''): 
    return { prefix + separator + k if prefix else k : v 
             for kk, vv in dd.items() 
             for k, v in flatten_dict(vv, separator, kk).items() 
             } if isinstance(dd, dict) else { prefix : dd } 

def main():   
    chat_to_db(dict,dbname,tablename)    
    get_memebr_details(dbname,tablename,tag,group_name)

if __name__ == '__main__':
    main()
