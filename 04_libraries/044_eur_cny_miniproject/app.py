import os
import tempfile

import matplotlib.pyplot as plt
import pandas as pd
import requests
import rumps

data_now = requests.get("https://api.frankfurter.dev/v2/rates?quotes=EUR,CNY")
data_now_json = data_now.json()
data_history = requests.get(
    "https://api.frankfurter.dev/v2/rates?quotes=EUR,CNY&from=2024-01-01&group=month&providers=ECB"
)
data_history_json = data_history.json()

# data = ... deine lange Liste von Dicts
df = pd.DataFrame(data_history_json)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


class CurrencyApp(rumps.App):
    def __init__(self):
        super().__init__(
            name="MyMenu",
            title=f"€/¥: {round(data_now_json[0]['rate'], 2)}",
        )

        self.menu = [rumps.MenuItem("Show overview (plot)")]

    @rumps.clicked("Show overview (plot)")
    def show_overview(self, _):
        # Plot erzeugen
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df["date"], df["rate"], marker="o")
        ax.set_title(f"{df['base'].iloc[0]} → {df['quote'].iloc[0]}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Rate")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        # Als temporäre PNG speichern
        tmp_dir = tempfile.gettempdir()
        out_path = os.path.join(tmp_dir, "eur_cny_overview.png")
        fig.savefig(out_path, dpi=150)
        plt.close(fig)

        # Optional: Bild im Default Viewer öffnen (macOS)
        # (Wenn du das lieber weglassen willst, sag Bescheid.)
        os.system(f'open "{out_path}"')


if __name__ == "__main__":
    CurrencyApp().run()
