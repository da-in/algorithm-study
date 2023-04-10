def solution(line):
    answer = []
    dots=[]
    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            a,b,e=line[i]
            c,d,f=line[j]
            if (a*d)-(b*c)!=0:
                y=((e*c)-(a*f))/((a*d)-(b*c))
                x=((b*f)-(e*d))/((a*d)-(b*c))
                if y==int(y) and x==int(x):
                    dots.append([int(y),int(x)])


    #dotY=[i[0] for i in dots]
    #dotX=[i[1] for i in dots]
    dotY=list(zip(*dots))[0]
    dotX=list(zip(*dots))[1]

    yStart=min(dotY)
    yMax=max(dotY)
    xStart=min(dotX)
    xMax=max(dotX)
    
    # ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    #                                  ㅋ
    # dots.sort()                      ㅋ
    # yStart=dots[0][0]                ㅋ
    # yMax=dots[-1][0]                 ㅋ
    # dots.sort(key= lambda x: x[1])   ㅋ
    # xStart=dots[0][1]                ㅋ
    # xMax=dots[-1][1]                 ㅋ
    #                                  ㅋ
    # ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

    
    data=[['.'for i in range(xMax-xStart+1)]for j in range(yMax-yStart+1)]
    for d in dots:
        data[d[0]-yStart][d[1]-xStart]="*"
    for i in reversed(data):
        answer.append(''.join(i))
    
    return answer
