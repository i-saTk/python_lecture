import tkinter
from tkinter import messagebox
# from tkinter import ttk
import DAO_logreset

login_ok = False
users = []

# Tkクラス生成
login_window = tkinter.Tk()


def login_click(user_id, password):

    global login_ok
    global users
    global login_window

    def pushed():
        with DAO_logreset.DB() as db:
            cur = db.connect.cursor()
            try:
                cur.execute("update admin set login_flag = 0")
            except Exception:
                db.connect.rollback()
                messagebox.showerror("エラー","ログインフラグのリセットができません。")
            else:
                db.connect.commit()
                messagebox.showinfo("終了","ログインフラグがリセットされました。")  
        

    try:
        user_id = int(user_id)
    except Exception:
        messagebox.showerror("不正なID","不正なIDが入力されました。")  

    for user in users:
        if user[0] == user_id:
            if user[1] == password:
                if user[3] == 1:
                    login_ok = True
                    break
    
    if login_ok == True:
        login_window.destroy()
        next_frame = tkinter.Tk()
        label = tkinter.Label(next_frame,text="ログイン状態をリセットしますか？")
        label.place(x=140,y=30)
        button = tkinter.Button(next_frame,command=pushed,text="リセット")
        button.place(x=140,y=70)
        label.pack()
        button.pack()
        # 画面サイズ
        next_frame.geometry('300x200')
        # 画面タイトル
        next_frame.title('Login Reset')
    else:
        messagebox.showerror("ログイン失敗","ログインできません。")
    
    


def main():

    
    # 画面サイズ
    login_window.geometry('300x200')
    # 画面タイトル
    login_window.title('Login Reset')
    # ラベル
    label1 = tkinter.Label(text='管理者ID')
    label1.place(x=30, y=30)
    label2 = tkinter.Label(text='パスワード')
    label2.place(x=30, y=70)
    # テキストボックス
    admin_id = tkinter.Entry(width=20)
    admin_id.place(x=90, y=30)
    # password = tkinter.Entry(width=20)
    password = tkinter.Entry(show='*', width=20)
    password.place(x=90, y=70)
    # ボタン
    log_button = lambda: login_click(admin_id.get(),password.get())
    btn = tkinter.Button(login_window, text='ログイン', command = log_button)
    
    btn.place(x=140, y=110)

    # 表示
    login_window.mainloop()

    

if __name__ == "__main__":
    
    with DAO_logreset.DB() as db:
        cur = db.connect.cursor()
        cur.execute("select * from admin")
        users = cur.fetchall()

    main ()
