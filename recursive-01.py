def factorial(n):
    if n == 0:  # 기저 조건: 0! = 1
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 출력: 120

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # 출력: 5

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # 출력: 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(56, 98))  # 출력: 14

def sum_of_array(arr, n):
    if n <= 0:
        return 0
    return sum_of_array(arr, n-1) + arr[n-1]

arr = [1, 2, 3, 4]
print(sum_of_array(arr, len(arr)))  # 출력: 10

def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_max(arr, n-1))

arr = [1, 5, 3, 9, 2]
print(find_max(arr, len(arr)))  # 출력: 9
