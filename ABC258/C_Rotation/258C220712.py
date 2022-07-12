def main():
    n, q = map(int, input().split())
    s = input() 
    change = 0
    
    for _ in range(q):
        q_t, q_x = map(int, input().split())
        if q_t == 1:
            change += q_x 
        else: 
            q_x -= 1
            print(s[q_x - (change % n)]) 
                
 
 
if __name__ == "__main__":
    main()
