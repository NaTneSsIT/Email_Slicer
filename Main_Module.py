from EmailSlicer import emailProcess

def main():
    emails=["natnessit@gmail.com","HTT1@haui.edu","CSGO@steam.com"]
    for email in emails:
        username,domain=emailProcess(email)
        print(f"Username :{username}  -  Domain :{domain}")
if __name__=="__main__":
    main()