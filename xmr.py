import requests
from bs4 import BeautifulSoup
import config

def return_balance() -> float:
    # nanominerに溜まってるXMRを取得
    url = f"https://api.nanopool.org/v1/xmr/balance/{config.ADDRESS}"
    res = requests.get(url)
    balance = float(res.json()["data"])
    
    # 現在のXMRの価格を取得
    url = f"https://coinmarketcap.com/ja/currencies/monero/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.select("#section-coin-overview > div.sc-65e7f566-0.czwNaM.flexStart.alignBaseline > span")
    xmr_yen = float(elems[0].text.translate(str.maketrans({"¥":"",",":""})))
    
    return balance * xmr_yen

def return_hashrate(hour: int, member: str) -> float | int:
    if member:
        url = f"https://api.nanopool.org/v1/xmr/workers/{config.ADDRESS}"
        res = requests.get(url)
        data = res.json()["data"]
        for i in range(len(data)):
            if data[i]["id"] == member:
                hashrate = data[i]["hashrate"]
                return hashrate
        return 0
    elif hour:
        url = f"https://api.nanopool.org/v1/xmr/avghashratelimited/{config.ADDRESS}/{hour}"
        res = requests.get(url)
        ave_hashrate = res.json()["data"]
        return ave_hashrate
    else:
        url = f"https://api.nanopool.org/v1/xmr/hashrate/{config.ADDRESS}"
        res = requests.get(url)
        current_hashrate = res.json()["data"]
        return current_hashrate

def return_member() -> list:
    url = f"https://api.nanopool.org/v1/xmr/workers/{config.ADDRESS}"
    res = requests.get(url)
    data = res.json()["data"]
    member_list = [data[i]["id"] for i in range(len(data)) if data[i]["hashrate"] != 0]
    return member_list