i=1
while(i<=10):
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1
    print("outside loop..")


    i=1
    while(i<=10):
        print(i)
        i+=2

i=1
while(i<=10):
    if(i%2==0):
        i+=1
        if(i%2==0):
            continue
        print(i)
        
