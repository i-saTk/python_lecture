import requests
import datetime
import mysql.connector as mydb
import json
import time
from tkinter import filedialog


# コネクションの作成
conn = mydb.connect(
    host="localhost",
    port="3306",
    user="user",
    password="pass",
    database="books"
)

cur = conn.cursor()

cur.execute("select book_id,isbn, book_name from book")
list_temp = cur.fetchall()

list_test = []
number=list_temp[-1][0]
# query_list = ["ドラえもん","電気","トラック","犬","猫","ひまわり","インドネシア","交通事故","就活","一億円","お墓","誕生日","セガ","メタル"]
query_list = []

while True:
    user_input = input("1)検索ワード入力\t2)外部ファイルから検索ワードを読み込む\t9)終了")
    match user_input:
        case "1":
            while True:
                user_input = input("検索したい言葉を入力してください。(ENDで終了)")
                if user_input == "END":
                    break
                query_list.append(user_input)
            break
        case "2":
            queries_temp =[] 
            typ = [('テキストファイル','*.txt')] 
            dir = './'
            fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 
            with open(fle,mode="r",encoding="utf-8") as f:
                queries_temp = f.readlines()
            if len(queries_temp) > 0:
                query_list = queries_temp
                break
            else:
                print("エラーが発生しました")
        case "9":
            quit()
        case _:
            pass

json_dump = []

# ISBN 取得(GoogleAPI)
isbn_list = []
# index_num = 0
for query in query_list:

    # url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=40&startIndex=0' #GooglBooksAPI
    # response = requests.get(url).json() #情報の取得,json変換
    # total_items = response['totalItems']
    # time.sleep(1)

    for index_no in range(2):
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=40&startIndex={index_no}' #GooglBooksAPI
        response = requests.get(url).json() #情報の取得,json変換
        items_list = response['items'] #items リストデータ
        items = items_list[0] #items
        # info = items['volumeInfo']
        for item in items_list:
        # print(item)
            temp = []
            info = item["volumeInfo"]
        # print(info)
        # print()
            try:
                identifiers = info['industryIdentifiers']
            except Exception:
                pass
            try:    
                if identifiers[1]['type'] == 'ISBN_13':
                    isbn_list.append(identifiers[1]['identifier'])
                else:
                    raise Exception
            except Exception:
                try:
                    if identifiers[0]['type'] == 'ISBN_13':
                        isbn_list.append(identifiers[0]['identifier'])
                    else:
                        raise Exception
                except Exception:
                    pass
        # index_num += 1
        time.sleep(1)

# OpenBD API で　書籍情報取得
for isbn_code in isbn_list:
    url = f'https://api.openbd.jp/v1/get?isbn={isbn_code}' #GooglBooksAPI

    response = requests.get(url).json() #情報の取得,json変換
    try:
        items_list = response[0]
        summary = items_list["summary"]
        # info = items['volumeInfo']
        json_dump.append(items_list)

        title = summary['title']
        title = title[:40]
        publisher = summary['publisher']
        publisher = publisher[:30]

        pubdate_temp = summary['pubdate']
        if len(summary['pubdate'])<6:
            if len(summary['pubdate'])<4:
                pubdate_temp += "0101"
            else:
                pubdate_temp += "01"
        publisheddate = datetime.datetime.strptime(summary['pubdate'], '%Y%m%d')
        publisheddate = publisheddate.strftime('%Y-%m-%d')
        # publisheddate = ''
        # for i, j in enumerate(summary['pubdate']):
        #     match i:
        #         case 6:
        #             publisheddate +="-" 
        #         case 4:
        #             publisheddate +="-"

        #     publisheddate += j
        isbn = summary['isbn']
        number += 1
        temp = [number,title,publisher, publisheddate,1,isbn]
        list_test.append(temp)
    except Exception:
        pass
    # time.sleep(0.2)

# ISBNと図書名かぶってる奴は追加しない処理
list_book_infos = []
for i in list_test:
    flag = 0
    for j in list_temp:
        # print(j[1])
        # print(i[5])
        if i[5] == j[1]:  
            flag += 1 
        elif i[1] == j[2]:
            flag += 1
    if flag == 0:
        list_book_infos.append(i)

# print(list_test)
text_sql = ""

text_sql += """INSERT INTO \n
 book\n
VALUES \n"""
for index1, i in enumerate(list_book_infos):
    text_sql += " ("
    for index2, j in enumerate(i):
        j = str(j)
        j = j.replace("'","")
        j = j.replace('"',"")
        text_sql += f"'{j}'"
        if index2 == (len(i)-1):
            pass
        else:
            text_sql += ","
    text_sql += ")"
    if index1 == (len(list_book_infos)-1):
        text_sql += "\n"
    else:
        text_sql += ",\n"

text_sql += ";\n"
# UNLOCK TABLES;\n"""

while 1:
    user_input = input("1)ファイル出力\t2)データベース書き込み\t9)終了")
    match user_input:
        case "1":
            with open(f"jsondump.txt", mode="w",encoding="utf-8") as f:
                json.dump(json_dump, f, indent=4, ensure_ascii=False)
                f.flush()
            text_sql = "LOCK TABLES book WRITE;\n"+ text_sql + "UNLOCK TABLES;\n"
            name_file = "books_SQL_"+datetime.datetime.now().strftime('%Y-%m-%d-%H%M')
            with open(f"{name_file}.sql", mode="w",encoding="utf-8") as f:
                f.writelines(text_sql)
                f.flush()
            print("書き出し終了")
        case "2":
            try:
                cur.execute(text_sql)
                conn.commit()
                print("登録完了")
            except Exception as err:
                print(err)
                conn.rollback()
                print("エラーが発生しました。ロールバックします。")
            break
        case "9":
            break
        case _:
            pass


# カーソルの切断
cur.close()

# コネクションの切断
conn.close()