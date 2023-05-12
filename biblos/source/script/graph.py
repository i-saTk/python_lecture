import matplotlib.pyplot as plt
import pandas as pd
from DAO import DB

def show_bar_graph(db:DB):

    book_list = db.sel_query("*","book")
    renta_list = db.sel_query("*","rental")

    # print(book_list)

    book_dict1 = []
    book_dict2 = []

    for i in range(len(book_list)):
        list(book_list[i])
        book_dict1.append(book_list[i][0])
        book_dict2.append(book_list[i][1])

    book_dict =dict(zip(book_dict1,book_dict2))

    renta_co =[]

    for i in range(len(renta_list)):
        list(renta_list[i])
        renta_co.append(renta_list[i][0])

    rent_co2 = pd.unique(renta_co).tolist()

    rent_co3 = []

    for i in range(len(rent_co2)):
        co = 0
        for i2 in range(len(renta_co)):
            if rent_co2[i] == renta_co[i2]:
                co += 1
        rent_co3.append(co)

    book_rent_co =dict(zip(rent_co2,rent_co3))

    book_rent_co = sorted(book_rent_co.items(), key=lambda x:x[1], reverse=True)
    book_rent_co = dict((x, y) for x ,y in book_rent_co)

    book_rent_bookid = list(book_rent_co.keys())
    book_rent_count = list(book_rent_co.values())


    book_rent_bookid2 = book_rent_bookid[:10]
    book_rent_count2 = book_rent_count[:10]


    book_rent_name = []

    for i in range(len(book_rent_bookid2)):
        book_id = book_rent_bookid2[i]
        book_rent_name.append(book_dict[book_id])

    left = book_rent_name
    height = book_rent_count2


    plt.rcParams['font.family'] = "MS Gothic"
    plt.xticks(rotation=-45)
    plt.tick_params(labelsize=7)
    plt.bar(left,height)

    plt.show()

def show_line_graph(db:DB, sel_year):

    rental_list = db.sel_query('*','rental')

    rent_s = []

    for i in range(len(rental_list)):
        list(rental_list[i])
        rent_s.append(rental_list[i][3])

    try:
        # 年月のみ抽出--------------------------------------------------
        df = pd.DataFrame(rent_s)
        df.columns = ["date"]
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        # .dt.strftime("%Y-%m")
        df2 = df[df["date"].dt.year == sel_year]
        month_x =[f"{sel_year}-{i}" for i in range(1,13)]
        month = []
        for i in range(1,13):
            temp = df2[df2["date"].dt.month == i].count()
            month.append(int(temp))
        # ---------------------------------------------------
    except Exception:
        month_x =[]
        month = []
    # グラフ可視化（折れ線グラフ）
    plt.plot_date(month_x, month, label='Loan per month', linestyle='solid')

    # 書式設定
    plt.legend(loc="best")         # 凡例
    plt.gcf().autofmt_xdate()      # X軸値を45度回転
    plt.savefig("date_graph3.jpg") # 画像保存
    plt.show()                     # グラフ表示
    plt.close()

def show_pie_chart(db:DB):
        
    db.cursor_create()
    # db.cursor.execute("SELECT distinct publish FROM book")
    db.cursor.execute("SELECT publish, count(*) FROM book group by publish order by count(*) desc")
    rows = db.cursor.fetchall()
    li_publish=[]
    li_publish2=[]
    for i in range(10): #上位 10社を選定　range(10)
        li_publish.append(rows[i][0])
        li_publish2.append(rows[i][1])
    db.cursor.close()

    ###########################################################################
    import matplotlib.pyplot as plt
    # li_publish=[]
    # li_publish2=[]
    ex = []
    for i in range(len(li_publish)):
        ex.append(0.1)

    plt.rcParams['font.family'] = "MS Gothic"
    plt.pie(li_publish2, explode=ex, labels=li_publish, autopct="%1.1f%%", counterclock=False)
    plt.show()
