/*
제 설명
Meter(택시 미터기)인터페이스는 start와 stop이라는 추상 메소드를 가지고 있습니다. stop메소드는 달린 거리에 해당하는 값(distance)를 매개변수로 받아 요금을 int형으로 반환하는 메소드입니다. Meter인터페이스를 구현하는 택시 클래스를 완성해 보세요. 요금은 distance x 2로 계산하세요.
*/

public class Taxi implements Meter {
    // Meter인터페이스의 start와 stop메소드를 구현해야 합니다.
    public int distance;
	
	
	protected Taxi() {
		distance = 0;
	}

	@Override
	public void start() {
		System.out.println("출발합니다.");
		
	}

	@Override
	public int stop(int distance) {
		int a = distance;
		return a*2;
	}
}

public interface Meter {
    public abstract void start();
    public abstract int stop(int distance);
}

// 아래는 실행을 위한 코드입니다. 수정하지 마세요.
public class MeterExam {
    public static void main(String[]args){
        Taxi taxi = new Taxi();
        boolean a = Meter.class.isInstance(taxi);
        
        if(a!=true){
            System.out.println("Taxi클래스는 Meter인터페이스를 구현해야 합니다.");
        }
        else if(taxi.stop(200)!=400){
            System.out.println("stop(200)의 값은 400이어야 합니다.");
        }
        else{
            System.out.println("정답입니다. [제출]을 누르세요.");
        }
    }
}