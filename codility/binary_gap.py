def solution(N):
    s = bin(N)[2:].split('1') #"{0:b}".format(N) 
    if N == 1:
        return 0
    if s.count('1') == len(s):
        return 0
    if (s[0]=='') & (s[len(s)-1] == ''):
        return max(map(lambda x: x.count('0'),s[1:len(s)-1]))
    if (s[0]=='') & (len(s) > 2):
        return max(map(lambda x: x.count('0'),s[1:len(s)-1]))
    return 0

if __name__ == "__main__":
    #int('1000010001',2)
    print("529, 1000010001 : " , solution(529))
    print("1041, 1000010001 : " , solution(1041))
    print("20, 10100 : " , solution(20))
    print("32, 100000 : " , solution(32))
    print("15, 1111 : " , solution(15))
    print("3, 11 : " , solution(3))
    print("1, 1 : " , solution(1))