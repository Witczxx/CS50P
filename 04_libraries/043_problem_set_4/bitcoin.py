"""
Notes:
sys.argv[1]
len(sys.argv) == 2
"""

import sys

import requests


def main():
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")
    except IndexError:
        sys.exit("Missing command-line argument.")
    bitcoin_value = get_value()
    multiplicated_value = float(bitcoin_value) * float(sys.argv[1])
    print(f"${multiplicated_value:,.4f}")


def get_value():
    try:
        bitcoin_query = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=03ecf32c36245294840e02c90704b0d8cc213423ba62e7ea9a5375eb356ada05"
        )
        bitcoin_json = bitcoin_query.json()
        bitcoin_json["data"]["priceUsd"]
        return float(bitcoin_json["data"]["priceUsd"])
    except requests.RequestException:
        print("Error in accessing data.")
        sys.exit()


if __name__ == "__main__":
    main()
