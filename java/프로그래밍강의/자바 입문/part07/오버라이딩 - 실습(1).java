/*
문제 설명
※ 본 문제는 세 코드 파일, Bus.java / Car.java / BusExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

오버라이딩은 부모 클래스의 메소드를 수정하고 싶을 때 아주 유용하게 쓰입니다. 예를 들어 버스는 일반 자동차와 비슷한 면도 많지만, 일반 자동차와는 달리 다음 정거장이 어디인지 안내하는 특수한 일도 하지요.

Car 클래스를 상속받는 Bus 클래스에서 run 메소드를 오버라이드 하세요. 오버라이드한 run메소드는 "차가 달리면서 다음 정거장을 안내합니다."라고 출력해야 합니다.
*/

public class Bus extends Car {
    // run 메소드를 오버라이드 하세요. 메소드의 접근 제한자는 public이어야 합니다.
    public void run() {
        System.out.println("차가 달리면서 다음 정거장을 안내합니다.");
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

//다음은 실행을 위한 코드입니다. 수정하지 마세요.
class BusExam {
    public static void main(String [] args) {
        Bus bus = new Bus();
        bus.run();
    }  
}