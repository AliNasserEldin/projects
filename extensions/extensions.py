def main():
    app = input("File name : ")
    app = app.lower().strip()
    if app[-4:] == ".gif":
        print("image/gif")
    elif app[-4:] == ".jpg":
        print("image/jpeg")
    elif app[-5:] == ".jpeg":
        print("image/jpeg")
    elif app[-4:] == ".png":
        print("image/png")
    elif app[-4:] == ".pdf":
        print("application/pdf")
    elif app[-4:] == ".txt":
        print("text/plain")
    elif app[-4:] == ".zip":
        print("application/zip")
    else :
        print("application/octet-stream")
main()