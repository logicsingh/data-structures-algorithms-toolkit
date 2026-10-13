def bubble_sort(items):
    """Bubble sort copy. O(n^2) worst case; O(n) best case."""
    a=list(items)
    for end in range(len(a)-1,0,-1):
        changed=False
        for i in range(end):
            if a[i] > a[i+1]: a[i],a[i+1]=a[i+1],a[i]; changed=True
        if not changed: break
    return a

def selection_sort(items):
    """Selection sort copy. O(n^2) time."""
    a=list(items)
    for start in range(len(a)):
        m=start
        for i in range(start+1,len(a)):
            if a[i] < a[m]: m=i
        a[start],a[m]=a[m],a[start]
    return a

def insertion_sort(items):
    """Insertion sort copy. O(n^2) worst case; O(n) best case."""
    a=list(items)
    for i in range(1,len(a)):
        value=a[i]; j=i-1
        while j>=0 and a[j]>value: a[j+1]=a[j]; j-=1
        a[j+1]=value
    return a

def merge_sort(items):
    """Merge sort copy. O(n log n) time and O(n) extra space."""
    a=list(items)
    if len(a)<=1: return a
    mid=len(a)//2
    return _merge(merge_sort(a[:mid]),merge_sort(a[mid:]))

def _merge(left,right):
    out=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: out.append(left[i]); i+=1
        else: out.append(right[j]); j+=1
    return out+left[i:]+right[j:]
