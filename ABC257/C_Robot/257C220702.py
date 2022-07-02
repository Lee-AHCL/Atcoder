

def main():
    n = int(input()) 
    s = list(input())
    w = list(map(int, input().split()))
    
    a = [[s[i], w[i]] for i in range(n)]
    a = sorted(a, key = lambda x : x[1])

    shokichi = s.count("1")
    kawari = shokichi
    ans = shokichi 
    
    for i in range(n):
        if a[i][0] == '1':
            kawari -= 1 
        else: 
            kawari += 1 
        
        if i < (n-1):
            if a[i][1] != a[i+1][1]: 
                ans = max(kawari, ans)
        else: 
            ans = max(kawari, ans)

    print(ans)

if __name__ == '__main__':
    main()
