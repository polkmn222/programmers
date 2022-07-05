/*
문제 설명
변수 i와 while문을 이용해서 1부터 10까지 숫자를 차례로 출력해 보세요. while 문은 실행문을 반복적으로 실행해야 할 때 사용합니다.
*/

public class WhileExam{
    public static void main(String[] args) {
        int i = 1;
        // while 문을 써서 1부터 10까지 숫자를 출력해보세요.
        while(i<10){
            System.out.println(i);
            i++;
        }
        System.out.println(i);
    }
}