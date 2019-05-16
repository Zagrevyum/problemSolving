
class Sort():

    def bubblesort(self, array):
        lastSorted = len(array)
        iterations = 0

        for i in range(0, len(array)):
            swaps = True
            for j in range(0, lastSorted-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swaps = False
                iterations += 1
            if swaps:
                break
            lastSorted -= 1
        print (iterations, len(array))
        return array




solution = Sort()

print(solution.bubblesort([8,1,3,5,1,6,2,1,3,4,5]))


# 1 1 2 3 3 4 5 5