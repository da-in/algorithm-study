def solution(phone_book):

    hash = {}
    phone_book.sort()

    for i in range(len(phone_book)-1):
        hash[phone_book[i]] = '1'
        l = len(phone_book[i])
        if phone_book[i+1][:l] in hash:
            return False
    return True
