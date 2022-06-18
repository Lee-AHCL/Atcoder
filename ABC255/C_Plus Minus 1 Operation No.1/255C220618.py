import math 

x, a, d, n = map(int, input().split())

if d < 0:
    a = a + d * (n-1)
    d *= -1     

st = 0 
ed = n-1 



while st <= ed : 
    md = (ed + st) // 2
    if a + md * d < x: 
        st = md + 1 
    else: 
        ed = md - 1 
        
ans = math.inf 

start = max([0, st-3])
end   = min([n-1, st+3])

for i in range(start, end + 1):
    ans = min([ans, abs(a + d*i - x)])

print(ans) 


# Binary Search
