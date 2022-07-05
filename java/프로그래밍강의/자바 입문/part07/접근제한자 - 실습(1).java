/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

CarExam 클래스의 main 메소드에서 Car클래스의 인스턴스를 만들고 name, number를 출력하는데요. 두 필드는 private 필드이기 때문에 코드를 실행하면 에러가 발생합니다. CarExam이 Car의 instance를 사용할 수 있도록 name과 number를 public 필드로 변경해 보세요.
*/

public class Car {
    public String name;
    public int number;
    
    public Car(String name, int number) {
        this.name = name;
        this.number = number;
    }
}

public class CarExam {
    public static void main(String[] args) {
        Car car = new Car("포니", 1234);
        
        System.out.println("name: " + car.name);
        System.out.println("number: " + car.number);
        
    }
}

