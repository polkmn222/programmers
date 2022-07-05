/*
문제 설명
이번엔 long 타입 변수, longValue의 값을 int 타입 변수에 넣으려합니다. 빈칸에 int 타입 변수, intValue를 선언하고, 변수를 longValue를 이용해 초기화해주세요.
*/

public class TypeCastingExam {
    public static void main(String[] args) {
        long longValue = 20;
        //이 아래줄에 int형 변수 intValue를 선언하고 longValue에 들어있는 값을 담아보세요.
        
	int intValue = (int)longValue;
        
        System.out.println(intValue);
    }
}