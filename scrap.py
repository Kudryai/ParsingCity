import pymysql
import os
from scrabyDo import ScrapyDo
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class FinancialTruthData:

    def connect_db(self):
        self.conn = pymysql.connect(host='127.0.0.1',
        unix_socket='/var/run/mysqld/mysqld.sock',
        user='root',
        passwd=os.getenv('bdpsw'), db='mysql', charset='utf8')
        self.cur = self.conn.cursor()

    def append_new_data(self,data):
        for value in data:
            self.stocks_update(value[0],value[3],value[4],value[5],value[6])
        self.cur.close()
        self.conn.close()


    def stocks_update(self,id, w_indx, price, yty, div):
        self.cur.execute('USE fintruth')
        self.cur.execute(f"UPDATE stocks_stocks SET weight_to_index = {w_indx}, price = {price}, proffit_52 = {yty}, dividend = {div} WHERE id = {id}")    
        self.conn.commit()

db = FinancialTruthData()
db.connect_db()
db.append_new_data(ScrapyDo.MOEX())

