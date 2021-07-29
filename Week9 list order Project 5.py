def isSorted(list_Element):
    for x in range(len(list_Element) - 1):
        if(list_Element[x] > list_Element[x + 1]):
            return False
    return True

def main():
    list_Element = []
    print(isSorted(list_Element))
    list_Element = [1]
    print(isSorted(list_Element))
    list_Element = list(range(10))
    print(isSorted(list_Element))
    list_Element[9] = 3
    print(isSorted(list_Element))

main()
