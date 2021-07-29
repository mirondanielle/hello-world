def mean(data):
    total = 0
    numbers = len(data)
    if(numbers == 0):
        return(0)
    for item in data:
        total = total + item
    av = total / (numbers)
    return (av)

def median(data):
    numbers = len(data)
    if(numbers == 0):
        return(0)
    data.sort()
    even = True
    if len(data)%2 == 1:
        even = False
    if even:
        slice_start = (len(data)//2) - 1
        slice_end   = (len(data)//2) + 1
        me = sum(data[slice_start:slice_end]) / 2
    else:
        me  = data[len(data)//2]
    return (me)

def mode(data):
    numbers = len(data)
    if(numbers == 0):
        return(0)
    compare = []
    for item in data:
        count = data.count(item)
        values = (count, item)
        if values not in compare:
           compare.append(values)
    compare.sort(reverse=True)
    if compare[0][0]>compare[1][0]:
        return(compare[0][1])
    else:
        return(None)

if __name__ == "__main__":
    data = [2, 5, 6, 8, 9, 4, 2]
    print("The mean is:", mean(data))
    print("The median is:", median(data))
    print("The mode is:", mode(data))

