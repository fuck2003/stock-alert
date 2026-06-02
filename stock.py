symbol = "TSLA"
target = 1

url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"

data = requests.get(url).json()

price = data["c"]

if price > target:

    requests.post(
        WEBHOOK,
        json={
            "msgtype":"text",
            "text":{
                "content":
                f"【K股票预警】\n"
                f"股票:{symbol}\n"
                f"当前价格:{price}\n"
                f"触发价格:{target}"
            }
        }
    )
