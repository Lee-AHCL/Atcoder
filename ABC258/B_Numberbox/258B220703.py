def main():
    n = int(input())
    A = []
    
    for i in range(n):
        row = [int(i) for i in input()]
        A.append(row)
    
    direci = [-1, -1, -1, 0, 0, 1, 1, 1]
    direcj = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    ans = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(8):
                fangi = direci[k]
                fangj = direcj[k]
                hikaku = 0
                for l in range(n):
                    hikaku *= 10 
                    hikaku += A[(i + fangi * l)%n][(j + fangj * l)%n]
                
                ans = max(ans, hikaku)
                    
                
    print(ans)



if __name__ == "__main__":
    main()
