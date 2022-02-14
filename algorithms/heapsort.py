'''
max heap = parent > children (ascending order)
min heap = parent <= children (descending order)
'''

'''
swap: swap at indices i and j in the list, more concise than verbose swap syntax
'''
def swap(lst, i, j): 
    lst[i], lst[j] = lst[j], lst[i]

'''
 sift_down: helps to initially heapify the list, sift down element that swaps with larger element of its children nodes, 
 sift down happens after swapping root with last node in the tree 
 upper = upper bound of list that we conisder as heap 
 (somewhere between 0 and end of list, 0 to end of unsorted part of list)
'''
def sift_down(lst, i, upper): 
    while True: # choosing loop over recursion bc in a large list, recu will throw error once it reaches a certain limit
        left, right = i*2+1, i*2+2 # i = current parent index  
        if max(left, right) < upper:
            if lst[i] >= max(lst[left], lst[right]): break
            elif lst[left] > lst[right]:
                swap(lst, i, left)
                i = left # update parent index, left child becomes new parent 
            else:
                swap(lst, i, right)
                i = right # update parent index, right child becomes new parent 
        elif left < upper:
            if lst[left] > lst[i]:
                swap(lst, i, left)
                i = left
            else: break
        elif right < upper:
            if lst[right] > lst[i]:
                swap(lst, i, right)
                i = right 
            else:
                break 
        else: break # no children, no swapping or sifting down that takes place, so do nothing 

def heapsort(lst): # sort list in place, review again 
    '''
    heapify into max heap 
    (len(lst)-2)//2 = index of last parent node in heap
    end at -1 and decrement by one 
    '''
    for j in range((len(lst)-2)//2, -1, -1): 
        sift_down(lst, j, len(lst)) 

    '''
    stop at 0 bc when we get to 0, everything is already sorted, including that first element 
    '''
    for end in range(len(lst)-1, 0, -1): # sort (swap root with element at end of list after heapifying)
        swap(lst, 0, end)
        sift_down(lst, 0, end)

lst = [45,78,90,1,2,3,44,3]
heapsort(lst)
print(lst)