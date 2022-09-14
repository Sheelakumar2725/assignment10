#10th assignment using for loop and range
#To print first n  odd natural numbers

n=int(input('enter a number:'))      
for e in range(1,n+1,1):
      if e%2!=0:
          print(e,end=' ')
print()      
