/*
문제 설명
다음 코드에서는 길이 10인 배열에서 인덱스가 20인 값을 읽어오려고 하기 때문에 Exception이 발생하게 됩니다. Exception이 발생하는 부분을 try/catch문으로 감싸서 처리해보세요.
*/

public class ExceptionExam{
    public static void main(String []args){
        int [] array = new int[10];
        try {
			array[20] = 5;
			
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println(e.toString());
		} finally {
			System.out.println("zz");
		} 
        
    }
}