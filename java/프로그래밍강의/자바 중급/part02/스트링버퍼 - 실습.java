/*
문제 설명
StringBufferExam의 randomName메소드는 임의의 이름과 성을 고른 다음, 이들을 조합해서 임의의 이름을 만들어냅니다. 22번째 줄에서 메소드체이닝을 이용해 sb에 firstName, 공백(" "), lastName을 붙이고, 마지막에 toString()을 붙여서 String type의 return을 하도록 만들고 제출해 보세요.
*/

import java.util.Random;

public class StringBufferExam{
    public String randomName(){
        StringBuffer sb = new StringBuffer();
        String[] firstNames = {"Tod", "John", "Michael"};
        String[] lastNames = {"Smith", "Brown", "Davis"};
        
        // 0~2 사이의 임의의 숫자를 골라서
        int random1 = new Random().nextInt(3);
        // 랜덤하게 이름을 뽑는다.
        String firstName = firstNames[random1];
        
        
        // 0~2 사이의 임의의 숫자를 골라서
        int random2 = new Random().nextInt(3);
        // 랜덤하게 성을 뽑는다.
        String lastName = lastNames[random2];
        
        // sb에 이름(fistName) 공백(" ") 성(lastname) 순으로 append해 보세요.
        // 단 메소드 체이닝을 이용해야 합니다.
        sb.append(firstName).append(" ").append(lastName);
        return sb.toString();
    }
    public static void main(String[]args) {}
}