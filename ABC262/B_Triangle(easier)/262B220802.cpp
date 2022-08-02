#include <iostream>
#include <vector>

using namespace std;



int main() {
    int n, m;
    int u, v;
    int ans = 0;
    cin >> n >> m;
    vector attached(n, vector<bool>(n));
    
    for(int i = 0 ; i < m ; i++){
        cin >> u >> v;
        attached[u-1][v-1] = true;
        attached[v-1][u-1] = true;
    }
    
    for(int a = 0; a < n ; a++){
        for(int b = a + 1 ; b < n; b++){
            for(int c = b + 1 ; c < n; c++){
                if (attached[a][b] && attached[b][c] && attached[c][a])
                    ans++;
            }
        }
    }
    
    cout << ans << endl;
    
    return 0;
}
