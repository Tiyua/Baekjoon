# 2739
a = int(input())
for i in range(1,10):
    print(a,"*",i,"=",a*i)

# 10950
a = int(input())
for i in range(0,a):
    b, c = map(int, input().split())
    print(b+c)

# 8393
n = int(input())
a=0
for i in range(0,n):
    a = a + i + 1
print(a)

# 15552
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+ b)

# 2741
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = i +1
    print(a)

# 2742
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = n - i
    print(a)

# 11021
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    c = a + b
    d = i + 1
    print(f"Case #{d}: {c}")

# 11022
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    c = a + b
    d = i + 1
    print(f"Case #{d}: {a} + {b} = {c}")

# 2438
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    j = i + 1
    print("*" * j)

# 2439
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    j = i + 1
    print(" " * (n - j) +"*" * j)

# 10871
import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(n):
    if l[i] < x :
        print(l[i])

# 10952
import sys
while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0  and b == 0 :
        break
    print(a+b)

# 10951
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except:
        break

# 1110
import sys
n = int(sys.stdin.readline().rstrip())
e = n
a = 0 
while True:
    b = n // 10
    c = n % 10
    d = c + b
    f = d % 10
    n = f + (c * 10)
    a = a + 1
    if(n == e):
        break
print(a)