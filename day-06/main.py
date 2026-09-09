import warnings
shop = []
while True:
 total=0
 dup=False
 print("1. names")
 print("2. add")
 print("3. remove")
 print("4. Search")
 print("5. product count")
 print("6. Total value")
 print("7. Quit")
 choice = int(input("Choose: "))
 if choice == 1:
    print("the names of items in the shop are: \n")
    shop.sort()
    for i in shop:
       print(f" {i} : {i[0]}") 
 elif choice == 2:
    item = input("Item: ").strip()
    quantity = int(input("enter the quantity in numbers: "))
    prize=int(input("enter the prize: "))
    entry=[item,quantity,prize]
    if len(shop) >0 :
       for i in shop:
          if entry[0] == i[0]:
             dup=True
       if dup == False:
          shop.append(entry)
       else:
          for i in shop:
             if entry[0] == i[0]:
                i[1]+=quantity
          
    else:
       shop.append(entry)
 elif choice == 3:
    item = input("Remove: ").strip()
    for i in shop:
        if item in i[0]:
           shop.remove(i)
 elif choice == 4:
    item = input("Search: ").strip()
    for i in shop:
       if item in i[0]:
          print(f" the {item} is available in the shop")
 elif choice == 5:
    sum=0
    for i in shop:
       sum+=i[1]
    print(f"The count of the items in the shop are {len(shop)} and the total quantity of products are {sum}")    
 elif choice == 6:
    for i in shop:
       val=i[1]*i[2]
       total+=val
    print("the total value of the store is :",total)
 elif choice == 7:
    break 
 else:
    print("Invalid choice")

for i in shop:
   if i[1]<5:
      warnings.warn(f"the stalk is verry low for the product {i[0]}")

