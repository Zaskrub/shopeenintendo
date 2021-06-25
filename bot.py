import time
import threading
import requests
from colorama import Fore
from colorama import init
import json
init(autoreset=True)

# แก้ไขตัวแปรนี้ (Cookie)
cookie = "SPC_IA=-1; _fbp=fb.2.1578202102406.1027072148; SPC_F=5c6uSJmS1hQPwefWbkTnWvPhkcgW8EAr; REC_T_ID=2f698b12-2f7c-11ea-8d5b-9c7da3191bc4; G_ENABLED_IDPS=google; language=th; SPC_CLIENTID=5c6uSJmS1hQPwefWsimjnkicbmwqjomj; _gcl_au=1.1.1423490084.1618827836; _fbc=fb.2.1624174919706.IwAR18UK3JRn_8LXHWRwDM2F7c_Ly2CS7OU1r3zQGZ7Pxr5f1_YUWhQzjcE_o; _gcl_aw=GCL.1624285844.CjwKCAjw8cCGBhB6EiwAgOReyz_gyEEBk-uy4wAOke-jT2eo0JP5tFsQqkIwPRcO827tdxcWxySQ6xoCf1MQAvD_BwE; _gac_UA-61914165-6=1.1624285846.CjwKCAjw8cCGBhB6EiwAgOReyz_gyEEBk-uy4wAOke-jT2eo0JP5tFsQqkIwPRcO827tdxcWxySQ6xoCf1MQAvD_BwE; SPC_PC_HYBRID_ID=59; csrftoken=dUtZw4lbC5rk0lNil3mdB0NTn0Y108lD; SPC_SSN=o; SPC_WSS=o; SPC_SI=bfftocth1.1wnVOszJqnxZSItJE4mX8Dsc5ncxYg9A; welcomePkgShown=true; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.106733014.1624506680; G_AUTHUSER_H=5; SPC_U=473897556; SPC_EC=9i5mYjZNZTQM8c5WHnhfgD3CNaGW+oLIpWMs5SmRcxb/+ml2LbF4JrcEHgenTKo2HehdAOKAFVcfQZ6zoqyctwX9eXMAwdJLVmsqbSEEOuolis0ILHrSfRruJzupo1NHL1lkQX0LhKKTeMCzClsQHpGrcwZ0chAw4QlJK8Cct40=; _med=affiliates; _ga_L4QXS6R7YG=GS1.1.1624506678.63.1.1624506811.44; _ga=GA1.3.2034149398.1578202105; SPC_R_T_ID="Tp41pdnloLN+VZgVw2MwhHU5qosCVLG8THUy9WyXk4N6WPEi/LDqUhHP07/c1PdNgcrmtml9BMwvnUopnIh37TSquPk41ddhZmEZpDjLz8U="; SPC_T_IV="HjwJXOr6zAqI0hNYLEMGQA=="; SPC_R_T_IV="HjwJXOr6zAqI0hNYLEMGQA=="; SPC_T_ID="Tp41pdnloLN+VZgVw2MwhHU5qosCVLG8THUy9WyXk4N6WPEi/LDqUhHP07/c1PdNgcrmtml9BMwvnUopnIh37TSquPk41ddhZmEZpDjLz8U="; REC_T_ID=93e88f47-d4a1-11eb-9e23-d0946600c94b; SPC_EC=9i5mYjZNZTQM8c5WHnhfgD3CNaGW+oLIpWMs5SmRcxb/+ml2LbF4JrcEHgenTKo2HehdAOKAFVcfQZ6zoqyctwX9eXMAwdJLVmsqbSEEOuolis0ILHrSfRruJzupo1NHL1lkQX0LhKKTeMCzClsQHpGrcwZ0chAw4QlJK8Cct40=; SPC_SSN=o; SPC_U=473897556; SPC_WSS=o"

def bot():
	global cookie
    while True:
        url = "https://shopee.co.th/api/v4/cart/add_to_cart"
        payload = json.dumps({
        "quantity": 1,
        "checkout": True,
        "update_checkout_only": False,
        "donot_add_quantity": False,
        "source": "{\"refer_urls\":[]}",
        "client_source": 1,
        "shopid": 98838392,
        "itemid": 5287430514,
        "modelid": 100261315994
        })
        headers = {
        'Cookie': str(cookie),
        'Content-Type': 'application/json'
        }
        r = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(r.text)
        if "cart_item" in result['data']:
            print("\033[32;1m[Nintendo] add to card success")
        else:
            print("\033[31;1m[Nintendo] found errors")

ths = input("Enter threads : ")
print("""\u001b[34;1m

███████╗██╗  ██╗ ██████╗ ██████╗ ███████╗███████╗██████╗  ██████╗ ████████╗
██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
███████╗███████║██║   ██║██████╔╝█████╗  █████╗  ██████╔╝██║   ██║   ██║   
╚════██║██╔══██║██║   ██║██╔═══╝ ██╔══╝  ██╔══╝  ██╔══██╗██║   ██║   ██║   
███████║██║  ██║╚██████╔╝██║     ███████╗███████╗██████╔╝╚██████╔╝   ██║   
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   
                                                                           

""")
print("\033[33;1mBy ZASXCV")
for i in range(int(ths)):
    thr = threading.Thread(target=bot)
    thr.start()