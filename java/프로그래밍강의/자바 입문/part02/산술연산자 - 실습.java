/*
문제 설명
주석의 지시에 따라 코드를 완성해보세요.

변수 c에는 변수 a와 b의 합을 저장
변수 d에는 변수 a에 b를 뺀 값을 저장
변수 e에는 변수 a와 b의 곱을 저장
변수 f에는 a를 b로 나눈 나머지를 저장
*/


public class OperatorExam {
    public int[] calculate() {
        int a = 7; 
        int b = 3;

        //c는 a와 b의 합 
        int c = a + b;

        //d는 a와 b의 차
        int d = a - b;

        //e는 a와 b의 곱
        int e = a * b;

        //f는 a를 b로 나눈 나머지 
        int f = a % b;


        System.out.printf("c는: %d\n", c);
        System.out.printf("d는: %d\n", d);
        System.out.printf("e는: %d\n", e);
        System.out.printf("f는: %d\n", f);

        int ret[] = {c, d, e, f};
        return ret;
    }

    public static void main(String []args){
        new OperatorExam().calculate();
    }
}