def solution(users, emoticons):
    """
    - 소요 시간: 33분 풀이하다 감이 안잡혀서 풀이 확인 .. 문제 이해부터 오래 걸렸고, 이해 후 그대로 구현해보려 했으나 구현도 잘 안됨
    - 접근법 ([참고 글](https://velog.io/@top1506/2023-KAKAO-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%95%A0%EC%9D%B8%ED%96%89%EC%82%AC-python))
      - 문제 조건 확인 시, 입력값 범위가 매우 적다 => 완전 탐색으로 가능
      - backtracking을 활용해 풀이
    """
    sales = [10, 20, 30, 40]
    check = [0] * len(emoticons)
    answer = []

    def backtracking(depth):
        if depth == len(emoticons):
            count = 0
            result = 0
            for rate, price in users:
                sum = 0
                for i in range(len(check)):
                    value = emoticons[i] - int(emoticons[i] * (check[i] / 100))
                    if rate <= check[i]:  # 사용자의 기준 할인율(rate)보다 크거나 같으면 구매
                        sum += value
                if sum >= price:  # 구매 가격 합이 사용자의 기준 가격(price)을 넘어서면
                    count += 1  # 이모티콘 플러스 가입
                    result -= sum
                result += sum
            answer.append([count, result])
            return

        for i in range(len(sales)):
            check[depth] = sales[i]
            backtracking(depth + 1)
            check[depth] = 0

    backtracking(0)
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[-1]
