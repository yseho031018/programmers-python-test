# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 
# 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000

def solution(array):
    count = [0] * (len(array)+1)

    for i in array:
        count[i] += 1

    m = 0
    for j in count:
        if m == max(count):
            m += 1

    if m > 1:
        return -1
    else:
        return count.index(max(count))

print(solution([1, 5, 3, 2, 1, 1, 3, 5, 2, 2]))