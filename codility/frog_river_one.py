def solution(X, A):
    d = {}
    total = sum(range(1,X+1))

    if X == 1 : return 0

    for i, v in enumerate(A):
        if v not in d:
            d[v] = 1
            total -= v
            if total == 0 :
                return i

    return -1

if __name__ == '__main__':
    print(" 5, [1, 3, 1, 4, 2, 3, 5, 4] : " ,solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
    print(" 1, [1] : " ,solution(1, [1]))
