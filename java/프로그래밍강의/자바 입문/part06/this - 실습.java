/*
문제 설명
※ 본 문제는 두 코드 파일, Person.java와 PersonExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

Person 클래스의 생성자가 매개변수 name과 age를 클래스 필드 name과 age에 저장하도록 만들어 보세요.
*/

class Person {
    String name;
    int age;
    public Person(String name, int age) {
        // 매개변수로 받은 name과 age를 각각 name, age 필드에 저장하세요.
        this.name = name;
        this.age = age;
    }
}

// 실행을 위한 코드입니다.
public class PersonExam {
    public static void main(String[] args) {
        // Person클래스에서 String과 int를 매개변수로 받는 생성자를 호출합니다.
        Person person = new Person("사람", 25);
    }
}