errorline=warningline=infoline=count=0
logs = """
2026-09-10 09:00:01 payment-service INFO Payment request received
2026-09-10 09:00:02 payment-service INFO Payment validated
2026-09-10 09:00:03 payment-service ERROR Payment gateway timeout
2026-09-10 09:00:04 auth-service INFO User authentication successful
2026-09-10 09:00:05 order-service WARNING Order processing delayed
2026-09-10 09:00:06 payment-service ERROR Payment retry failed
2026-09-10 09:00:07 inventory-service INFO Stock updated
2026-09-10 09:00:08 notification-service ERROR Email delivery failed
2026-09-10 09:00:09 order-service INFO Order completed
""".lower()
words=logs.split()
len=len(logs)
lines=logs.splitlines()
for line in lines:
    if "error" in line:
        errorline+=1
    elif "warning" in line:
        warningline+=1
    else:
        infoline+=1
    count+=1
print("************************************")
print("Basic Statistics")
print("************************************")
print(f'''
      The total character in the ord are : {len}
      Total logs    :   {count}
      INFO          :   {infoline}
      WARNING       :   {warningline}
      ERROR         :   {errorline}
      \n''')
print(" WORDS IN THE LOG ARE :\n")
print(set(words))
wo1=payment=auth=order=inventory=notification=0
for word in words:  
    wo1+=1
    if "payment-service" in word:
        payment+=1
    if "auth-service" in word:
        auth+=1
    if "order-service" in word:
        order+=1
    if "inventory-service" in word:
        inventory+=1
    if "notification-service" in word:
        notification+=1

print(f'''
     payment-service       :  {payment}
     auth-service          :  {auth}
     order-service         :  {order}
     inventory-service     :  {inventory}
     notification-service  :  {notification}
      \n''')

e1=e2=e3=e4=e5=0

for line in lines:
    if "error" and "payment-service" in line :
        e1+=1
    elif "error" and "auth-service" in line:
        e2+=1
    elif "error" and "order-service" in line:
        e3+=1
    elif "error" and "inventory-service" in line:
        e4+=1
    elif "error" and "notifition-service" in line:
        e5+=1
test=max(e1,e2,e3,e4,e5)