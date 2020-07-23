def solution(A):
    s = sum(A)
    left_sum = 0
    m = float('inf')
    for i in A[:-1]:
        left_sum += i
        m = min( abs(s - 2*left_sum), m)
    return m

if __name__ == '__main__':
    print("[3, 1, 2, 4, 3] : " ,solution([3, 1, 2, 4, 3]))