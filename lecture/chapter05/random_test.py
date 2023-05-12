# randomモジュールのrandint関数
from random import randint

# 1～6までのランダムな値を取得
print(randint(1,6))

# randomモジュールのrandint関数をdiceという別名で読み込む
from random import randint as dice

# dice関数を用いて1～6までのランダムな値を取得
print(dice(1,6))
print(dice(0,1000))
print(help(dice))
