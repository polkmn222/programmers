/*
문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
*/

// import java.util.List;
// import java.util.ArrayList;

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        answer[0] = x;
        for(int i=1; i<n; i++) {
            answer[i] = answer[i-1] + x; 
        }
        
        // List<Integer> answer = new ArrayList<Integer>();
//         // for(int j=0; j<n; j++) {
//             for(int i=x; i<=x*n; i+=x) {
//                 for(int j=0; j<n; j++) {
                    
//                 answer[j] = i;
//             }
//         }
        // for(int i=1; i<=x*n; i+=n) {
        //     answer.add(i);
        // }
        // System.out.println(answer);
        // for(int i=1; i<=answer.length; i++) {
        //     answer[i-1] = x * i;
        // }
        
        return answer;
    }
}