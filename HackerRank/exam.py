def f(arr):
    i = 0
    s = 0
    while i < len(arr):
        s = s + arr[i]
        i = i + 1

    return s

if __name__ == '__main__':
    array = [5, 7, 8, 3]
    print(f(array))
