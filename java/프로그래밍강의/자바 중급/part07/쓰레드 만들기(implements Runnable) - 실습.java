/*
문제 설명
자바에서는 두 개의 클래스로부터 상속을 받을 수 없으므로 이미 상속을 받은 클래스가 쓰레드로 동작하려면 Runnable인터페이스를 구현해야 합니다. Bus클래스는 Car를 상속받은 상태인데요. Bus클래스가 쓰레드로 동작할 수 있게 Runnable인터페이스를 구현하고 run메소드를 오버라이드 해 보세요.
*/

public class Bus extends Car implements Runnable{
  //이미 Car를 상속받은 상태이기 때문에 Thread를 상속받을 수는 없습니다.
  //Runnable인터페이스를 implements하고 run메소드를 작성해 보세요.

    String str;

    public Bus(){

    }

    public Bus(String str){
        this.str = str;
    }

    public void run(){
        for(int i=0; i<5; i++){
            System.out.println(str);

            try{
                Thread.sleep(1000);
            }catch(Exception e){
                e.printStackTrace();
            }
        }
    }


}

public class Car{
    public String name;
    public int number;
    
    public void drive(){
        System.out.println("차가 달립니다.");
    }
}

public class RunnableExam{
    public static void main(String [] argv){
        Bus bus = new Bus();
        /*
        Runnable을 구현한 클래스를 이용해 쓰레드를 이용할때는
        아래와 같이 Thread의 생성자에 해당 객체(bus)를 전달하면 됩니다.
        하지만 이대로 실행하면 에러가 발생합니다.
        bus가 runnable을 implements하고 있지 않기 때문입니다.
        */
        Thread busThread = new Thread(bus);
        busThread.start();
    }
}

