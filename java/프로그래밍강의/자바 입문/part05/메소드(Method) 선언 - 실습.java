/*
문제 설명
※ 본 문제는 두 코드 파일, MyClass.java와 MyClassExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

MyClass 클래스에 다음 조건을 만족하는 메소드를 작성해보세요.

메소드는 정수 하나를 매개변수로 받아야합니다.
메소드는 정수를 반환해야합니다. (정해진 값은 없고, 아무 정수나 반환해도 됩니다.)
메소드 이름은 myMethod여야합니다.
*/

public class MyClass{
    //이곳에 코드를 작성하세요.
    public int myMethod(int x) {
        // x = 3;
        return x;
    }
}

// 정상적인 실행을 위한 코드입니다. 이 아래는 수정하지 마세요.
public class ClassExam{
    public static void main(String[]args){
        MyClass mc = new MyClass();
    }
}