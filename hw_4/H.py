import sys

class Heap():
    def __init__(self):
        self.heap = []
        self.curr_length = 0

    def add(self, val: int):
        self.curr_length += 1
        self.heap.append(val)

        # sift up
        idx = self.curr_length - 1
        while idx > 0:
            idx_parent = (idx-1) // 2
            if self.heap[idx] > self.heap[idx_parent]:
                self.heap[idx], self.heap[idx_parent] = self.heap[idx_parent], self.heap[idx]
                idx = idx_parent
            else:
                break
    
    def extract_max(self) -> int:
        self.curr_length -= 1
        max_val = self.heap[0]
        last_val = self.heap.pop()
        
        if not self.heap:
            return max_val

        self.heap[0] = last_val

        idx = 0
        while 2*idx + 1 < self.curr_length:
            idx_first = 2*idx + 1
            idx_second = 2*idx + 2
            if idx_second == self.curr_length or self.heap[idx_first] > self.heap[idx_second]:
                idx_max = idx_first
            else:
                idx_max = idx_second

            if self.heap[idx] < self.heap[idx_max]:
                self.heap[idx], self.heap[idx_max] = self.heap[idx_max], self.heap[idx]
                idx = idx_max
            else:
                break

        return max_val



n = int(input())
heap = Heap()
for oper in sys.stdin.readlines():
    if oper[0] == '0':
        heap.add(int(oper.split(' ')[1]))
    else:
        print(heap.extract_max())

    # print(heap.heap)