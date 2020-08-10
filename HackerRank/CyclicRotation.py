def solution(A, K):
    if K > 0:
        if K >= len(A):
            K = K - len(A)

            if K % len(A) == 0:
                K = int(K / len(A))

    
        w1 = A[K-1:]
        w2 = A[:K-1]  
        print(w1+w2)

    else:
        print(A)
        
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    print(A)
    K = 2
    solution(A,K)