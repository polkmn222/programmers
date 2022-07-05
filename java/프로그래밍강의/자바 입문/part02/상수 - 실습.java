/*
문제 설명
원의 둘레, 반지름 * 2 * 원주율을 구하는 코드를 짜려 합니다. 빈칸에 원주율을 나타내는 double 타입 상수, PI를 선언과 동시에 초기화해 코드를 완성해보세요. 원주율은 3.14159입니다.
*/

public class ConstantExam {
    public static void main(String[] args) {
        // 상수 PI를 만들어보세요.
        
	final double PI = 3.14159;

        int radius = 5;
        double result = radius * 2 * PI;
        System.out.println(result);
    }
}