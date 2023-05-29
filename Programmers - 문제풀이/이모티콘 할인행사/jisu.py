"""
15:55 -> 16:23 (28분 소요)

우선순위
- 1. 서비스 가입자 최대
- 2. 이모티콘 판매액 최대

핵심 조건
- 사용자는 자기 기준 비율보다 더 할인하는 이모티콘을 구매한다.
- 그렇게 구매한 이모티콘 가격의 합이 자기 기준 가격보다 높으면 이모티콘 플러스에 가입한다.

접근 방법
- 이모티콘마다 할인율(10, 20, 30, 40)이 다르다 -> 다르게 주어지는 건 할인율 뿐이다.
- 각 이모티콘에 모든 할인율을 적용해보고 거기서 목적을 최대한 달성했을 때의 경우의 수를 찾자 (완전탐색)
"""

from itertools import product

def solution(users, emoticons):
    discount_rates_list = [10, 20, 30, 40]  # 할인율 리스트
    num_of_emoticons = len(emoticons)       # 이모티콘 수

    answer_list = []    # 아래 경우의 수 마다의 최종 결과(가입자 수, 구매 이모티콘 가격)를 담을 리스트

    # 이모티콘 갯수 만큼 할인율 리스트를 cartesian product 해서 모든 이모티콘에 특정 할인율을 적용하는 모든 경우의 수를 순회
    for discount_rates in product(*[discount_rates_list for _ in range(num_of_emoticons)]):     # 만약 이모티콘이 3개이면 (10, 10, 10) -> (20, 10, 10) -> (30, 10, 10) -> ... (40, 40, 40)
        total_users_of_emoticon_plus = 0            # 이모티콘에 특정 할인율을 적용했을 떄의 결과 (가입자 수, 구매 이모티콘 가격)
        total_count_of_emoticon_purchase = 0

        for user_rate, user_price in users:
            purchase_count = 0
            for discount_rate, emoticon in zip(discount_rates, emoticons):              # 이모티콘 할인율과 이모티콘 가격을 묶어서 순회 ex) (10, 7000)
                if discount_rate >= user_rate:                                          # 할인율이 유저 기준 비율 이상이라면
                    purchase_count += int(emoticon - emoticon * discount_rate / 100)    # 해당 유저는 구매하므로, purchase_count에 더해 줌 (핵심 조건 1)
            
            if purchase_count >= user_price:                                            # 총 이모티콘 구매 가격이 유저 기준 가격 이상이라면 
                total_users_of_emoticon_plus += 1                                       # 유저는 이모티콘을 구매하지 않고 이모티콘 플러스에 가입함 (핵심 조건 2)
            else:
                total_count_of_emoticon_purchase += purchase_count

        answer_list.append((total_users_of_emoticon_plus, total_count_of_emoticon_purchase))    # 특정 할인율을 적용했을 때의 결과를 최종 리스트에 append

    answer_list.sort(key=lambda x : (x[0], x[1]), reverse=True) # 특정 할인율을 적용하는 모든 경우의 수에 대한 결과가 담겨있음, 우선순위에 맞게 정렬(내림차순)

    return answer_list[0]   # 첫 번째 원소는 우선 순위를 만족하는 결과이다


case1 = [[[40, 10000], [25, 10000]], [7000, 9000]] # [1, 5400]
case2 = [[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]] # [4, 13860]

print(solution(*case1)) # [1, 5400]
print(solution(*case2)) # [4, 13860]