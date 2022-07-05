/*
문제 설명
다음은 while문을 이용해 1부터 10까지 숫자를 출력하는 코드입니다. 여섯 번째 줄에 if문을 추가해서 i가 짝수일 때만1 i를 출력하게 코드를 바꿔보세요.
*/

public class WhileExam{
    public static void main(String[] args){
        int i = 1;
        while(i < 11){
            // if 문을 추가해, i가 짝수일때만 i를 출력하는 코드를 짜보세요.
            if(i % 2 == 0) {
                System.out.println(i);
            }
            // System.out.println(i);
            i++; 
        }
    }
}