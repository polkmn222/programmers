/*
문제 설명
다음 코드는 이차원 배열을 출력하는 코드입니다. 코드를 살펴보고 실행해서 결과를 확인해 보세요.
*/

public class ArrayExam {
    public static void main(String[] args) {
        int [][] array = {{1}, {1, 2}, {1, 2, 3}, {1, 2, 3, 4}};
        
        // 2차원 배열 array를 출력합니다.
        for(int i = 0 ; i < array.length; i++) {
            System.out.print( (i+1) + "번째 줄을 출력합니다>");
            for(int j = 0; j< array[i].length; j++) {
                System.out.print(array[i][j]+" ");
            }
            System.out.println("");
        }
    }
}