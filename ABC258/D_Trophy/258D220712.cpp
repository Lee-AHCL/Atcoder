#include <iostream>
#include <string>
#include <vector>
 
#define ll long long
 
using namespace std;
 
 
int main(void) {
    int n, x;
    cin >> n >> x;
    vector<int> a(n), b(n);
    ll ans = numeric_limits<ll>::max();
    ll sum = 0;
    
    for(int i = 0 ; i < n ; i++){
        cin >> a[i] >> b[i];
    }
    
    for(int i = 0 ; i < n ; i++){
        x--;
        if(x == 0){
            break;
        }
        sum += (a[i] + b[i]);
        ans = min(ans, sum + (ll)b[i] * x);
    }
    
    cout << ans << endl;
    
    
    return 0;
}
 
