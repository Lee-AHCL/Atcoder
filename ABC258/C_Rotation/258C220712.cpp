#include <iostream>
#include <string>
 
#define ll long long
 
using namespace std;
 
 
int main(void) {
    ll n, q;
    ll t, x;
    string s;
    ll change = 0;
    ll ind;
    cin >> n >> q;
    cin >> s;
    
    
    for(int i = 0 ; i < q ; i++){
        cin >> t >> x;
        if (t == 1)
            change += x;
        else {
            x--;
            ind = x - (change % n);
            if (ind <0)
                ind += n;
            cout << s.at(ind) << endl;
        }
    }
    
    return 0;
}
 
