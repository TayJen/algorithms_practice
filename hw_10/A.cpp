#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n = 0;
  cin >> n;

  vector<vector<int>> paths(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> paths[i][j];
    }
  }

  vector<vector<int>> dp(n, vector<int>(1 << n));
  vector<vector<int>> prev(n, vector<int>(1 << n));
  for (int i = 0; i < n; i++) {
    dp[i][1] = 0;
  }

  for (int mask = 1; mask < (1 << n); mask++) {
    for (int u = 0; u < n; u++) {
      if (mask & (1 << u) == 0) {
        continue;
      }
      for (int v = 0; v < n; v++) {
        if (u != v && mask & (1 << v) != 0) {
          if (dp[v][mask ^ (1 << u)] + paths[v][u] < dp[u][mask]) {
            dp[u][mask] = dp[v][mask ^ (1 << u)] + paths[v][u];
            prev[u][mask] = v;
          }
        }
      }
    }
  }

  int min_path = INT_MAX;
  for (int u = 0; u < n; u++) {
    min_path = min(min_path, dp[u][(1 << n) - 1]);
  }
  cout << min_path << endl;

  vector<int> path;
  int mask = (1 << n) - 1;
  int u = 0;
  for (int i = 0; i < n; i++) {
    if (dp[u][mask] == INT_MAX) {
      break;
    }
    path.push_back(u);
    mask ^= (1 << u);
    u = prev[u][mask];
  }
//   int u = min(range(n), key=lambda x: dp[x][(1 << n) - 1]);
//   while (mask > 0) {
//     path.push_back(u);
//     v = prev[u][mask];
//     mask ^= (1 << u);
//     u = v;
//   }

  for (int i = path.size() - 1; i >= 0; i--) {
    cout << path[i] + 1 << " ";
  }
  cout << endl;

  return 0;
}