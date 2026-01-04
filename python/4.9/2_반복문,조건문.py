answer = int(input("숫자를 입력하세요"))
if answer < 0 :
    print("음수입니다.")
elif answer > 0 :
    print("양수입니다.")
else:
    print("0입니다.")
    
words = ['cat','window','defenestrate']
for w in words:
    print(w,(len(w)))
    
for i in range(5,10):
    print(i)
for i in range(0,10,3):
    print(i)
for i in range(-10,-100,-30):
    print(i)
print()
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])
print()
print(sum(range(4)))
print(list(range(4)))

for n in range(2,10):
    for x in range(2, n):
        if n%x ==0:
            print(n,'equals',x,"*",n//x)
            break
    else:
        print(n, 'is a prime number')
        
for num in range(2,10):
    if num % 2 ==0:
        print("Found an even number", num)
        continue
    print("Found a number", num)