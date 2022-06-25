n = int(input()) 

lr = [list(map(int, input().split())) for _ in range(n)]

lr = sorted(lr, key = lambda x : x[0]) 

curL, curR = lr[0] 

for i in range(1, n):
  nextL, nextR = lr[i] 
  if curR < nextL: 
    print("{0} {1}".format(curL, curR))
    curL, curR = nextL, nextR 
  else: 
    curR = max(curR, nextR)
    
print("{0} {1}".format(curL, curR)) 
