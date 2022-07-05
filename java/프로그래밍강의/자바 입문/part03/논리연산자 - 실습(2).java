/*
문제 설명
어떤 사람이 20대인지 검사하려 합니다.

사람의 나이를 담은 int 형 변수, age가 주어집니다. age가 20대를 나타낸다면 isTwenties에 true를, 그렇지 않으면 false를 저장하는 코드를 작성하세요.
※ 20대는 20세 이상, 29세 이하입니다.
*/

public class LogicalOperatorExam {
    public boolean isAgeTwenties(int age) {
        boolean isTwenties = false;
        //아래 빈칸을 채워 코드를 완성하세요.
        if( 
age >= 20 && age <= 29
 ) {
            isTwenties = true;
        }
        else {
            isTwenties = false;
        }    
        return isTwenties;
    }

    public static void main(String[] args) {
        LogicalOperatorExam exam = new LogicalOperatorExam();
        exam.isAgeTwenties(19);
        exam.isAgeTwenties(25);
    }
}