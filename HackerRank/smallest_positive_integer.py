# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# this solution will return the smallest positive integer that is within the range of the values in the list
def solution(A):
    #ensure that the array elements are within the limits
    if len(A) > 0 and len(A) <= 100000:
        print(A)
        A.sort()
        print(A)
        num = 1
        for i in range(0, len(A)):
            if num == A[i]:
                num += 1
        print(num)


if __name__ == '__main__':
    A = [9, -3, 1, 2, 3, 4, 5, -2]
    solution(A)