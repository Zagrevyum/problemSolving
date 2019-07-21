class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        mergedList = temp =ListNode(0)
        heap = []
        k = len(lists)
        for index in range(k):
            if lists[index] is not None and len(heap) < k:
                #print("appending", lists[index].val)
                heap.append(lists[index].val)
                lists[index] = lists[index].next
            if index < k and lists[index] is None:
                del lists[index]
                k -= 1

        while(heap and lists):
            print(heap)
            temp.next, heap, indextoadd = self.getMin(heap)
            temp = temp.next
            print("adding", temp.val, "from list", indextoadd)
            if lists[indextoadd] is not None:
                print("inserting from index", lists[indextoadd].val, indextoadd)
                heap.insert(indextoadd, lists[indextoadd].val)
                lists[indextoadd] = lists[indextoadd].next
                continue
            del lists[indextoadd]
            for index in range(k):
                if lists[index] is not None and len(heap) < k:
                        print("appending", lists[index].val, index)
                        heap.append(lists[index].val)
                        lists[index] = lists[index].next
                        continue
        return mergedList

    def getMin(self, numberslist):
        min = numberslist[0]
        indextopop = 0
        for index in range(len(numberslist)):
            if numberslist[index] < min:
                min = numberslist[index]
                indextopop = index
        numberslist.pop(indextopop)
        return ListNode(min), numberslist, indextopop

"""
Input
[[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]]
Output
[-10,-8,-8,-8,-6,-6,-6,-5,-4,-4,-3,-3,-3,-2,-2,-2,-2,-1,-1,1,1,2,2,-2,2,2,2,3,4,4]
Expected
[-10,-8,-8,-8,-6,-6,-6,-5,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-1,-1,1,1,2,2,2,2,2,3,4,4]
"""
lists = [ListNode(0), ListNode(0), ListNode(0)]
_lists = []
for l in lists:
    _l = l
    for i in range(1,10):
        l.next = ListNode(i)
        l = l.next
        #print(l.val)
    _lists.append(_l)
solved = Solution()

_test = _lists
for a in lists:
    while a:
        print(a.val)
        a = a.next


result = solved.mergeKLists(_lists)
result = result.next
while result:
    print(result.val)
    result = result.next

