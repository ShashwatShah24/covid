import pandas as pd
from sqlalchemy import create_engine

def db_connection(dbname):
    try:
        engine = create_engine(f"mysql+pymysql://@localhost/{dbname}")
        db_conn = engine.connect()
    except Exception as err:
        print(err)
        db_conn=False
    finally:
        return db_conn

def inv_to_db(dbname,tablename):
    try:
        dict_df = pd.read_csv("",encoding="iso-8859-1")
        con=db_connection(dbname)
        if con!=False:
            dict_df.to_sql(con=con, name=tablename, if_exists='replace',index = False)
            print("Appended to db!!!")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    inv_to_db("telegram_db","testing_chat_bot_support_inv")
    # "airtel_care_bot_support_inv