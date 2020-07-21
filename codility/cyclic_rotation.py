def solution(A, K):
    if (len(set(A))==1):
        return A
    if (len(A)==K):
        return A
    if (A == []):
        return A

    times = K % len(A)
    B = [None] * len(A)
    for i in range(0, len(A)):
        if (i+times) >= len(A) :
            B[i+times-len(A)] = A[i]
        else:
            B[i+times] = A[i]
    return B    

if __name__ == '__main__':
    print("[3, 8, 9, 7, 6], 3  : " ,solution([3, 8, 9, 7, 6], 3)) #[9, 7, 6, 3, 8]
    print("[5, 6, 7, 1, 2, 3, 4], 6  : " ,solution([5, 6, 7, 1, 2, 3, 4], 6)) #[6, 7, 1, 2, 3, 4, 5]
    print("[3, 8, 9, 7, 6], 8  : " ,solution([3, 8, 9, 7, 6], 8))
    print("[], 8  : " ,solution([], 8))
    print("[""], 8  : " ,solution([], 8))
