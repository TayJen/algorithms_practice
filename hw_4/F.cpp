#include <iostream>

class Node {
public:
    int val;
    Node* next_node;
    Node* previous_node;
    
    Node(int val) {
        this->val = val;
        this->next_node = nullptr;
        this->previous_node = nullptr;
    }
};

class MiddleQueue {
public:
    Node* head;
    Node* middle;
    Node* tail;
    int overall_length;
    
    MiddleQueue() {
        this->head = nullptr;
        this->middle = nullptr;
        this->tail = nullptr;
        this->overall_length = 0;
    }
    
    void push(int val) {
        this->overall_length += 1;
        if (this->overall_length == 1) {
            this->first_push(val);
        } else {
            Node* new_node = new Node(val);
            new_node->next_node = this->tail;
            this->tail->previous_node = new_node;
            this->tail = new_node;
        }
        if (this->overall_length % 2 == 1 && this->middle->previous_node != nullptr) {
            this->middle = this->middle->previous_node;
        }
    }
    
    int pull() {
        this->overall_length -= 1;
        int val = this->head->val;
        if (this->overall_length) {
            this->head = this->head->previous_node;
            this->head->next_node = nullptr;
            if (this->overall_length % 2 == 1 && this->middle->previous_node != nullptr) {
                this->middle = this->middle->previous_node;
            }
        } else {
            this->head = nullptr;
            this->middle = nullptr;
            this->tail = nullptr;
        }
        return val;
    }
    
    void first_push(int val) {
        this->tail = this->middle = this->head = new Node(val);
    }
    
    void push_middle(int val) {
        this->overall_length += 1;
        if (this->overall_length == 1) {
            this->first_push(val);
        } else {
            Node* new_node = new Node(val);
            new_node->next_node = middle;
            new_node->previous_node = middle->previous_node;
            if (this->middle->previous_node != nullptr) {
                this->middle->previous_node->next_node = new_node;
            }
            this-> middle->previous_node = new_node;
            if (this->tail == this->middle) {
                tail = new_node;
            }

            if (this->overall_length % 2 == 1) {
                middle = new_node;
            }
        }
    }
};

int main() {
    int n;
    std::cin >> n;
    MiddleQueue q;
    std::string oper;
    for (int i = 0; i < n; i++) {
        std::cin >> oper;
        if (oper[0] == '+') {
            int val;
            std::cin >> val;
            q.push(val);
        } else if (oper[0] == '*') {
            int val;
            std::cin >> val;
            q.push_middle(val);
        } else if (oper[0] == '-') {
            std::cout << q.pull() << std::endl;
        }
    }
    return 0;
}