
def main():
    n, m = map(int, input().split())
    attached = [[False] * n for _ in range(n)]
    ans = 0

    for _ in range(m): 
        u, v = map(int, input().split())
        attached[u-1][v-1] = True 
        attached[v-1][u-1] = True 

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if attached[a][b] and attached[b][c] and attached[c][a]:
                    ans += 1

    print(ans)

    


if __name__ == "__main__":
    main() 
