import sys
log = sys.stdin.read()
log=log.lower()
words=log.split()
len=len(log)
err=0
ser="payment service"
c=0
warn=0
wo1=0
err=0
errorline=0
warningline=0
paymentline=0
count=0
for word in words:  
    wo1+=1
    if "error" in word:
        err+=1
    if "warning" in word:
        warn+=1
    if ser in word:
        c+=1
lines=log.splitlines()
for line in lines:
    if "error" in line:
        errorline+=1
    if "warning" in line:
        warningline+=1
    if ser in line:
        paymentline+=1
    count+=1

print(f''' the given log consits of {len} character
           thr given log consits of {words} words i.e {wo1}\n    
           the given logs are {lines} 
           the error count in logs is {err}
           the warning count in log is {warn}
           the number of error lines are {errorline}
           the number of warning lines are {warningline}
           the number of payment lines are {paymentline}
           the total number of lines are {count}
           ''')
if ser in words:
    print(f" the the sevice we seached for is {ser} it occured for {c} times ")
else:   
    print("the service we are looking for is not available")
