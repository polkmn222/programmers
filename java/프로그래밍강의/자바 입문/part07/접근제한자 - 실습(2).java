/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

접근제한자는 필드뿐만 아니라 메소드에도 적용할 수 있습니다. 클래스의 main 메소드에서 Car클래스의 인스턴스를 만들고 run, stop 메소드를 수행하는데요. 이때, stop 메소드는 private이라 클래스 밖에서는 사용할 수 없습니다.

CarExam 클래스가 stop 메소드를 쓸 수 있도록 Car 클래스의 stop메소드를 public으로 바꿔주세요.
*/

public class Car{
    public void run(){
        System.out.println("차가 달립니다.");
    }
    
    public void stop(){
        System.out.println("차가 멈춥니다.");
    }
}

public class CarExam{
    public static void main(String[]args){
        Car car = new Car();
        car.run();
        car.stop();
    }
}
