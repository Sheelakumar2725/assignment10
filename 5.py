#10th assignment using for loop and range
#To print first n  odd natural numbers in reverse order

n=int(input('enter a number:'))      
for e in range(n,0,-1):
      if e%2!=0:
          print(e,end=' ')
print()      
