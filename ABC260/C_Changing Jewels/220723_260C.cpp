#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <iomanip>   // setprecision

#define ll long long

using namespace std;

ll n, x, y, r[12], b[12];
int N, X, Y;

int calcul(int lev, bool is_red){
    if (lev == 1)
        return is_red ? 0 : 1;
    if (is_red)
        return calcul(lev - 1, true) + calcul(lev, false) * X;
    else
        return calcul(lev - 1, true) + calcul(lev - 1, false) * Y;
    return 0;
}

int main(void) {
    cin >> n >> x >> y;
    r[1] = 0;
    b[1] = 1;
    
    for(int i = 2 ; i <= n ; i++){
        b[i] = r[n-1] + b[n-1] * y;
        r[i] = r[n-1] + b[n] * x;
    }
    
    cout << r[n] << endl;
    
    //cin >> N >> X >> Y;
    //cout << calcul(N, true) << endl; 
    
    return 0;
}
