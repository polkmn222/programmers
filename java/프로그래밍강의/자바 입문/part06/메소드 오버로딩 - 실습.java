/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

Car클래스에 int형 매개변수를 1개 받고, 반환 값이 없는 run 메소드를 추가해 보세요.
*/

class Car {
    void run() {
        System.out.println("차가 달립니다.");        
    }
    // 정수 하나를 매개변수로 받는 메소드, run을 추가해 보세요.
    void run(int x) {
        System.out.println("차가 달립니다.");        
    }
    
}

// 실행을 위한 코드입니다.
public class CarExam {
    public static void main(String[] args) {
        // Person클래스에서 String과 int를 매개변수로 받는 생성자를 호출합니다.
        Car car = new Car();
        
        car.run();
        // int형 매개변수를 받는 run을 호출합니다.
        car.run(100);
    }
}