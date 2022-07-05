/*
문제 설명
Taxi클래스는 Meter인터페이스를 구현하고 있습니다. Meter인터페이스를 살펴보면 start,stop이외에도 default메소드인 afterMidnight이라는 메소드가 추가되었는데요. afterMidnight은 default로 선언되어 있기 때문에 Taxi에서 별도로 구현하지 않더라도 에러가 발생하지는 않습니다. 우선 [실행]을 눌러서 확인해 보세요. 그리고 Taxi에서 afterMidnight을 오버라이드 한 다음 [제출]해 보세요.
*/

public class Taxi implements Meter{
    public void start(){
        System.out.println("택시가 출발합니다.");
    }
    
    public int stop(int distance){
        int fare = distance * 2;
        System.out.println("택시가 도착했습니다. 요금은 "+fare+"입니다.");
        return fare;
    } 
    @Override
	public  void afterMidnight() {
		System.out.println("자정이 넘었습니다. 할증이"
				+ " 필요한경우 이 메소드를 오버라이드 하세요.");
	}
    
}

public interface Meter{
    public void start();
    public int stop(int distance);
    
    public default void afterMidnight(){
        System.out.println("자정이 넘었습니다. 할증이 필요한경우 이 메소드를 오버라이드 하세요.");
    }
}

public class TaxiExam{
    public static void main(String[] args){
        Taxi taxi = new Taxi();
        
        taxi.start();
        taxi.afterMidnight();
        taxi.stop(10);
    } 
}