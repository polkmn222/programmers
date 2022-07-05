/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

Car 클래스에는 문자열과 정수를 입력받아 필드 name와 number를 초기화하는 생성자가 있습니다. 주어진 생성자를 이용해, 나머지 두 생성자를 구현해보세요.

매개변수를 받지 않는 생성자: name은 "이름없음", number는 0으로 초기화 합니다.
매개변수로 String을 받는 생성자: 매개변수로 name을 초기화하고, number는 0으로 초기화 합니다.
*/

public class Car {
    String name;
    int number;
    
    Car() {
        // this.name = "이름없음";
        // this.number = 0;
        this("이름없음", 0);
    }
    public Car(String name){
        this(name, 0);
    }
    // Car(String name) {
    //     this.name = "name";
    //     // this.number = 0;
    // }

    Car(String name, int number) {
        this.name = name;
        this.number = number;
    }
}

// 실행을 위한 코드입니다.
public class CarExam {
    public static void main(String[] args) {
        Car car1 = new Car();
        Car car2 = new Car("자동차");
        Car car3 = new Car("자동차", 1234);
    }
}