import math 
 
def main():
    n, x = map(int, input().split())
    sm = 0
    jeux = [list(map(int, input().split())) for _ in range(n)]
    ans = math.inf 
    
    for i in range(n):
        game = jeux[i]
        x -= 1
    
        if x == 0:
            break 
        
        sm += sum(game)
        ans = min(ans, sm + game[1] * x)
        
            
  
    print(ans)
    return 
            
        
 
 
if __name__ == "__main__":
    main()
