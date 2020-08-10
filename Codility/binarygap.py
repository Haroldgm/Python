# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    bin_string = list(str(bin(N)[2:]))
    bin_array = [int(d) for d in bin_string]
    print(bin_array)
    indices = []
    gap = 0

    #Record the indices of 1's 
    for i in range(0, len(bin_array)):
        if bin_array[i] == 1:
            indices.append(i)

    print(indices)

    #Evaluate the indices' distance
    if len(indices) < len (bin_array):
        max_diff = 1
        for i in range(0, len(indices)-1):
            diff = indices[i + 1] - indices[i]
            if diff > max_diff:
                max_diff = diff - 1
                gap = diff - 1

    return gap

if __name__ == '__main__':
    print(solution(20))