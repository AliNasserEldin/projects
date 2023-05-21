def main():
    words = input("camelCase : ")
    res = sep(words)
    for i in range(len(res)-1):
        print(res[i],end="_")
    print(res[len(res)-1],end="")

def sep(words):
    res = []
    temp = ""
    loop = 0
    for i in range(len(words)):
        if words[i].isupper() or i == len(words)-1:
            if i == len(words)-1:
                for j in range(loop,i+1):
                    temp += words[j]
                loop = i
                res.append(temp.lower())
                temp =""
                return res
            for j in range(loop,i):
                temp += words[j]
            loop = i
            res.append(temp.lower())
            temp =""
    return res

main()