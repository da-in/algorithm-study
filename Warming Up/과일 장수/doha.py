def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(m - 1, len(score), m):
        answer += score[i] * m
    return answer

# JAVA
# import java.util.*;

# class Solution {
#     public int solution(int k, int m, int[] score) {
#         int answer = 0;

#         Arrays.sort(score);

#         for(int i = score.length; i >= m; i -= m){
#             answer += score[i - m] * m;
#         }

#         return answer;
#     }
# }