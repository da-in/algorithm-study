from heapq import *
def cal_time(time):
        hour, minu = map(lambda x : int(x), time.split(":"))
        return hour * 60 + minu

def solution(book_time):
    room_count = 1
    end_time = []
    book_time.sort()

    heappush(end_time, cal_time(book_time[0][1]))

    for i in range(1, len(book_time)):
        st_time, en_time = map(cal_time, book_time[i])
        cur_end = heappop(end_time)

        if st_time < cur_end + 10:
            heappush(end_time, cur_end)
            room_count += 1
        heappush(end_time, en_time)

    return room_count
