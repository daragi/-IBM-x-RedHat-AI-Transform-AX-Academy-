while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    except KeyboardInterrupt: # try - except 구조는 if문과 유사하게 사용 가능, if-elif
        print("Oops! That was Terminated...")
        break
    
import sys
f = open('./myfile.txt')
s = f.readline() # 한줄씩 출력
try:
    i = int(s.strip()) #0 및 공백 제거
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:",sys.exc_info()[0]) #에러를 발생시키고 해결안하기(책임전가)
    raise #에러 발생시키기
print(i)
# 출력값이 한줄 씩만 나옴, try에 print()를 사용해 문서 내용을 출력
# 파일에 한글이 있을 경우 출력불가

for arg in sys.argv[1:]:
    try:
        f  = open(arg,'r') #rwx (read, write, execution)
    except OSError:
        print("cannot open",arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()
        
try:
    raise Exception('spam', 'eggs') # anonymous class -> 객체 생성
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    
    x,y = inst.args
    print('x =',x)
    print('y =',y)