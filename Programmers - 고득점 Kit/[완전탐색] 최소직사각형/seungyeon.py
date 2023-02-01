def main():
    sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]	
    print(solution(sizes))

def solution(sizes):
    w=[]
    h=[]
    for i in sizes: 
        w.append(max(i))
        h.append(min(i))
    return max(w)*max(h)
    
if __name__ == "__main__":
    main()