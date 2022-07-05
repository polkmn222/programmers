/*
문제 설명
int형 변수, value가 3의 배수인지 확인하려면 어떻게 해야 할까요? value를 3으로 나눈 나머지가 0인지를 검사하면 됩니다. value의 값을 변경해가면서 출력이 어떻게 바뀌는지 확인해 보세요.
*/

public class ConditionalExam {
    public static void main(String[] argv) {
        int value = 3;        
        if( value % 3 == 0 ) {
            System.out.println("value는 3의 배수입니다.");
        }
    }
}