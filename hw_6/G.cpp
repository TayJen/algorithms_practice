#include <iostream>
#include <vector>

int N;
std::vector<std::vector<std::vector<int>>> arr;

int prefix_sum(int x, int y, int z) {
    int res = 0;
    int x0 = x;
    while (x0 >= 0) {
        int y0 = y;
        while (y0 >= 0) {
            int z0 = z;
            while (z0 >= 0) {
                res += arr[x0][y0][z0];
                z0 = (z0 & (z0 + 1)) - 1;
            }
            y0 = (y0 & (y0 + 1)) - 1;
        }
        x0 = (x0 & (x0 + 1)) - 1;
    }
    return res;
}

int range_sum(int x1, int y1, int z1, int x2, int y2, int z2) {
    return prefix_sum(x2, y2, z2) - prefix_sum(x1 - 1, y2, z2) - prefix_sum(x2, y1 - 1, z2) - prefix_sum(x2, y2, z1 - 1) + prefix_sum(x1 - 1, y1 - 1, z2) + prefix_sum(x1 - 1, y2, z1 - 1) + prefix_sum(x2, y1 - 1, z1 - 1) - prefix_sum(x1 - 1, y1 - 1, z1 - 1);
}

void update(int x, int y, int z, int delta) {
    int x0 = x;
    while (x0 < N) {
        int y0 = y;
        while (y0 < N) {
            int z0 = z;
            while (z0 < N) {
                arr[x0][y0][z0] += delta;
                z0 = (z0 | (z0 + 1));
            }
            y0 = (y0 | (y0 + 1));
        }
        x0 = (x0 | (x0 + 1));
    }
}

int main() {
    std::cin >> N;
    arr.resize(N, std::vector<std::vector<int>>(N, std::vector<int>(N, 0)));

    while (true) {
        int oper;
        std::cin >> oper;

        if (oper == 1) {
            int x, y, z, val;
            std::cin >> x >> y >> z >> val;
            update(x, y, z, val);
        } else if (oper == 2) {
            int x1, y1, z1, x2, y2, z2;
            std::cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
            std::cout << range_sum(x1, y1, z1, x2, y2, z2) << std::endl;
        } else if (oper == 3) {
            break;
        }
    }

    return 0;
}