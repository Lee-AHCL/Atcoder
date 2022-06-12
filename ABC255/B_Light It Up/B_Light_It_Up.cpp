#include <iostream> // cout, endl, cin
#include <string> // string, to_string, stoi
#include <vector> // vector
#include <algorithm> // min, max, swap, sort, reverse, lower_bound, upper_bound
#include <utility> // pair, make_pair
#include <tuple> // tuple, make_tuple
#include <cstdint> // int64_t, int*_t
#include <cstdio> // printf
#include <map> // map
#include <queue> // queue, priority_queue
#include <set> // set
#include <stack> // stack
#include <deque> // deque
#include <unordered_map> // unordered_map
#include <unordered_set> // unordered_set
#include <bitset> // bitset
#include <cctype> // isupper, islower, isdigit, toupper, tolower
#include <stdlib.h>
#include <limits>
#include <random>
#include <cmath>
#include <numeric>

#define ll long long 

using namespace std;



int main(void)
{
    int n, k; 
    cin >> n >> k; 
    vector<int> A(k); 
    for(auto &num : A)
    {
        cin >> num;
        num--;
    }

    vector<ll> x(n), y(n);
    for(int i = 0 ; i < n ; i++)
    {
        cin >> x.at(i) >> y.at(i) ;
    }

    ll distmx = 0;
    for(int i = 0 ; i < n ; i++)
    {
        ll distmn = 8e18;
        for(auto &num : A)
        {
            distmn = min(distmn, (x.at(i) - x.at(num))*(x.at(i) - x.at(num)) + (y.at(i) - y.at(num)) * (y.at(i) - y.at(num)));
        }
        distmx = max(distmx, distmn);
    }

    cout << sqrt(double(distmx)) << endl;
    



    return 0;
}
