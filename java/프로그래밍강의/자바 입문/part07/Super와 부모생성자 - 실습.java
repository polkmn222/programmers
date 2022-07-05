/*
문제 설명
※ 본 문제는 세 코드 파일, Bus.java / Car.java / BusExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

Bus 클래스는 Car 클래스의 자식 클래스입니다. Bus 클래스의 생성자는 name(이름), number(차량번호), fee(요금)을 입력받는데요. 부모 클래스의 생성자를 이용해 name과 number를 초기화한 후, fee를 직접 초기화하는 Bus의 생성자를 만들어보세요.
*/

public class Bus extends Car {
    int fee;
    
    public Bus(String name, int number, int fee) {
        // super를 이용해서 Car클래스의 생성자를 이용하세요.
        super(name, number);
        this.fee = fee;
    }
}

public class Car {
    String name;
    int number;
    public Car(String name, int number) {
        this.name = name;
        this.number = number;
    }
}

//아래는 실행을 위한 코드입니다. 수정하지 마세요.
public class BusExam {
    public static void main(String[] args) {
        Bus bus = new Bus(new String("뛰뛰"), 3000, 1050);
        if(!bus.name.equals("뛰뛰")){
            System.out.println("bus의 name이 다릅니다.");
        }
        else if(bus.number != 3000){
            System.out.println("bus의 number가 다릅니다.");
        }
        else if(bus.fee != 1050){
            System.out.println("bus의 fee가 다릅니다.");
        }
        else{
            System.out.println("정답입니다. [제출]을 누르세요.");
        }
        
    }
}