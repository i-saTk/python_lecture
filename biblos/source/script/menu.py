import color_word as cw

class Menu(object):

    def __init__(self) -> None:
        pass

     # ログイン時メニュー
    def id_input(self):
        try:
            adminID = int(cw.i_message("IDを入力してください: "))
            adminPASS = cw.i_message("PASSを入力してください: ")
            return adminID, adminPASS     
        except Exception:
            cw.p_error_message('入力が適切ではありません。')



    #管理者メニュー
    def admin_menu(self):
        admin_select = cw.i_menu_message('1：書籍\t\t2：利用者\t3：グラフ表示\t9：終了\n>>> ')
        return admin_select

    #管理者メニュー
    def admin_menu_book(self):
        admin_book_select = cw.i_menu_message('1：本の検索\t2：本の一覧\t3：本の貸出\t4：本の返却\t5：本の登録\t6：本の削除\n7：CSV書き出し9：終了\n>>> ')
        return admin_book_select

    # 各変数に登録情報を代入
    def book_register_menu(self):
        s_book_id = cw.i_message("図書ID >>> ")
        s_book_name = cw.i_message("図書名 >>> ")
        s_publish = cw.i_message("出版社 >>> ")
        s_date = cw.i_message("出版日 >>> ")
        t_data = (s_book_id,s_book_name,s_publish,s_date,"1")
        return t_data

    #検索
    def search_word(self):
        try:
            search_key = cw.i_message("検索文字を入力してください>>> ")
            return search_key
        except Exception:
            cw.p_error_message('入力が適切ではありません。')


    #利用者メニュー
    def user_menu(self):
        user_menu_select = cw.i_menu_message('1：利用者検索\t2：利用者一覧\t3：利用者登録\t4：利用者削除\t5：CSV書き出し\t9：終了\n>>> ')
        return user_menu_select


    #一般職員メニュー
    def general_staff_menu(self):
        general_staff_select = cw.i_menu_message('1：本の検索\t2：本の一覧\t3：本の貸出\t4：本の返却\t9：終了\n>>> ')
        return general_staff_select
    
    def book_list_rent_menu(self):
        book_list_rent_select = cw.i_menu_message("1:貸出\t2:返却\t\t9:終了\n>>> ")
        return book_list_rent_select
    
    def graph_menu(self):
        graph_menu_view = cw.i_menu_message("1:貸出ランキング\t2:年間貸出情報\t3:出版社TOP10\t9:終了\n>>> ")
        return graph_menu_view
    
    def input_year(self):
        year = cw.i_message("調べたい年を入力してください。")
        return year
    
    def default_error(self):
        return cw.p_error_message("エラーが発生しました。")