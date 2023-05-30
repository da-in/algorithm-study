from itertools import product


def solution(users, emoticons):
    """

    풀이시간
    - 약 2시간 가량 풀다가 계속 테스트케이스가 안 맞아서 레퍼런스 참조
    (https://blogeon.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV2-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%95%A0%EC%9D%B8%ED%96%89%EC%82%AC)

    접근법
    - user 와 emoticon 의 길이가 그렇게 길지 않다 -> 시간 복잡도는 크게 생각안해도 될 것 같음
    - 개별 아이템에 할인 비율을 막 조절하는 방법은 너무 복잡함 -> 구현 느낌 보다는 키 포인트가 되는 아이디어를 떠올려야 할 듯
        - 라고 생각하고 오래동안 삽질하다가 말이 안된다고 느껴서 문제를 다시 읽어보니 할인율은 10, 20, 30, 40 중 하나였다 ㅠㅠ
        - 시간복잡도도 크게 고려하지 않아도 되니 노가다(?)를 하면 되겠다 라고 생각

    회고
    - 구현 문제를 조금 더 연습해봐야겠다는 것을 느낌, 사실 접근이 어려운 문제가 아니었는데 구현 능력이 부족해서 못 푼다는 건 많이 아쉽다!
    - itertools 의 product 를 몇 번 써본적이 있었는데도 생각해내지 못했음, 반성하자 ..!

    """

    answer = []

    for discount in product([10, 20, 30, 40], repeat=len(emoticons)):       # 가능한 모든 할인율 조합에 대해 검토
        service, total = 0, 0                                               # 서비스 가입, 고객의 총 구매 가격 초기화

        for user in users:
            limit_discount = user[0]
            limit_pay = user[1]

            pay = []                                                        # 할인율 조합에 대한 고객의 가격 초기화
            for i in range(len(emoticons)):
                if discount[i] >= limit_discount:
                    pay.append(emoticons[i] * (100 - discount[i]) // 100)

            pay = sum(pay)

            if pay >= limit_pay:                                            # 가격 상한을 넘어버리면 서비스 가입
                service += 1

            else:                                                           # 가격 상한을 넘지않으면 이모티콘 구매
                total += pay
        answer.append([service, total])

    return sorted(answer, reverse=True)[0]                                  # 모든 할인율 조합의 경우의 수에서 문제에서 제시한대로 정렬
