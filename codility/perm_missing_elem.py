def solution(A):
    N = len(A) + 1

    return ( N * (N+1) //2 ) - sum(A)

if __name__ == '__main__':
    print("[1] : " ,solution([1]))
    print("[2, 3, 1, 5] : " ,solution([2, 3, 1, 5]))
    print("[2, 0, 4, 1] : " ,solution([2, 0, 4, 1]))