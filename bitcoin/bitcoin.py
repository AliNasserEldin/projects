import requests,json
from sys import argv,exit

def main():
    while True:
        try:
            if len(argv) != 2:
                exit("Missing command-line argument")
            elif not isfloat(argv[1]):
                exit("Command-line argument is not a number")
            res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            res = res.json()
            price = round(res["bpi"]["USD"]["rate_float"]*float(argv[1]),4)
            print(f"${price:,}")
            exit(0)
        except requests.RequestException:
            pass


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
main()