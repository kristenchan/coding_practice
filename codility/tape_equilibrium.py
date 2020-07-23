def solution(A):
    total = sum(A)
    result = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i

        result = min( abs(total - 2*left_sum) , result)

    return result

if __name__ == '__main__':
    print("[3, 1, 2, 4, 3] : " ,solution([3, 1, 2, 4, 3]))