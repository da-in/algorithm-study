# 즉, 아무 한 전화번호가 다른 전화번호의 시작부터의 일부와 동일하면 false

def main():
    phone_book=["119", "97674223", "1195524421"]
    print(solution(phone_book))

def solution(phone_book):
    phone_book.sort() 
    for i in range(len(phone_book)-1):
            # j가 접두어가 맞다면 : return false
            if phone_book[i+1].startswith(phone_book[i]): return False
    return True
   

if __name__ == "__main__":
    main()
