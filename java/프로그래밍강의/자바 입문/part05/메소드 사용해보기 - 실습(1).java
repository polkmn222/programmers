/*
문제 설명
참조 타입 복습하기
기본형 타입과 참조 타입의 차이는 메소드 호출에서 확인할 수 있습니다. 다음 코드는 기본형 타입 변수 value와 참조형 타입 변수 arr을 addOne이라는 메소드에 전달합니다. 두 메소드 모두 전달받은 값을 1씩 더하는데요. 메소드 실행 후 전달했던 값을 출력해 보면 결과가 다릅니다.

코드를 실행해서 기본형 타입과 참조 타입의 차이를 확인해보세요.
*/

class ReferenceTypeExam {
    public static void main(String []args) {
        ReferenceTypeExam exam = new ReferenceTypeExam();
        
        //기본형 변수value1을 addOne에 전달합니다.
        int value = 10;
        exam.addOne(value);
        System.out.println("기본형 변수의 값을 다른 메소드에서 변경한 결과: " + value);
        
        //참조형 변수arr을 addOne에 전달합니다.
        int []arr = {10};
        exam.addOne(arr);
        System.out.println("참조형 변수의 값을 다른 메소드에서 변경한 결과: " + arr[0]);
    }
    
    
    public void addOne(int value) {
        value++;
    }
    
    public void addOne(int[] arr) {
        for(int i = 0; i < arr.length; i++){
            arr[i] ++;
        }
    }
}
