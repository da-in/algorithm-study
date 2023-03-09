def main():
    print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    camera=[routes[0][1]]
    for i in range(1,len(routes)):
        if routes[i][0] <= camera[-1] and routes[i][1] >= camera[-1]:
            continue
        else:
            camera.append(routes[i][1])
    return len(camera)


    
if __name__ == "__main__":
    main()