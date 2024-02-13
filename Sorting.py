from random import randint, seed
import sys
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")


    def selection_sort(self):
        """Implements selection sort"""
        for i in range(self.size):
            #assume array is sorted and self.arr[i], i are the min and min_index            
            min = self.arr[i]
            min_index = i

            #check if they are the min and min_index
            for j in range(i, self.size):
                if self.arr[j] < min:
                    min = self.arr[j]
                    min_index = j

            #move min and min_index to sorted portion of array if they change
            if i != min_index:
                temp = self.arr[i]
                self.arr[i] = min
                self.arr[min_index] = temp

    def max_heapify(self, n, i):
        """Implements Heapify for array"""

        # Will rearrange self.arr into a max heap by sinking nodes in reverse level order
        subroot_index = i
        l = (2 * i) + 1
        r = (2 * i) + 2

        if l < n and self.arr[l] > self.arr[subroot_index]:
            subroot_index = l

        if r < n and self.arr[r] > self.arr[subroot_index]:
            subroot_index = r

        if subroot_index != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[subroot_index]
            self.arr[subroot_index] = temp

            # maintain max heap
            self.max_heapify(n, subroot_index)
        
    def heap_sort(self):
        """Implements Heap sort"""

        #bottom up heapification starting node -> last subheap in the list
        N = (self.size // 2) - 1    

        for i in range(N, -1, -1):
            self.max_heapify(self.size, i)

        # Sort max heap
        for i in range(self.size-1, -1, -1):

            #Move root to sorted portion
            temp = self.arr[0]
            self.arr[0] = self.arr[i]
            self.arr[i] = temp

            # maintain max heap
            self.max_heapify(i, 0)

    def merge_sort(self):
        self.arr = self._merge_sort(self.arr)
        # print(self.arr)

    def _merge_sort(self, S): 
        """Implements Merge sort"""
        # input: sequence S with n elements
        # output: Sequence S sorted according to C

        if len(S) > 1:

            # Midpoint, left and right sub arrays 
            index = len(S) // 2
            s1 = S[:index]
            s2 = S[index:]
            self._merge_sort(s1)
            self._merge_sort(s2)

            i = 0
            j = 0
            k = 0
            while i < len(s1) and j < len(s2): 
                # Left is less than right, increment i
                if s1[i] <= s2[j]:
                    S[k] = s1[i]
                    i+=1
                # Right is less than left, increment j
                else: 
                    S[k] = s2[j]
                    j+=1
                #increment sorted array counter in either case 
                k+=1

            # If the array was an odd number
            while i < len(s1):
                S[k] = s1[i]
                i+=1
                k+=1
            while j < len(s2):
                S[k] = s2[j]
                j+=1
                k+=1
        return S
        
    def test_sorting_time(self, sorting_method):


        if sorting_method == 'selection':
            start = time.time()
            self.selection_sort()
            finish = time.time()

            return finish - start
        
        elif sorting_method == 'heap':
            start = time.time()
            self.heap_sort()
            finish = time.time()

            return finish - start
        
        elif sorting_method == 'merge':
            start = time.time()
            self.merge_sort()
            finish = time.time()

            return finish - start

#Test Sorted array
def is_sorted(arr):
    if arr == sorted(arr):
        print("Passed!")
        return True
    else:
        print("Failed!")
        return False

# Test each sirting technique
def test_sort_algorithms(sorting_method, set_seed=None):
    if seed != None:
        seed(set_seed)
    sorting = Sorting(10)
    # Add 10 random elements
    for _ in range(10):
        sorting.add(randint(1, 100))
    # Apply the sorting algorithm
    if sorting_method == 'selection':
        sorting.selection_sort()
        print("Selection Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'heap':
        sorting.heap_sort()
        print("Heap Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'merge':
        sorting.merge_sort()
        print("Merge Sort:", is_sorted(sorting.arr))
        
#Test run time
def run_time_tests():
    seeding = 45
    array_sizes = [10000,20000,30000,40000,50000]
    methods = ['selection', 'heap', 'merge']

    print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    for size in array_sizes: 
        times = []
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            for _ in range(size):
                sorting.add(randint(1, 50000))

            interval = sorting.test_sorting_time(m)
            times.append(interval)

        print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")
        
#test case execution
if __name__ == "__main__":
    seed_num = 43   
    test_sort_algorithms('selection', seed_num)
    test_sort_algorithms('heap', seed_num)
    test_sort_algorithms('merge', seed_num)
    run_time_tests()
