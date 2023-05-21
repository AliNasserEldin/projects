def convert(text):
    buffer = text.replace(":)","🙂")
    buffer = buffer.replace(":(","🙁")
    return buffer

def main():
    temp = input()
    print (convert(temp))

main()