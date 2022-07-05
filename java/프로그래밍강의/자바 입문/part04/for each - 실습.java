/*
문제 설명
for each문을 이용해서 일차원 배열, array의 원소를 한 줄씩 출력하세요.
*/

public class ForEachExam {
    public static void main(String[] args) {
        int [] array = {1, 5, 3, 6, 7};
        //for each문을 이용해서 array의 값을 한 줄씩 출력하세요
        for(int value : array) {
            System.out.println(value);
        }
        
    }
}