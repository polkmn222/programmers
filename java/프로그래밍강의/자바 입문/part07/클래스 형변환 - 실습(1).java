/*
문제 설명
Car클래스는 gas라는 필드를 가집니다. 그리고 Car클래스를 상속받은 Suv, Truck, Bus클래스가 있습니다. GasStation클래스에서는 fill(주유하다)라는 메소드가 있는데요. 총3종류의 fill메소드가 오버로딩 되어 있습니다. 각각 Suv, Truck, Bus의 객체를 매개변수로 받아서 주유를 하는 메소드인데요. Car, Suv, Truck, Bus클래스를 한 번씩 살펴보고 GasStation의 코드를 살펴본 다음 제출을 눌러서 결과를 확인하세요.
*/

public class Car{
    public int gas;
}

public class Suv extends Car{
}

public class Truck extends Car{
}

public class Bus extends Car{
}

public class GasStation{
    public static void main(String[]args){
        GasStation gasStation = new GasStation(); //gasStation인스턴스 생성
        Suv suv = new Suv(); //suv 인스턴스 생성
        Truck truck = new Truck(); //truck 인스턴스 생성
        Bus bus = new Bus(); //bus 인스턴스 생성
        
        //gasStation에서 suv에 기름을 넣습니다.
        gasStation.fill(suv);
        
        //gasStation에서 truck에 기름을 넣습니다.
        gasStation.fill(truck);
        
        //gasStation에서 bus에 기름을 넣습니다.
        gasStation.fill(bus);
        
    }
    
    public void fill(Suv suv){
        System.out.println("Suv에 기름을 넣습니다.");
        suv.gas += 10;
        System.out.println("기름이 "+suv.gas+"리터 들어있습니다.");
    }
    
    public void fill(Truck truck){
        System.out.println("Truck에 기름을 넣습니다.");
        truck.gas += 10;
        System.out.println("기름이 "+truck.gas+"리터 들어있습니다.");
    }
    
    public void fill(Bus bus){
        System.out.println("Bus에 기름을 넣습니다.");
        bus.gas += 10;
        System.out.println("기름이 "+bus.gas+"리터 들어있습니다.");
    }
}