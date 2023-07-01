def check(n, memo):
    if memo[n]:
        return memo[n]
    if n == 1 or n == 0:
        return n
    memo[n] = check(n-1, memo) + check(n-2, memo)
    return memo[n]

n = int(input("Nhap n = "))
memo = [0] * (n+1)
tmp = 0
for i in range(n+1):
    if check(i, memo) > n:
        tmp = i
        break

if check(tmp-1, memo) == n:        
    print("So " + str(n) + " la so fibonacci")
else:
    print("Khong phai so fibonacci")
