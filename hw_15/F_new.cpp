#include <iostream>
using namespace std;

const int N = 2 * 1000000;
int prime_set[N];

void sieve() {
    prime_set[0] = prime_set[1] = 0;
    for (int i = 2; i < N; i++) {
        prime_set[i] = 1;
    }
    for (int i = 2; i * i < N; i++) {
        if (prime_set[i]) {
            for (int j = i * i; j < N; j += i) {
                prime_set[j] = 0;
            }
        }
    }
}

int main() {
    int m;
    cin >> m;
    sieve();
    while (m) {
        int n;
        cin >> n;
        if (prime_set[n]) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
        m--;
    }
    return 0;
}
