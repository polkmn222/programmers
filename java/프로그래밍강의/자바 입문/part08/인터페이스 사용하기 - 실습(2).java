/*
문제 설명
인터페이스에서 정의한 변수는 모두 상수이기 때문에 변경할 수 없습니다. 때문에 다음 코드를 실행하면 TaxiExam.java의 4번째 줄에서 "cannot assign a value to final variable BASE_FARE"라는 에러가 발생합니다. 오류를 수정하고 문제를 해결해 보세요.
*/

public class Taxi implements Meter{
    
    public static int BASE_FARE;
	
	public Taxi() {
		BASE_FARE = 3000;
	}
    
    public void start(){
        System.out.println("운행을 시작합니다.");
    }
    
    public int stop(int distance){
        int fare = BASE_FARE + distance * 2;
        System.out.println("운행을 종료합니다. 요금은 " + fare + "원 입니다.");
        return fare;
    }
}

public interface Meter{
    public int BASE_FARE = 3000; // 기본요금(인터페이스에 정의한 변수는 상수라서 변경할 수 없습니다.)
    public abstract void start();
    public abstract int stop(int distance);
}

public class TaxiExam{
    public static void main(String []args){
        Taxi taxi = new Taxi();
        taxi.BASE_FARE = 2500;
    }
}