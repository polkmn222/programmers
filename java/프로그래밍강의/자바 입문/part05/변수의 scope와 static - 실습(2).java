/*
문제 설명
※ 본 문제는 두 코드 파일, Car.java와 CarExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

다음 코드에서 taxi의 wheelCount와 suv의 wheelCount는 서로 다른 값을 저장한 것 처럼 보이지만, 둘은 모두 마지막에 지정한 4라는 값을 가집니다. (코드 7번째 줄 참고) 이는 Car클래스의 wheelCount가 static 변수이기 때문입니다.

코드를 제출해서 정말 둘이 같은 값을 가지는지 확인해 보세요.
*/


public class StaticExam{
    public static void main(String []args){
        Car taxi = new Car();
        Car suv = new Car();
        
        taxi.wheelCount = 10;
        suv.wheelCount = 4;
        
        System.out.println("taxi의 바퀴수:"+ taxi.wheelCount);
        System.out.println("suv의 바퀴수:"+ suv.wheelCount);
    }
}

public class Car{
    static int wheelCount;
}