try:
    # 身長と体重の入力
    h = float(input("身長(m)を入力してください。："))
    w = float(input("体重(kg)を入力してください。："))

    # 入力値のチェック
    if h <= 0 or w <= 0:
        raise ZeroDivisionError

    # BMIの計算と表示
    bmi = w / h ** 2
    print(bmi)
except ValueError:
    print("正しい値を入力してください")
except ZeroDivisionError:
    print("0以下の数値は入力できません")