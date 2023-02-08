def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    
    h={}
    for p in phone_book:
        h[p] = True
    for pn in phone_book:
        temp=""
        for p in pn:
            temp+=p
            if temp in h and temp!=pn:
                return False
        
    return True