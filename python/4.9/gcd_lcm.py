def gcd(a, b):
    # 유클리드 호제법
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# 테스트
a = 48
b = 18

print(f"{a}와 {b}의 최대공약수(GCD):", gcd(a, b))
print(f"{a}와 {b}의 최소공배수(LCM):", lcm(a, b))