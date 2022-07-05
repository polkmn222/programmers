/*
문제 설명
Integer는 int의 wrapper class입니다. class이기 때문에 속성과 메소드를 가지는데요. 다음 코드를 실행해 보면 Integer 타입인 경우 필드와 method를 사용할 수 있지만, 기본형 타입인 int의 경우 필드와 method를 사용할 수 없는걸 확인할 수 있습니다. (코드의 7~9번째 줄을 지워야 정상동작 합니다.)

https://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html 를 참고해서 Integer의 다양한 필드와 메소드를 테스트해 보세요.
*/


public class IntegerExam{
    public static void main(String[] args){
        Integer i1 = 5;
        int max_int = i1.MAX_VALUE;
        long i1_long = i1.longValue();
        
        // int i2 = 5;
        // int min_int = i2.MIN_VALUE;
        // long i2_long = i2.longValue();
    }
}