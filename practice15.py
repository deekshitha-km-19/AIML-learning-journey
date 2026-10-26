username=(input("enter username:"))
password=(input("enter password:"))
if(username=="admin"and password=="pass"):
    print("success")
else:
    if(username!="admin"):
        print("wrong username")
    else:
        print("wrong password")

        colour=input("enter colour:")
        match colour:
            case "green":
                print("go")
            case "yellow":
                print("look")
            case "red":
                print("stop")
            case _:
                print("wrong colour!")

                while true:
                    print("hello world")
                    count=1
                    while(count<=5):
                        print(" hi hello")
                        count+1
                        print("after loop ,count=",count)
                        