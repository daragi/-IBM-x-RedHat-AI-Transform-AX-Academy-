# -*- coding: <UTF-8> -*-
## 1.int
print("hello")
a = [1, '1', "1"] # 문자열 배열
a = str(a[0]) + a[1] + a[2] # 문자열 - concatenation
b = int(a[0]) + int(a[1]) + int(a[2]) # 정수형으로 연산
print(a)
print(b)
# python: int , str 에 대한 연산자 재정의가 안되어 있음
# literal 이 필요, 연산을 하려면 문자열을 통일
print(8/5)
print(10/5)
print(10//5)
print(10%5)
print(10*5)
print(10**5)
print()

# shift 연산 : 음수를 표현할 방법이 없음 => sipn bit

i = 1 # 1

# language int 32bit

print(i << 1) # 10 
print(i << 2) # 100
print(i >> 1) # 0
print(i << 31) # 31번째 자리는 부호비트, 0번째에서 시작, 자리는 총 32개개 -> -2**31

i = 8 # 1000

print(i >> 3) # 1
print(i >> 10) # 0

i = -1 # - 1

print(i << 1) # -10  
print(i << 2) # -100
print(i >> 1) # -0


#-real memory
# :클래스, 함수, 메서드 등을 선언할 때 부모 변수(클,함,메)가 자식 변수에 '상속'할 때
# 메모리의 크기가 변동이 생길 수 있다. 예를 들어 일반적인 데이터를 상속할 경우 error가 발생할 수 있지만
# python은 할당이 가능하다.
# why? 파이썬은 태그를 달아서 변형이 필요하면 다른 곳으로 메모리를 잡기 때문에
# 그니까 공간이 부족할 경우에 다른 데 부모의 태그를 달아서 그곳을 그냥 마치 둔갑?
# 해서 데이터를 옮길 수 있다

print(float('inf'))

# int(Hex) : 0x(0~F)
# int(Octal) : 0o16
# int(binary) : 0b0010
# complex : 복소수 ex) 45+ 0j
# false = 0 ,  true = 0이외의 다른 값   =>   int를 상속해서 정의


## 2. String
print('span eggs')
print('doesn\'t') # use \' to escape the single quote...
print("doesn't")
print('"yes",they said.')
print("\"yes\",they said.")
s = 'First line.\nSecond line.' #\n means newline
s # without print(), \n is included in the ouput
print('C:\some\name')
print('C:\some\\name')
print(r'C:\some\name')  # r = escape 코드를 무시
print()
print(""" Usage: thingy [OPTIONS]
      -h        Display this usage message
      -H hostname       Hostname to connect to
      """) # """~~~ "" 문자 여러 줄 출력
print(3*'ha'+'bi')
print('Put several strings within parentheses '  \
      'to have them joined together.')

word = 'python'
print(word[0:2])
print(word[2:5])
print(word[:4]+word[4:])
print(word[:5])
print(word[:-1])
print(word[-5:3])

# 파이썬은 문자열을 변경할 수 없다
# word[0] = 'J'
# word = 'Jython'
word = 'J' + word[1:]
length = len(word)
print(word)
print(length)

# bool 을 int에 상속할 경우 like 환승 int보다 속도가 느려짐