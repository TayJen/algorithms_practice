#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    s += "$";
    int n = s.length();
    
    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        p[i] = i;
    }
    sort(p.begin(), p.end(), [&](int i, int j) {
        return s.substr(i) < s.substr(j);
    });
    
    vector<int> c(n);
    for (int i = 0; i < n; i++) {
        c[p[i]] = i;
    }

    vector<int> l(n);
    int k = 0;
    for (int i = 0; i < n; i++) {
        int x = c[i];
        if (!x) {
            continue;
        }
        if (k > 0) {
            k -= 1;
        }
        while (s[p[x - 1] + k] == s[p[x] + k]) {
            k += 1;
        }
        l[x - 1] = k;
    }
    
    int m;
    cin >> m;
    while (m) {
        int a, b;
        scanf(" %d %d ", &a, &b);
        if (a == b) {
            printf("%d\n", n - a - 1);
        } else {
            int pos_a = min(c[a], c[b]);
            int pos_b = max(c[a], c[b]);
            int min_l = *min_element(l.begin() + pos_a, l.begin() + pos_b);
            printf("%d\n", min_l);
        }
        m -= 1;
    }
    return 0;
}