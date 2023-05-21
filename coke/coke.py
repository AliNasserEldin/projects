def main():
    start = 50
    print("Amount Due: 50")
    coin = input("Insert Coin: ")
    coin = int(coin)
    change = start - coin
    while change > 0:
        print(f"Amount Due: {change}")
        coin2 = input("Insert Coin: ")
        coin2 = int(coin2)
        change = change - coin2
    print(f"Change Owed: {-change}")

main()