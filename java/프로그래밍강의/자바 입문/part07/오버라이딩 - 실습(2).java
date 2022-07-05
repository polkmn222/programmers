/*
문제 설명
※ 본 문제는 세 코드 파일, Bus.java / Car.java / BusExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

메소드를 오버라이딩하면서, 부모 클래스의 메소드를 호출하고 싶을때에는 super()를 이용하세요. 주어진 코드에서, Bus 클래스의 메소드 run은 부모 클래스의 run 메소드를 호출합니다. [실행] 버튼을 눌러 코드가 어떻게 동작하는지 알아보세요.
*/

public class Bus extends Car {
    public void run() {
        // Car 클래스의 run을 호출합니다.
        super.run();
        System.out.println("다음 정거장을 안내합니다.");
    }
}

public class Car {
    public void run() {
        System.out.println("차가 달립니다.");
    }
    
    public void stop() {
        System.out.println("차가 멈춥니다.");
    }
    
    public void horn() {
        System.out.println("경적을 울립니다.");
    }
}

public class BusExam {
    public static void main(String[] args) {
        Bus bus = new Bus();
        bus.run();
    }
}