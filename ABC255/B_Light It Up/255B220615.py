# B - Light It Up 
import math 

n, k = map(int, input().split())

A = list(map(int, input().split()))
A = list(map(lambda x : x-1, A))

zahyo = [list(map(int, input().split())) for _ in range(n)]


lightmax = 0 

for man in zahyo:
    lightmin = math.inf 
    for lighter in A: 
        tomoshibi = zahyo[lighter]
        xs = man[0] - tomoshibi[0] 
        ys = man[1] - tomoshibi[1] 
        light = xs**2 + ys**2 
        lightmin = min([lightmin, light])
    
    lightmax = max([lightmax, lightmin])
    
    
ans = math.sqrt(lightmax)
print(ans)
