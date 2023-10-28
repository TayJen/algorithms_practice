#include <iostream>
using namespace std;

const int N = 5005;

int n, m, a[N], b[N];
int f[N][N], pre[N][N];

int main()
{
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> a[i];

    cin >> m;
    for (int j = 1; j <= m; ++j)
        cin >> b[j];

    // O(n^2) solution
    for (int i = 1; i <= n; ++i)
    {
        int fmax = 0, pos = 0;
        for (int j = 1; j <= m; j++)
        {
            f[i][j] = f[i - 1][j];     // Exclude a[i] from LCIS
            pre[i][j] = pre[i-1][j];
            if (a[i] == b[j])
            {   // Add a[i] to LCIS
            // fmax is the maximum value of the O(n^3) solution f[i-1][k]+1
                if (f[i][j] < fmax + 1) 
                {
                    f[i][j] = fmax + 1;
                    // Prepare for the output path, record the index of the 
                    // previous element of the LCIS ending with b[j] among the
                    // first j elements of b, which is also an element of the 
                    // first i elements of a.
                    pre[i][j] = pos;  
                }
            }
            if (b[j] < a[i])
            {
                if (f[i - 1][j] > fmax)
                {
                // fmax is the maximum value of the O(n^3) solution f[i-1][k]+1
                    fmax = f[i - 1][j]; 
                    pos = j;
                }
            }
        }
    }

    int res = 0, last = 0, tot = 0, path[N];

    // Looking for the length of LCIS and the position of the end of LCIS
    for (int j = 1; j <= m; ++j) 
    { 
        if (res < f[n][j])
        {
            res = f[n][j];
            last = j;
        }
    }

    cout << res << endl;

    int i = n, j = last;
    // Using the pre-array, find the entire sequence step by step based on
    // the last element of LCIS
    while (i || j) 
    {
        if (pre[i][j] != j)
            path[++tot] = b[j];
        j = pre[i][j];
        i--;
    }

    while (tot)
        cout << path[tot--] << ' ';
    cout << endl;

    return 0;
}