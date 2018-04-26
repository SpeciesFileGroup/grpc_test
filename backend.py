import psycopg2
from pprint import pprint

class ConnectDB(object):
    def __init__(self, number_of_pages):
        self.number_of_pages = number_of_pages

    def connect(self):
        try:
            conn = psycopg2.connect(database="bhlindex", user="bhl", password="grpc2BHL", host="172.22.247.14", port ="5432")
        except:
            print("Unable to connect to db")

        return conn

    def get_data(self):
        conn = self.connect()
        cur = conn.cursor()
        query = "SELECT * from dev_page_name_counts LIMIT {}".format((str(self.number_of_pages)))
        cur.execute(query)

        rows = cur.fetchall()
        return rows
