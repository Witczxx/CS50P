# "https://api.frankfurter.dev/v2/rates?quotes=EUR,CNY"

import matplotlib.pyplot as plt
import pandas as pd
import requests

data_now = requests.get("https://api.frankfurter.dev/v2/rates?quotes=EUR,CNY")

data_now_json = data_now.json()

data_history = requests.get(
    "https://api.frankfurter.dev/v2/rates?quotes=EUR,CNY&from=2024-01-01&group=month&providers=ECB"
)
data_history_json = data_history.json()


print(data_now_json)
print(data_history_json)


# data = ... deine lange Liste von Dicts
df = pd.DataFrame(data_history_json)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

plt.figure(figsize=(8, 4))
plt.plot(df["date"], df["rate"], marker="o")
plt.title(f"{df['base'].iloc[0]} → {df['quote'].iloc[0]}")
plt.xlabel("Date")
plt.ylabel("Rate")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
