# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을
# return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ num_list의 길이 ≤ 100
# 0 ≤ num_list의 원소 ≤ 1,000

def solution(num_list):

    odd = 0
    even = 0

    for i in num_list:
        if i % 2 == 0:
            odd += 1
        else:
            even += 1


    return [odd, even]


print(solution([4, 3, 2, 1, 5, 2, 2, 7, 2, 8]))