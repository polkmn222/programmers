/*
문제 설명
다음 코드를 실행하면
error: unreported exception MyCheckedException; must be caught or declared to be thrown
이라는 에러메시지가 나옵니다. get50thItem에서 Checked exception을 throw하는데 try/catch문으로 처리되고 있지 않기 때문입니다. 코드의 6번째줄을 try/catch문으로 처리해 보세요.
*/

public class MyCheckedException extends Exception{
    
}

public class ExceptionExam{
    public static void main(String[] args){
        ExceptionExam exam = new ExceptionExam();
        int[] array = new int[10];
        try {
            exam.get50thItem(array);
        } catch(Exception ex) {
            // ex.printStrackTrace();
        }
        // exam.get50thItem(array);
    }
    
    public int get50thItem(int []array) throws MyCheckedException{
        if(array.length < 50){
            throw new MyCheckedException();
        }
        return  array[49];
    }
}