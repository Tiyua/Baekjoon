# 1330
a, b = map(int, input().split())
if a > b :
    print(">")
elif a < b :
    print("<")
else :
    print("==")

# 9498
a = int(input())
if a >= 90 :
    print("A")
elif a >= 80 :
    print("B")
elif a >= 70 :
    print("C")
elif a >= 60 :
    print("D")
else :
    print("F")

# 2753
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 : 
    print("1")
else :
    print("0")

# 14681
a = int(input())
b = int(input())
if a < 0 and b < 0 :
    print("3")
elif a > 0 and b < 0 :
    print("4")
elif a < 0 and b > 0 :
    print("2")
elif a > 0 and b > 0 :
    print("1")

# 2884
a, b = map(int, input().split())
if b >= 45 :
    print(a, b - 45)
elif a >= 1 :
    print(a - 1, 15 + b)
else :
    print(23 , 15 + b) 

# 2525
a, b = map(int, input().split())
c = int(input())
b = b + c
if b >= 60 :
    a = a + (b // 60)
    b = b % 60
if a >= 24 :
    a = a % 24
print(a, b) 

# 2480
a, b, c = map(int, input().split())
if a == b == c :
    d = 10000 + (a * 1000)
elif a == b :
    d = 1000 + (a * 100)
elif b == c :
    d = 1000 + (b * 100)
elif a == c :
    d = 1000 + (a * 100)
else :
    if a > b and a > c :
        d = a * 100
    elif b > a and b > c :
        d = b * 100
    else :
        d = c * 100
print(d)