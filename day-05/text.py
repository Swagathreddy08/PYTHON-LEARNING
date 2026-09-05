a=input("enter the sentence : ").lower()
b=input("enter the choosen word : ").lower()
word=a.split()
count=0
for word in word:
    if b==word:
        count=count+1
        con="True"
print(word)
if a is not "":
    print(f'''{con} the choosen word is {b} is in the sentence it occured for {count} times. The first leter of string is {a[0]}and the last letter is {a[-1]}''')