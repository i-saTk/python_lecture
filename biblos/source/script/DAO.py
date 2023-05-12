import mysql.connector as mydb
import datetime
import color_word as cw
import configparser
from os import getcwd


class DB(object):

    # 製作者：出田(2023/3/14)----------------------
    def __init__(self):
        path = getcwd()
        config_ini = configparser.ConfigParser()
        config_ini.read(f'{path}\\config\\config.ini', encoding='utf-8')
        host = config_ini['MySQLConnection']['host']
        port = config_ini['MySQLConnection']['port']
        user = config_ini['MySQLConnection']['user']
        password = config_ini['MySQLConnection']['password']
        database = config_ini['MySQLConnection']['database']
    # コネクションの作成
        self.__connect = mydb.connect(
            host = str(host),
            port = str(port),
            user = str(user),
            password= str(password),
            database= str(database)
        )
        # self.cursor = self.__connect.cursor(buffered=True)
    
    # 製作者：出田(2023/3/14)----------------------
    # 接続が切れないようにこのメソッドを呼んでください
    def ping(self):
        return self.__connect.ping(reconnect=True)
    
    # 製作者：出田(2023/3/15)----------------------
    # 列、テーブルを引数で渡し、射影した結果を戻り値として返す関数
    # SELECT文
    def sel_query(self, row:str, table:str, where_row="",where_pattern=""):
        self.cursor_create()
        try:
            t_data = (row,table,where_row, where_pattern)
            if where_row != "":
                query = f"select {row} from {table}\
                    where {where_row} = {where_pattern}"
            else:
                query =  f"select {row} from {table}"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.cursor.close()
            return rows
        except Exception as err:
            self.cursor.close()
            print(err)

    # 製作者：竹内(2023/3/16)----------------------
    # 列、テーブルを引数で渡し、射影した結果を戻り値として返す関数
    # bookテーブル全体検索SELECT文
    def sel_book_where_query(self, where:str):
        self.cursor_create()
        try:
            query = f"select * from book where concat_ws(char(0),book_id,book_name,publish_date,delete_flag) like '%{where}%'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.cursor.close()
            return rows
        except Exception as err:
            self.cursor.close()
            print(err)

    # 製作者：竹内(2023/3/16)----------------------
    # 列、テーブルを引数で渡し、射影した結果を戻り値として返す関数
    # 利用者テーブル全体検索SELECT文
    def sel_user_where_query(self, where:str):
        self.cursor_create()
        try:
            query = f"select * from user where concat_ws(char(0),user_id, user_name, delete_flag) like '%{where}%'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.cursor.close()
            return rows
        except Exception as err:
            self.cursor.close()
            print(err)

    # 製作者：竹内(2023/3/16)----------------------
    # 列、テーブルを引数で渡し、射影した結果を戻り値として返す関数
    # 利用者テーブル全体検索SELECT文
    def sel_user_where_query(self, where:str):
        self.cursor_create()
        try:
            query = f"select * from user where concat_ws(char(0),user_id, user_name, delete_flag) like '%{where}%'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.cursor.close()
            return rows
        except Exception as err:
            self.cursor.close()
            print(err)

    # # 製作者：出田(2023/3/14)----------------------
    # # コネクションクローズ
    # def close(self):
    #     return self.__connect.close()
    
    # 製作者：出田(2023/3/15)----------------------
    # 貸出コミットメソッド。引数のタプルは(book_id, user_id, 
    # rental_flag, rental_date, return_date) の順で作ったタプルにしてください。
    # rental_formatメソッドの戻り値を引数としていれてもらえばいいです。
    def rent_commit(self,datas_tuple):
        self.cursor_create()
        try: 
            self.cursor.execute("insert into rental values(%s,%s,%s,%s,%s)", datas_tuple)
        except Exception as err:
            #問題があればコミットしない、エラーを吐かせる
            print(err)
            self.cursor.close()
            self.__connect.rollback()
            raise Exception
        self.cursor.close()
        self.__connect.commit()
        return
    
    # 製作者：出田(2023/3/15)----------------------
    # 最終変更者：出田(2023/3/16)クエリが間違ってたので修正
    # 返却コミットメソッド。引数のタプルは(rental_flag, book_id, user_id)の
    # 順で作ったタプルにしてください。return_formatメソッドの戻り値を引数
    # として入れてもらえばいいです。
    def return_commit(self,datas_tuple):
        self.cursor_create()
        try: 
            self.cursor.execute("update rental\
                       set rental_flag = %s\
                       where book_id = %s and user_id = %s", datas_tuple)
        except Exception as err:
            #問題があればコミットしない、エラーを吐かせる
            print(err)
            self.cursor.close()
            self.__connect.rollback()
            raise Exception
        self.cursor.close()
        self.__connect.commit()
        return
    
    # 製作者：出田(2023/3/15)----------------------
    # レンタル冊数が３冊以上の場合Trueを返すメソッド
    # 引数は仮引数とテーブルの物理名が合致する物を渡してください。
    def rent_count(self, user_id):
        self.cursor_create()
        t_user_id = user_id,
        try: 
            self.cursor.execute("select count(*) from rental\
                                where user_id = %s and rental_flag = 1", t_user_id)
            l_row = self.cursor.fetchone()
            self.cursor.close()
            if l_row[0] >= 3:
                # すでに3冊借りていればTrue
                return True
            else:
                return False
        except Exception as err:
            #問題があればエラーを吐かせる
            self.cursor.close()
            return print(err) 
        
    # 製作者：出田(2023/3/15)----------------------
    # レンタル冊数を返すメソッド
    # 引数は仮引数とテーブルの物理名が合致する物を渡してください。
    def rent_count_number(self, user_id):
        self.cursor_create()
        t_user_id = user_id,
        try: 
            self.cursor.execute("select count(*) from rental\
                                where user_id = %s and rental_flag = 1", t_user_id)
            l_row = self.cursor.fetchone()
            self.cursor.close()
            # print(l_row[0])
            return l_row[0]
        except Exception as err:
            #問題があればエラーを吐かせる
            self.cursor.close()
            return print(err) 
    
    # 製作者：出田(2023/3/15)----------------------
    # 貸出中かどうか確認するメソッド
    # 引数は仮引数とテーブルの物理名が合致する物を渡してください。
    def is_rented(self, book_id):
        self.cursor_create()
        t_book_id = book_id,
        try: 
            self.cursor.execute("select count(*) from rental\
                                where book_id = %s and rental_flag = 1", t_book_id)
            l_row = self.cursor.fetchone()
            self.cursor.close()
            if l_row[0] >= 1:
                # 貸出中であればTrue
                return True
            else:
                return False
        except Exception as err:
            self.cursor.close()
            #問題があればエラーを吐かせる
            return print(err) 

    # 製作者：出田(2023/3/15)----------------------
    # 存在確認メソッド
    # リストを引数で渡し、存在するか確認する。
    # 結果はTrueかFalseで返る。
    def it_exist(self, row:str, table:str, where_row="",where_pattern=""):
        rows = self.sel_query(row,table,where_row,where_pattern)
        if 0 == len(rows):
            return False
        else:
            return True
        
    # 製作者：川村(2023/3/15)----------------------
    # 最終変更者：出田(2023/3/16)、DAO側に移動、コミット処理追加
    # 図書削除フラグを０にする
    def book_del_commit(self, book_id:tuple):
        self.cursor_create()
        try:
            self.cursor.execute("UPDATE book SET delete_flag = 0 where book_id = %s",book_id)
        except Exception as err:
            print(err)
            self.cursor.close()
            self.__connect.rollback()
            raise Exception
        # 削除件数の表示
        self.cursor.close()
        self.__connect.commit()
        
    # 製作者：川村(2023/3/15)----------------------
    # 最終変更者：出田(2023/3/16)、DAO側に移動、コミット処理追加
    # 図書登録コミット
    def book_ent_commit(self, book_info:tuple):
        self.cursor_create()
        try:
            self.cursor.execute("insert into book values(%s,%s,%s,%s,%s,%s)",book_info)
        except Exception as err:
            print(err)
            self.cursor.close()
            self.__connect.rollback()
            raise Exception
        # 登録メッセージ
        self.cursor.close()
        self.__connect.commit()

        
    # 製作者：川村(2023/3/15)----------------------
    # 最終変更者：出田(2023/3/16)、DAO側に移動、コミット処理追加
    # ユーザー削除フラグを０にする
    def user_del_commit(self, user_id:tuple):
        self.cursor_create()
        try:
            self.cursor.execute("UPDATE user SET delete_flag = 0 where user_id = %s",user_id)
        except Exception as err:
            print(err)
            self.cursor.close()
            self.__connect.rollback()
            raise Exception
        # 削除件数の表示
        self.cursor.close()
        self.__connect.commit()
        
    # 製作者：川村(2023/3/15)----------------------
    # 最終変更者：出田(2023/3/16)、DAO側に移動、コミット処理追加
    # ユーザー登録コミット
    def user_ent_commit(self, user_info:tuple):
        self.cursor_create()
        try:
            self.cursor.execute("insert into user values(%s,%s,%s)",user_info)
        except Exception as err:
            print(err)
            self.cursor.close()
            self.__connect.rollback()
            raise Exception
        self.cursor.close()
        self.__connect.commit()

    # 製作者：出田(2023/3/16)----------------------
    # 図書情報、利用者情報フェッチメソッド
    def fetch_user_book(self, book_id):
        self.cursor_create()
        t_book_id = book_id,
        try: 
            self.cursor.execute("select \
                                book.book_name, user.user_name, rental_date, return_date, \
                                book.book_id, user.user_id\
                                from rental\
                                inner join book on book.book_id = rental.book_id\
                                inner join user on user.user_id = rental.user_id\
                                where rental.book_id = %s", t_book_id)
            l_row = self.cursor.fetchone()
            self.cursor.close()
            if len(l_row) >= 1:
                return l_row
            else:
                return []
        except Exception as err:
            self.cursor.close()
            #問題があればエラーを吐かせる
            return print(err) 
        
    # 製作者：出田(2023/3/22)----------------------
    # 図書情報、利用者情報フェッチメソッドその２
    # 返却時の処理に使ってます
    def fetch_user_book2(self, book_id):
        self.cursor_create()
        t_book_id = book_id,
        try: 
            self.cursor.execute("select \
                                book.book_name, user.user_name, rental_date, return_date, \
                                book.book_id, user.user_id\
                                from rental\
                                inner join book on book.book_id = rental.book_id\
                                inner join user on user.user_id = rental.user_id\
                                where rental.rental_flag = 1 and rental.book_id = %s", t_book_id)
            l_row = self.cursor.fetchone()
            self.cursor.close()
            if len(l_row) >= 1:
                return l_row
            else:
                return []
        except Exception as err:
            self.cursor.close()
            #問題があればエラーを吐かせる
            return print(err) 
        
    # 製作者：伊藤、出田(2023/03/16)---------------------
    # CSV出力(書籍、利用者兼用)
    # flag = "book"で書籍、"user"で利用者
    def csv_out(self, flag="book"):
        self.cursor_create()
        li_write = []
        li_write2 = []
        csv_name = ""
        today = datetime.datetime.now()

        def tuple_to_list(book, rental):
            li_bo = book
            li_re = rental
            li_bo2 = []
            li_bo3 = []
            for i2 in range(len(li_bo)):
                li_bo2.append(list(li_bo[i2]))
            for i in range(len(li_bo2)):
                if li_bo2[i][4] != 0:
                    li_bo3.append(li_bo2[i])

            # -------------------------------------
            # 貸出フラグが立ってるものだけ抽出
            li_temp = []
            for i in range(len(li_re)):
                if li_re[i][2] == 1:
                    li_temp.append(li_re[i])
            li_re = li_temp
            # -------------------------------------
            for i in range(len(li_bo3)):
                for i3 in range(len(li_re)):
                    if li_re[i3][0] == li_bo3[i][0]:
                        # del li_bo3[i][4]
                        if li_re[i3][2] == 1:
                            li_bo3[i].append('貸出中')
                        # del li_bo3[i][4]
            for i in range(len(li_bo3)):
                if li_bo3[i][-1] !='貸出中':
                    li_bo3[i].append('貸出可能')
            for i in range(len(li_bo3)):
                del li_bo3[i][4]
            return li_bo3

        try:
            if flag == "book":
                self.cursor.execute("select * from book")
                t_books = self.cursor.fetchall()
                self.cursor.execute("select * from rental")
                t_rentals = self.cursor.fetchall()
                t_rows = tuple_to_list(t_books,t_rentals)
                s_columns = "図書ID,図書名,出版社,出版日,ISBN,貸出可不可\n"
                li_write.append(s_columns)
                for elements in t_rows:
                    s_line = str(elements[0])+","
                    s_line += f"'{str(elements[1])}'"+","
                    s_line += f"'{str(elements[2])}'"+","
                    s_line += f"{str(elements[3])}"+","
                    s_line += f"{str(elements[4])}"+","
                    s_line += f"{str(elements[5])}"+"\n"
                    li_write.append(s_line)
                csv_name = "books" + today.strftime('%Y-%m-%d')

                self.cursor.execute("select\
                                    book.book_id, book_name, publish, \
                                    publish_date, isbn, rental.rental_date, return_date\
                                    from book\
                                    inner join rental on book.book_id = rental.book_id\
                                    where rental.rental_flag = 1")
                t_rows = self.cursor.fetchall()
                s_columns = "図書ID,図書名,出版社,出版日,ISBN,貸出日,返却日\n"
                li_write2.append(s_columns)
                for elements in t_rows:
                    s_line = str(elements[0])+","
                    s_line += f"'{str(elements[1])}'"+","
                    s_line += f"'{str(elements[2])}'"+","
                    s_line += f"{str(elements[3])}"+","
                    s_line += f"{str(elements[4])}"+","
                    s_line += f"{str(elements[5])}"+","
                    s_line += f"{str(elements[6])}"+"\n"
                    li_write2.append(s_line)    
                csv_name2 = "rented_books" + today.strftime('%Y-%m-%d')

            elif flag == "user":
                self.cursor.execute("select * from user")
                t_rows = self.cursor.fetchall()
                s_columns = "利用者ID,利用者名,削除フラグ\n"
                li_write.append(s_columns)
                for elements in t_rows:
                    s_line = str(elements[0])+","
                    s_line += f"'{str(elements[1])}'"+","
                    s_line += f"{str(elements[2])}"+"\n"
                    li_write.append(s_line)
                    csv_name = "user" + today.strftime('%Y-%m-%d')
        except Exception as err:
            self.cursor.close()
            return print(err)
        self.cursor.close()
        with open(f"{csv_name}.csv","w",encoding="cp932") as f:
            f.writelines(li_write)
            f.flush()
        if flag =="book":
            with open(f"{csv_name2}.csv","w",encoding="cp932") as f:
                f.writelines(li_write2)
                f.flush()
        return print("CSVの書き込みを完了しました。")
    
    # 製作者：出田(2023/03/16)---------------------
    # ID連番作成用 flag は "book" か "user" を指定
    def id_gen(self, flag="book"):
        self.cursor_create()
        self.cursor.execute(f"select * from {flag}\
                            order by {flag}_id desc")   
        t_last_user = self.cursor.fetchone()
        self.cursor.close()
        # print(t_last_user[0])
        return int(t_last_user[0])
    
    def connected(self):
        return self.__connect.is_connected()
    
    # 出田　2023/03/17
    # カーソル生成メソッド
    def cursor_create(self):
        self.cursor = self.__connect.cursor(buffered=True)
    

     # 鈴木　2023/03/22
     # ログイン時、使用フラグ生成メソッド
    def login_flag_chenge(self,login_user):
        self.cursor_create()
        login_confi = (1,login_user)
        self.cursor.execute("update admin set login_flag = %s where admin_id = %s",login_confi)
        self.cursor.close()
        self.__connect.commit()

     # 鈴木　2023/03/22
     # 終了時、終了フラグ生成メソッド
    def login_flag_out(self):
        self.cursor_create()      
        self.cursor.execute("update admin set login_flag = 0 ")
        self.cursor.close()
        self.__connect.commit()
    
