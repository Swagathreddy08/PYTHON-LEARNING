shopping = []
while True:
 print("\n1. Add")
 print("2. Remove")
 print("3. View")
 print("4. Search")
 print("5. Quit")
 choice = input("Choose: ").strip()
 if choice == "1":
    item = input("Item: ").strip()
    shopping.append(item)
 elif choice == "2":
    item = input("Remove: ").strip()
    if item in shopping:
        shopping.remove(item)
 elif choice == "3":
    for i, item in enumerate(shopping, start=1):
        print(i, item)
 elif choice == "4":
    item = input("Search: ").strip()
    print(item in shopping)
 elif choice == "5":
    break
 else:
    print("Invalid choice")
