#include <iostream>
#include <string>

using namespace std;

int find_max(int i, int j, string s) {
    if (i >= j) {
        return 0;
    }
    if (s[i] == '(' && s[j] == ')' || s[i] == '[' && s[j] == ']' || s[i] == '{' && s[j] == '}') {
        return 2 + find_max(i + 1, j - 1, s);
    }
    if (s[i] != s[j]) {
        return max(find_max(i + 1, j, s), find_max(i, j - 1, s));
    }
    return 0;
}

int main() {
    string s;
    cin >> s;
    int start = 0;
    int end = s.length() - 1;
    cout << find_max(start, end, s) << endl;
    return 0;
}