def solution(A):
    result = 0

    for i in A:
        result ^= i

    return result

#--- Ref ---
# Use XOR bitwise operator to detect overlapping values
# https://codesays.com/2015/solution-to-odd-occurrences-in-array-by-codility/

if __name__ == '__main__':
    print("[5] : " ,solution([5]))
    print("[5, 6, 7, 1, 7, 6, 5] : " ,solution([5, 6, 7, 1, 7, 6, 5]))
    print("[9, 3, 9, 3, 9, 7, 9] : " ,solution([9, 3, 9, 3, 9, 7, 9]))
