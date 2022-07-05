/*
문제 설명
다음 코드는 변수 value가 3의 배수이면 ret에 3을 저장합니다. else if 문을 추가해 value가 4의 배수이면 ret에 4를 저장하는 코드를 추가해보세요.
*/

public class ConditionalExam{
    public int conditionTest(int value){
        // 변수 value가 선언되어 있다고 가정하고 아래에 코드를 작성하세요.
        int ret = 0;
        if( value % 3 == 0 ){
            ret = 3;
        } else if( value % 4 == 0 ) {
            // 이 아래 줄에 else 구문을 추가해서 코드를 완성하세요.
            ret = 4;
        }    

        // 결과 체크를 위한 코드입니다.
        return ret;
    }
    
    //아래는 실행을 위한 코드입니다. 수정하지 마세요.
    public static void main(String[]args){
        ConditionalExam exam = new ConditionalExam();
        exam.conditionTest(6);
        exam.conditionTest(8);
    }
}