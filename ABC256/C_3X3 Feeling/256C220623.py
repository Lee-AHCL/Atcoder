h1, h2, h3, w1, w2, w3 = map(int, input().split()) 

cnt = 0 

for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            for d in range(1, 31): 
                e = h1 - a - b 
                f = w3 - b - c 
                g = h3 - c - d 
                h = w1 - a - d 
                i = w2 - e - g 
                if e > 0 and f > 0 and g > 0 and h > 0 and i > 0 and (i + f + h) == h2 :
                    cnt += 1 
                
                
print(cnt)     


# 馬鹿みたいな解放なのに制限が低くてこれでもできる。DFSでもやってみようと思う
