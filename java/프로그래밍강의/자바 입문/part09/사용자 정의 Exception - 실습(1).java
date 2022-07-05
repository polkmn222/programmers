/*
문제 설명
MyCheckedException클래스가 Checked Exception이 되도록 만들어 보세요.
*/


public class MyCheckedException extends Exception {
    // public CheckedExam(Exception ex) {
    //     super(ex);
    //     // return msg;
    // }
    
//     public CheckedExam(Exception ex) {
//         super(ex);
//     }
    
}


//아래는 실행을 위한 코드입니다. 수정하지 마세요.
public class CheckedExam{
    public static void main(String[]args){
        MyCheckedException ex = new MyCheckedException();
    }
}