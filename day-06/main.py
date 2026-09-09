shop = []
total=0
dup=False
while True:
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
    for i in shop:
       print(f" {i} : {i[0]}") 
 elif choice == 2:
    item = input("Item: ").strip()
    quantity = int(input("enter the quantity in numbers: "))
    prize=int(input("enter the prize: "))
    entry=[item,quantity,prize]
    if len(shop) >0 :
       for i in shop:
          if entry[0] not in i[0]:
             dup=True
        if dup:
          shop.append(entry)
        else:
          print("cant add this item as ita=s already present")
          
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
    for i in shop:
       print(f"The count of the items in the shop are {len(shop)} and the total quantity of products are {sum(i[1])}")    
 elif choice == 6:
    for i in shop:
       val=i[1]*i[2]
       val+=val
    print("the total value of the store is :",total)
 elif choice == 7:
    break 
 else:
    print("Invalid choice")
