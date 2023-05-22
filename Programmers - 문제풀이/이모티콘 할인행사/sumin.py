"""
시간: 50분(주석까지)
브루트포스 구현 문제

<input>
- users: 1 ≤ len(users) = n ≤ 100, [비율, 가격] 형태
- emoticons: 1 ≤ len(emoticons) = m ≤ 7

<solution>
1. 이모티콘 할인율은 무조건 [10%, 20%, 30%, 40%] 중 하나이고 이모티콘은 최대 7개가 올 수 있기 때문에 모든 경우의 수를 계산해도 4^7 = 16,384가지 밖에 되지 않는다.
2. 마찬가지로 모든 user에 대해 확인한다해도 user는 최대 100명이기 때문에 모든 사용자에 대해 이모티콘 구매비용을 확인하고, 서비스에 가입할지 안할지 여부를 확인할 수 있다.
3. 구현
- 3-1) 모든 이모티콘에 대해 할인율을 결정한다. (중복순열 product 사용, 재귀로 가능)
- 3-2) 사용자를 한명씩 순회하며 각 사용자가 할인된 이모티콘을 구매할지, 구매한다면 구매비용으로 얼마를 쓰는지, 구매비용이 자신의 기준 비용을 초과해 서비스에 가입하는지를 확인한다.
- 3-3) 3-1에서 정한 할인율에 대해 n명의 사용자를 모두 확인한 후의 서비스 가입자 수와 매출액이 이전까지와 비교했을 때 목적을 극대화할 수 있는지 확인하고, 가능하다면 정답을 갱신해준다.

-> 시간복잡도: O(4^N * N * M)
"""
from itertools import product


def solution(users, emoticons):
    answer = [0, 0]  # 서비스 가입 수, 매출액 최대값
    discount = [10, 20, 30, 40]  # 할인율
    n, m = len(users), len(emoticons)  # 사용자수, 이모티콘 수
    join_cnt = 0  # 이모티콘 플러스 서비스 가입 수
    revenue = 0  # 매출액
    for permu in product(discount, repeat=m):  # O(4^m) -> 최대 4^7
        join, sales = 0, 0  # permu로 할인율을 적용했을 때 발생하는 서비스 가입자 수, 이모티콘 판매액
        for per, price in users:  # n명의 모든 유저에 대해 확인해야함(per: 비율, price: 가격)
            tot = 0  # 이모티콘 구매비용
            for i in range(m):  # m개의 이모티콘
                # i번째 이모티콘에 대한 할인율(permu[i])가 현재 확인하고 있는 유저의 기준 이상이라면
                if permu[i] >= per:
                    # 할인하는 이모티콘을 모두 구매
                    tot += emoticons[i] * (100 - permu[i]) * 0.01
            if tot >= price:  # 이모티콘 총 구매비용이 사용자의 기준 가격 이상이라면
                # 이모티콘 구매를 모두 취소하고 이모티콘 구매 서비스에 가입
                join += 1  # 서비스 가입
            else:  # 기준 미달이라면 매출액에 구매비용을 더해줌
                sales += tot
            # print(f"{permu}일 때: {join}명 가입, {sales}원 판매")

        # 현재 설정한 이모티콘 할인율이 목적(서비스 가입자수, 매출액)을 극대화할 수 있는지 확인
        if join > join_cnt:  # 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것
            join_cnt = join
            revenue = sales
            # print(f"가입자 갱신 발생, {permu}일 때: {join_cnt} -> {join}명 가입, {revenue}원 -> {sales}원 판매")
        elif join == join_cnt:
            if sales > revenue:  # 2. 이모티콘 판매액을 최대한 늘리는 것
                # print(f"판매액 갱신 발생, {permu}일 때: {join_cnt} -> {join}명 가입, {revenue}원 -> {sales}원 판매")
                revenue = sales

        # print(join_cnt, revenue, permu)
        # print('--------------------')

    # print(join_cnt, revenue)
    answer[0], answer[1] = join_cnt, revenue
    return answer


"""
users = [[40, 10000], [25, 10000]], emoticons = [7000, 9000] -> [1, 5400]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], emoticons = [1300, 1500, 1600, 4900] -> [4, 13860]
"""

# fmt: off
print(solution(users=[[40, 10000], [25, 10000]], emoticons=[7000, 9000]))
print(solution(users=[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], emoticons=[1300, 1500, 1600, 4900]))
