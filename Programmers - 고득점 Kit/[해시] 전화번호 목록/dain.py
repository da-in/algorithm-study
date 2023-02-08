def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    phone_dict = {}
    for phone in phone_book:
        cur = phone_dict
        for p in phone:
            if "end" in cur:
                return False
            if p not in cur:
                cur[p] = {}
            cur = cur[p]
        cur["end"] = True
    return True
