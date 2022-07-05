/*
문제 설명
주어진 코드에서 str1과 str2은 모두 "Hello World"라는 값을 저장하는 변수입니다. 둘은 사람이 보기엔 완전히 똑같지만, java는 둘을 다르다고 판단합니다.

주어진 코드는 equal operator == 로 두 변수를 비교합니다. 코드를 실행해 java가 str1과 str2을 다르다고 판단하는 것을 확인해보세요
*/

public class StringExam {
    public static void main(String[] args) {
        String str1 = new String("Hello world");
        String str2 = new String("Hello world");
        
        if(str1 == str2){
            System.out.println("str1과 str2는 같은 인스턴스를 참조합니다.");
        }
        else{
            System.out.println("str1과 str2는 다른 인스턴스를 참조합니다.");
        }
    }
}