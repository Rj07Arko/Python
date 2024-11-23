import time

def add(a,b) :
    c=a+b
    return c

def sub(a,b) :
    c=a-b
    return c

def multi(a,b) :
    c=a*b
    return c

def div(a,b) :
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        print(f"Exception : {e}")
    
       

def main():
    print("This is a Basic calculator programme : ")
     
    for a in ("For addition"," type'A'","\nfor substraction"," type 'S'","\nfor multiplication"," type 'M'","\nfor division"," type 'D'","\n'E'"," to exit\n") :
        print(a,flush=True,end="")
        time.sleep(1.5)
    
    while True :
        option=input("provide option : ")

        if option in ("A","S","M","D"):
            a=input("Input-1 : ")
            b=input("Input-2 : ")
            
            if (a.isnumeric()== False) or (a.isnumeric()== False):
                print("One of inputs or both not contain number")
                continue
            else:
                a=int(a)
                b=int(b)

            if option == "A":
                result=add(a,b)

            if option == "S":
                result=sub(a,b)

            if option == "M":
                result=multi(a,b)

            if option == "D":
                result=div(a,b)
            if result:
                print(result)

        elif option == "E":
            break

        else :
            continue

if __name__ == "__main__" :
    main()
    print("Adiós!")

