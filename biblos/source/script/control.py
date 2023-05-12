from menu import Menu
from DAO import DB
import process
import graph


#クラスのオブジェクト化
menu = Menu()
db = DB()

#ログインメニュー　竹内　20230314
li_pass = db.sel_query("admin_id,admin_pass,login_flag,perm_flag", "admin")


# 鈴木 2023/03/22
# ログイン時、重複コントロール
while True:
    try:
        u_id, u_pas = menu.id_input()
        login_check = process.login_situation_check()
        if login_check == False:
            continue
        else:
            db.login_flag_chenge(u_id)
        s_next01, user_no = process.id_login(li_pass, u_id, u_pas)
    except Exception:
        print('有効な文字を入力してください。')
    else:
        if s_next01 == 'next':
            break
        else:
            continue


#管理者メインメニュー
if user_no == 1:
    while True:
        admin_menu = menu.admin_menu()
        if admin_menu == '1':
            while True:
                admin_menu_book = menu.admin_menu_book()
                if admin_menu_book == '1':
                    st_search_word = menu.search_word()
                    li_all_book = db.sel_book_where_query(st_search_word)
                    li_rental = db.sel_query("*", "rental")
                    process.indicate_table(li_all_book, li_rental)
                #　記入　貸出、返却処理 2023.03.23 伊藤
                    if len(li_all_book)!=0:
                        while True:
                            select_user_input = menu.book_list_rent_menu()
                            if select_user_input == "1":
                                process.rental_control(db)
                                break
                            elif select_user_input == "2":
                                process.return_control(db)
                                break
                            elif select_user_input == "9":
                                # process.sarvice_fin()
                                break
                            else:
                                continue
                    
                ######
                    continue
                if admin_menu_book == '2':
                    li_book = db.sel_query("*", "book")
                    li_rental = db.sel_query("*", "rental")
                    process.indicate_table(li_book, li_rental)

                #　記入　貸出、返却処理 2023.03.22 伊藤
                    while True:
                        select_user_input = menu.book_list_rent_menu()
                        if select_user_input == "1":
                            process.rental_control(db)
                            break
                        elif select_user_input == "2":
                            process.return_control(db)
                            break
                        elif select_user_input == "9":
                            # process.sarvice_fin()
                            break
                        else:
                            continue
                ######
                



                elif admin_menu_book == '3':
                    process.rental_control(db)
                elif admin_menu_book == '4':
                    process.return_control(db)
                elif admin_menu_book == '5':                
                    process.book_ent(db)
                elif admin_menu_book == '6':
                    ob_book_del_id = process.book_del(db)
                elif admin_menu_book == '7':
                    db.csv_out('book')
                elif admin_menu_book == '9':
                    # process.sarvice_fin()
                    break
        elif admin_menu == '2':
            while True:
                user_menu = menu.user_menu()
                if user_menu == '1':
                    st_search_word = menu.search_word()
                    li_all_user = db.sel_user_where_query(st_search_word)
                    li_rental = db.sel_query("*", "rental")
                    # process.indicate_table01(li_all_user)
                    process.indicate_table_user(li_all_user,li_rental)
                    continue
                elif user_menu == '2':
                    li_user = db.sel_query("*", "user")
                    li_rental = db.sel_query("*", "rental")
                    # process.indicate_table01(li_user)
                    process.indicate_table_user(li_user,li_rental)
                elif user_menu == '3':
                    process.user_ent(db)
                elif user_menu == '4':
                    process.user_del(db)
                elif user_menu == '5':
                    db.csv_out('user')
                elif user_menu == '9':
                    # process.sarvice_fin()
                    break
        elif admin_menu == '3':
            while True:
                graph_menu = menu.graph_menu()
                match graph_menu:
                    case "1":
                        graph.show_bar_graph(db)
                    case "2":
                        yr = menu.input_year()
                        try:
                            yr = int(yr)
                        except Exception:
                            menu.default_error()
                        else:
                            graph.show_line_graph(db,yr)
                    case "3":
                        graph.show_pie_chart(db)
                    case "9":
                        break    
        elif admin_menu == '9':
            process.sarvice_fin()
            break



#一般メインメニュー
elif user_no == 0:
    while True:
        general_staff_select = menu.general_staff_menu()
        if general_staff_select == '1':
            st_search_word = menu.search_word()
            li_all_book = db.sel_book_where_query(st_search_word)
            li_rental = db.sel_query("*", "rental")
            process.indicate_table(li_all_book, li_rental)
            while True:
                select_user_input = menu.book_list_rent_menu()
                if select_user_input == "1":
                    process.rental_control(db)
                    break
                elif select_user_input == "2":
                    process.return_control(db)
                    break
                elif select_user_input == "9":
                    process.sarvice_fin()
                    break
                else:
                    continue
        if general_staff_select == '2':
            li_book = db.sel_query("*", "book")
            li_rental = db.sel_query("*", "rental")
            process.indicate_table(li_book, li_rental)
            while True:
                select_user_input = menu.book_list_rent_menu()
                if select_user_input == "1":
                    process.rental_control(db)
                    break
                elif select_user_input == "2":
                    process.return_control(db)
                    break
                elif select_user_input == "9":
                    process.sarvice_fin()
                    break
                else:
                    continue
        elif general_staff_select == '3':
            process.rental_control(db)
        elif general_staff_select == '4':
            process.return_control(db)
        elif general_staff_select == '9':
            process.sarvice_fin()
            break

def exit_logout_call():
    db.login_flag_out()