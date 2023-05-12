from DAO import DB
# from menu import Menu
from datetime import datetime, timedelta, date
import pandas as pd
import color_word as cw

pd.set_option('display.max_columns', 100)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_rows', 150)

db = DB()

# ログイン確認　2023.03.14 伊藤
def id_login(li_pass, u_id, u_pas):
    for i in range(len(li_pass)):
        if li_pass[i][0] == u_id:
            if li_pass[i][1]  == u_pas:
                print("ログインしました。")
                return 'next', li_pass[i][3]
            else:
                cw.p_error_message("ログイン ID またはパスワードが違います。")
                break
    else:
        cw.p_error_message("ログイン ID またはパスワードが違います。")




# 鈴木 20230322
# ログイン時、多重ログインチェック
def login_situation_check():
    admin_check = db.sel_query("*","admin")
    for i in range(len(admin_check)):
        if admin_check [i][2] == 1:
            cw.p_error_message("ほかの人がログイン中のため、入れません。")
            return False
    else:
        return True

# テーブル内容表示
def indicate_table(li_book, li_rental):
    try:
        li_bo = li_book
        li_re = li_rental
        li_bo2 = []
        li_bo3 = []

    #    for i2 in range(len(li_bo)):
    #        li_bo2.append(list(li_bo[i2]))
    #    for i in range(len(li_bo2)):
    #        if li_bo2[i][4] != 0:
    #            li_bo3.append(li_bo2[i])

    #    for i in range(len(li_bo3)):
    #        for i3 in range(len(li_re)):
    #            if li_re[i3][0] == li_bo3[i][0]:
    #                del li_bo3[i][4]
    #                li_bo3[i].append('貸出中')
    #            else:
    #                del li_bo3[i][4]
    #                li_bo3[i].append('貸出可能')

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
        li_bo3 = pd.DataFrame(li_bo3)
        li_colmuns_names = ["図書ID","図書名","出版社","出版日","ISBN","貸出可不可"]
        li_bo3.columns = li_colmuns_names
        print(li_bo3.to_string(index=False, max_colwidth=30, justify="left"))
    except Exception:
        cw.p_error_message('内容が見つかりません')


def indicate_table_user(li_users,li_rental):
    try:
        li_users2 =[]

        for i in li_users:
            temp = []
            for index, j in enumerate(i):
                if index == 2:
                    break
                temp.append(j)
            li_users2.append(temp)
        for index1, i in enumerate(li_users2):
            count = 0
            for index2, j in enumerate(li_rental):
                if i[0]==j[1]:
                    if j[2] ==1:
                        count += 1
            li_users2[index1].append(count)

        dt_users = pd.DataFrame(li_users2)
        li_colmuns_names = ["ユーザーID","ユーザー名","貸出冊数"]
        dt_users.columns = li_colmuns_names
        print(dt_users.to_string(index=False, max_colwidth=30, justify="left"))
    except Exception:
        cw.p_error_message('内容が見つかりません')

def indicate_table01(li_bo):
    for row in li_bo:
        print(row)

################　本の削除　20230315　川村　################
# 更新者：出田　20230316
def book_del(dao):
    # 削除する情報を図書IDを基に呼び出す
    t_delete = cw.i_message("削除する図書を指定して下さい"),
    t_book_info = dao.sel_query("*","book","book_id",t_delete[0])
    for i in t_book_info:
        print(i,"",end="")
    print()
    s_input = cw.i_menu_message("1：削除\t2：キャンセル >>>")
    if s_input != "1":
        return
    if True == dao.is_rented(t_delete[0]):
        return cw.p_error_message("貸出中の図書を削除できません。")
    try:
        dao.book_del_commit(t_delete)
    except Exception:
        print("エラーが発生しました。")
        return
    print("削除しました。")

################　本の登録　20230315　川村　################
def book_ent(dao):
    # 各変数に登録情報を代入
    s_book_id = str(dao.id_gen("book")+1)
    s_book_name = cw.i_message("図書名 >> ")
    if len(s_book_name) > 40:
        return cw.p_error_message("図書名の長さが最大値を超えています。")
    s_publish = cw.i_message("出版社 >> ")
    s_date = cw.i_message("出版日 >> ")
    s_isbn = cw.i_message("ISBN >> ")
    t_book_info =(s_book_id,s_book_name,s_publish,s_date,"1",s_isbn)
    for i in t_book_info:
        print(i,"",end="")
    print()
    s_input = cw.i_menu_message("1：登録\t2：キャンセル >>>")
    if s_input != "1":
        return
    try:
        dao.book_ent_commit(t_book_info)
    except Exception:
        print("エラーが発生しました。")
        return
    print("登録しました。")


################　利用者の削除　20230315　川村　################
def user_del(dao):
    # 削除する情報をユーザーIDを基に呼び出す
    t_delete = cw.i_message("削除するユーザーのIDを指定して下さい"),
    t_user_info = dao.sel_query("*","user","user_id",t_delete[0])
    for i in t_user_info:
        print(i,"",end="")
    print()
    s_input = cw.i_menu_message("1：削除\t2：キャンセル >>>")
    if s_input != "1":
        return
    t_row = dao.sel_query("*", "rental", "user_id", f"{t_delete[0]} and rental_flag = 1")
    if len(t_row) > 0:
        return cw.p_error_message("図書借用中の利用者を削除できません。")
    try:
        dao.user_del_commit(t_delete)
    except Exception:
        print("エラーが発生しました。")
        return
    
    print(f"利用者：{t_user_info[0][1]}を削除しました。")
    

################　利用者の登録　20230315　川村　################
def user_ent(dao):
    # 各変数に登録情報を代入
    # s_user_id = input("ユーザーID >> ")
    s_user_id = str(dao.id_gen("user")+1)
    s_user_name = cw.i_message("ユーザー名 >> ")
    if len(s_user_name) > 20:
        return cw.p_error_message("利用者名の長さが最大値を超えています。")
    t_user_info =(s_user_id,s_user_name,"1")
    for i in t_user_info:
        print(i,"",end="")
    print()
    s_input = cw.i_menu_message("1：利用者登録\t2：キャンセル >>>")
    if s_input != "1":
         return
    try:
        dao.user_ent_commit(t_user_info)
    except Exception:
        print("エラーが発生しました。")
        return 
    print("登録しました。")


################　本の貸出　################
    # 出田　2023/03/15　貸出処理-DAOに引き渡すためのメソッド
    # 引数は仮引数とテーブルの物理名が合致する物を渡してください。
def rental_format(book_id:str,user_id:str):
    s_book_id = book_id
    s_user_id = user_id
    #貸出フラグ
    i_flag = 1 
    #貸出日は今日の日付
    s_rent_date = datetime.now() 
    #今日の日付の５日後
    s_return_date = s_rent_date + timedelta(days=5) 
    #10文字制限に収まるようにフォーマット
    s_rent_date,s_return_date = s_rent_date.strftime('%Y/%m/%d'), \
        s_return_date.strftime('%Y/%m/%d') 
    #executeするためにタプル化
    t_data =(s_book_id,s_user_id,i_flag,s_rent_date,s_return_date)
    return t_data

#製作： 出田　2023/03/15　貸出処理
# 更新：出田　2023/03/16 try, except文追加
# インスタンス化したclass DBを引数として渡してください。
def rental_control(dao, book_id=""):
    try:
        if book_id =="":
            s_book_id = int(cw.i_message("図書 IDを入力してください。>>>"))
            if False == dao.it_exist("*","book","book_id",s_book_id):
                return cw.p_error_message("不正な図書 ID が入力されました。")
            if True == dao.is_rented(s_book_id):
                return cw.p_error_message("図書はすでに貸出中です。")
        else:
            s_book_id = book_id
        s_user_id = int(cw.i_message("利用者IDを入力してください。>>>"))
        if False == dao.it_exist("*","user","user_id",s_user_id):
            return cw.p_error_message("不正な利用者 ID が入力されました。")
        if True == dao.rent_count(s_user_id):
            return cw.p_error_message("利用者はすでに 3 冊の図書を借りています。")
        t_row = dao.sel_query("*","user","user_id",s_user_id)
        # rent_cnt = dao.rent_count_number(s_user_id)
        if t_row[0][2] == 0:
            return cw.p_error_message("利用者は削除されてます。")
        dao.rent_commit(rental_format(s_book_id, s_user_id))
    except Exception:
        return print("エラーが発生しました")
    t_user_book = dao.fetch_user_book2(s_book_id)
    rent_cnt = dao.rent_count_number(s_user_id)

    for i in t_user_book[:4]:
        print(i,"",end="")
    print(f"{rent_cnt}冊貸出中")
    # print()
    print("貸出しました。")


################　本の返却　################
# 出田　2023/03/15　返却処理-DAOに引き渡すためのメソッド
# 引数は仮引数とテーブルの物理名が合致する物を渡してください。
def return_format(book_id:str,user_id:str):
    s_book_id = book_id
    s_user_id = user_id
    #貸出フラグ初期化
    i_flag = 0
    t_data =(i_flag, s_book_id,s_user_id) 
    return t_data

#製作： 出田　2023/03/16　返却処理
# インスタンス化したclass DBを引数として渡してください。
def return_control(dao, book_id=""):
    try:
        if book_id == "":
            s_book_id = int(cw.i_message("図書 IDを入力してください。>>>"))
            if False == dao.it_exist("*","book","book_id",s_book_id):
                return cw.p_error_message("不正な図書 ID が入力されました。")
        else:
            s_book_id = book_id
        if False == dao.is_rented(s_book_id):
            return cw.p_error_message("図書は貸出されていません。")
        t_user_book = dao.fetch_user_book2(s_book_id)
        # print(t_user_book)
        rent_cnt = dao.rent_count_number(t_user_book[5])
        for i in t_user_book[:4]:
            print(i,"",end="")
        print(f"{rent_cnt}冊貸出中")
        s_input = cw.i_menu_message("1：返却登録\t2：キャンセル >>>")
        if s_input != "1":
            return
        dao.return_commit(return_format(t_user_book[4], t_user_book[5]))
        # dao.return_commit(return_format(t_user_book[0], t_user_book[1]))
    except Exception:
        return print("エラーが発生しました")
    print(f"図書：{t_user_book[0]}を返却しました。")

# サービス終了
def sarvice_fin():
    print('サービスを終了します')
# 鈴木2023/03/22
# ログアウト時、ログアウトフラグ生成
    db.login_flag_out()