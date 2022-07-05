/*
문제 설명
ExceptionExam클래스의 get50thItem메소드에서는 매개변수로 받은 array의 50번째 값을 return합니다. 만약 array의 크기가 50보다 작을 경우에는 ArrayIndexOutOfBoundsException이라는 예외가 발생하는데요. get50thItem이 ArrayIndexOutOfBoundsException를 throw하도록 정의해 보세요.
*/

public class ExceptionExam{
    public int get50thItem(int []array) throws ArrayIndexOutOfBoundsException {
        return  array[49];
    }
}

public class ExamExam{
    public static void main(String[]args){
        ExceptionExam ex = new ExceptionExam();
    }
}