c=1
p,n,z=0,0,0
while c<6:
    a=int(input("Enter a number: "))
    c+=1
    if a==0:
        print(f"you entered {a}")
        z=+1
    elif a>0:
        print(f"you entered {a} which is positive")
        p+=1
    else:
        print(f"you entered {a} which is negative")
        n+=1
print(f"you entered {p} positive numbers, {n} negative numbers and {z} zeros")