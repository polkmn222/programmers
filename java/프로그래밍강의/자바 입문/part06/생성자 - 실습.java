/*
문제 설명
※ 본 문제는 두 코드 파일, Person.java와 PersonExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

Person클래스에 int형 변수를 매개변수로 받아 age 값을 초기화하는 생성자를 만들어주세요.
*/

class Person{
    
    int age;
    
    public Person(int a) {
        age = a;
    }
    
}

//실행을 위한 코드입니다.
public class PersonExam {
    public static void main(String[] args) {
        //Person클래스에서 int형 변수를 매개변수로 받는 생성자를 호출합니다.
        Person person = new Person(25);
    }
}
