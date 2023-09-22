
def bubblesort():
    for a in range(n, 0, -1):
        for i in range(0, a-1):
            if List[i] > List[i+1]:
                temp = List[i]
                List[i] = List[i+1]
                List[i+1] = temp

List = [-4, 999, 45, 21, 66, 879, 5453, -9, 24.3, 42.011, 53252, 535, 53, 42, 426, 832, 132]
n = len(List)
bubblesort()
print(List)
