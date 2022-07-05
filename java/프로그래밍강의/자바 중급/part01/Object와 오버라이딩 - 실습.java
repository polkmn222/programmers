/*
문제 설명
Car클래스는 name과 number라는 필드를 가집니다. Car클래스를 문자열로 바꾸면 다음과 같은 형식이 되도록 toString메소드를 오버라이드 해 보세요.
name: [이름], number: [번호]

예를들어 name의 값이 "Car"이고, number가 1234이라면, 해당 오브젝트의 문자열 값은 "name: Car, number: 1234"와 같이 되어야 합니다.
*/

public class Car{
    String name;
    int number;
    // name.toString("Car");
    // number.toString("1234");
    //toString을 오버라이드 해 보세요.
    //return 형식은 아래줄을 참고하세요: 
    //"name: " + name + ", number: " + number;
    @Override 
    public String toString() {
        return "name: " + name + ", number: " + number;
  }
    
}

//아래는 실행을 위한 코드입니다. 수정하지 마세요.
public class CarExam{
    public static void main(String[]args){
        Car ex = new Car();
    }
}