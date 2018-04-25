import psycopg2







def main(limit):
    print('main')
    print(limit)
    try:
        conn = psycopg2.connect(database="bhlindex", user="bhl", password="grpc2BHL", host="172.22.247.14", port ="5432")
        print "Opened database successfully"
        cur = conn.cursor()
        cur.execute("SELECT * from dev_page_name_counts LIMIT 10")
        rows = cur.fetchall()
        print(len(rows))
       	

    except:
        print "I am unable to connect to the database"



if __name__ == '__main__':
    main(100)