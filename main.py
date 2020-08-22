a = [0, 1,2,3,4,5,6,7,8,9]

start, end = 0, 3
count = len(a)
while True:
    if end < count:
        print(a[start: end])
    else:
        print(a[start: count])
        break
    start += 3
    end += 3
