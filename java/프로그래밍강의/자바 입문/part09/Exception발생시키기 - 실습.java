/*
문제 설명
ExceptionExam클래스의 get50thItem메소드에서는 매개변수로 받은 array의 50번째 값을 return합니다. 만약 array의 크기가 50보다 작을 경우에는 0을 return하고 있는데요. 0을 리턴하는 대신에 IllegalArgumentException을 throw하도록 만들어 보세요.
*/

public class ExceptionExam{
    public int get50thItem(int []array) throws IllegalArgumentException {
        if(array.length < 50){
            throw new IllegalArgumentException("");
        }
    return  array[49];
    }
}


//아래는 실행을 위한 코드입니다. 수정하지 마세요.
public class ExamExam{
    public static void main(String[]args){
        ExceptionExam ex = new ExceptionExam();
    }
}