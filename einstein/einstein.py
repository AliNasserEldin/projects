def main():
    m = input("m : ")
    print(calc(int(m)))

def calc(m):
    res = m * (300000000 * 300000000)
    return res

main()