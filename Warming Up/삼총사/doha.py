def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer

    
# JAVA 코드
# class Solution {
#     public int solution(int[] number) {
#         int answer = 0;

#         for(int i=0; i<number.length-2; i++){
#             for(int j=i+1; j<number.length-1; j++){
#                 for(int k=j+1; k<number.length; k++){
#                     if(number[i]+number[j]+number[k]==0) answer++;
#                 }
#             }
#         }

#         return answer;
#     }
# }