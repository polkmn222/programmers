/*
문제 설명
static 메소드는 static한 필드(속성)만 사용할 수 있습니다. 그런데 주어진 코드는 static 메소드인 main method에서 static 하지 않은 변수, value를 쓰려고해 오류가 발생합니다. 코드가 정상적으로 동작하도록 코드를 수정해보세요.
*/


public class VariableScopeExam{
    static int value = 10;
    public static void main(String []args){
        System.out.println(value);
    }
}