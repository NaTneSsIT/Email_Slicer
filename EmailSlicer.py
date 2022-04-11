def emailProcess(email):
    email_username=email[0:email.index("@")]
    email_domain=email[email.index("@")+1:]
    return [email_username,email_domain]
def main():
    email=input("Enter your email :")
    email_username,email_domain=emailProcess(email)
    print(f"Username :{email_username} Domain :{email_domain}")
if __name__=="__main__":
    main()