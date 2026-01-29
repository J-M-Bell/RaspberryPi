import yagmail

password = ""

with open("/home/jmbell97/Documents/temp.txt", "r") as f:
    password = f.read().rstrip()
    

yag = yagmail.SMTP("justinsraspberrypi71@gmail.com", password)

yag.send(to="justinmbell1997@gmail.com",
         subject="First email",
         contents="This is a test email.")
         
print("Email sent")