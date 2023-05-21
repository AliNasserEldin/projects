def main():
    names = []
    while True:
        try:
            x = input()
            names.append(x)
        except EOFError:
            if len(names) > 1:
                print("Adieu, adieu, to ",end="")
                for i in range(len(names)-1):
                        print(names[i],", ",end="",sep="")
                print("and",names[-1])
            else:
                print(f"Adieu, adieu, to {names[0]}")
            break
main()