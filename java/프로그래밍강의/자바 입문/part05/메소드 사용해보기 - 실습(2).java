/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

CarExam.java 파일의 main 메소드에서 Car 클래스의 인스턴스를 만들어, run메소드를 호출해 보세요.
*/

class CarExam {
    public static void main(String [] args) {
        // 이 아래에서 car에 Car클래스의 인스턴스를 생성하고 run메소드를 사용해 보세요.
        Car car = new Car();
        car.run();
        
    }
}


class Car{
    void run(){
        System.out.println("차가 달립니다.");
    }
}