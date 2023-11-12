#include <iostream>
#include <vector>
#include <random>
#include <ctime>

struct ImplicitTreap {
    int x;
    int y;
    ImplicitTreap* left;
    ImplicitTreap* right;
    int size;
    bool reversed;

    ImplicitTreap(int x, ImplicitTreap* left = nullptr, ImplicitTreap* right = nullptr) {
        this->x = x;
        this->y = rand();
        this->left = left;
        this->right = right;
        this->size = 1;
        this->reversed = false;
    }
};

int get_size(ImplicitTreap* T) {
    if (T == nullptr) {
        return 0;
    } else {
        return T->size;
    }
}

void recalc(ImplicitTreap* T) {
    if (T != nullptr) {
        T->size = get_size(T->left) + get_size(T->right) + 1;
    }
}

void push(ImplicitTreap* T) {
    if (T == nullptr) {
        return;
    }
    if (!T->reversed) {
        return;
    }
    T->reversed = false;
    std::swap(T->left, T->right);
    if (T->left != nullptr) {
        T->left->reversed ^= true;
    }
    if (T->right != nullptr) {
        T->right->reversed ^= true;
    }
}

ImplicitTreap* merge(ImplicitTreap* L, ImplicitTreap* R) {
    push(L);
    push(R);
    if (L == nullptr) {
        return R;
    }
    if (R == nullptr) {
        return L;
    }
    if (L->y > R->y) {
        L->right = merge(L->right, R);
        recalc(L);
        return L;
    } else {
        R->left = merge(L, R->left);
        recalc(R);
        return R;
    }
}

std::pair<ImplicitTreap*, ImplicitTreap*> split(ImplicitTreap* T, int x0) {
    push(T);
    if (T == nullptr) {
        return {nullptr, nullptr};
    }
    if (get_size(T->left) < x0) {
        auto [L, R] = split(T->right, x0 - get_size(T->left) - 1);
        T->right = L;
        recalc(T);
        return {T, R};
    } else {
        auto [L, R] = split(T->left, x0);
        T->left = R;
        recalc(T);
        return {L, T};
    }
}

ImplicitTreap* reverse(ImplicitTreap* T, int A, int B) {
    auto [L, R] = split(T, A - 1);
    auto [M, R2] = split(R, B - A + 1);
    M->reversed ^= true;
    return merge(merge(L, M), R2);
}

void print_tree(ImplicitTreap* T) {
    if (T == nullptr) {
        return;
    }
    push(T);
    print_tree(T->left);
    std::cout << T->x << " ";
    print_tree(T->right);
}

ImplicitTreap* from_list(const std::vector<int>& arr) {
    ImplicitTreap* result = nullptr;
    for (int val : arr) {
        result = merge(result, new ImplicitTreap(val));
    }
    return result;
}

int main() {
    srand(time(nullptr));

    int n, m;
    std::cin >> n >> m;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = i + 1;
    }

    ImplicitTreap* main_T = from_list(arr);

    while (m--) {
        int a, b;
        std::cin >> a >> b;
        main_T = reverse(main_T, a, b);
    }

    print_tree(main_T);

    return 0;
}