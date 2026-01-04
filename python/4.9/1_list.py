squares = [1,4,9,16,25]
print(squares)
print(squares[0])
print(squares[1])
print(squares[2])
print(squares[-3])
print(squares + [36,49,64,81,100])

cubes = [1,8,27,65,125]
cubes[3] = 4**3
print(cubes)
cubes.append(216)
cubes.append(7**3)
print(cubes)
print()

letters = ['a','b','c','d','e','f','g']
letters[2:5] = ['C','D','E']
letters[2:5] = []
print(letters)
print()

a= ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print()

# 피보나치 수열
a= 0; b=1
while a< 10:
    print(a, end='\t')
    a,b = b,a + b # 스왑
print([1,2,3]*3)
print()
i= 256*256
print('The value of i is',i) #, 는 띄어씌기가 있음
print('The value of i is'+ str(i)) # +는 띄어씌기가 없음
print('The value of i is %d'%i) # %d는 띄어씌기가 있음
print()

temp = input("입력하세요:")
temp = int(temp)
print(type(temp))
