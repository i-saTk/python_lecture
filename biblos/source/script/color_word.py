# 製作者：出田
# colorama を使って色付きprintするモジュール
from colorama import init as c_init
from colorama import Fore,Back

c_init(autoreset=True)

# エラーメッセージ用
def p_error_message(string):
    return print(Back.RED+Fore.LIGHTYELLOW_EX+string)

# メニュー用
def i_menu_message(string):
    print(Back.BLACK+Fore.LIGHTCYAN_EX+string,end="")
    return input("")

# 入力用
def i_message(string):
    print(Back.BLACK+Fore.LIGHTGREEN_EX+string,end="")
    return input("")


