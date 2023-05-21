def main():
    answer = input("what's is the answer to the great question of life, the university , and everything?")
    match answer.lower().strip():
        case "42":print("Yes")
        case "forty two":print("Yes")
        case "forty-two":print("Yes")
        case other : print("No")


main()