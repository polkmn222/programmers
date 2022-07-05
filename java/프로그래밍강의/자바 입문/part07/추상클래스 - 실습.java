/*
문제 설명
※ 본 문제는 세 코드 파일, Car.java / Machine.java / CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

추상 클래스인 Machine클래스는 두 추상 메소드, turnOn과 turnOff를 가집니다. Machine 클래스를 상속받는 Car 클래스를 만들고, Car클래스에 turnOn 메소드와 turnOff 메소드를 구현하세요.
*/

class Car extends Machine {
    // Machine 클래스를 상속받고, 추상 메소드를 구현하세요.
    @Override
    public void turnOn() {
        System.out.println("꽥꽥!!");
    }
    
    @Override
    public void turnOff() {
        System.out.println("꽥꽥!!");
    }
    
}

public abstract class Machine {
    public abstract void turnOn();
    public abstract void turnOff();
}

//아래는 실행을 위한 코드입니다. 수정하지 마세요.
public class CarExam {
    public static void main(String[] args) {
        Car car = new Car();
        if(Machine.class.isInstance(car)){
            System.out.println("정답입니다. [제출]을 누르세요.");
        }
        else{
            System.out.println("Car가 Machine을 상속받지 않았습니다.");
        }
    }
}