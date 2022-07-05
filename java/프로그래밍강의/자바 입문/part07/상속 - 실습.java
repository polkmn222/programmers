/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 Machine.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

Machine 클래스를 상속받는 클래스, Car를 만들어보세요.
*/

class Car extends Machine {
    
}

class Machine {
    public void turnOn() {
        System.out.println("켰습니다.");    
    }
    
    public void turnOff() {
        System.out.println("껐습니다.");    
    }
}