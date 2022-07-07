/*
문제 설명
이번에는 조건이 더 복잡한 경우입니다. 내부클래스를 이용해서 CheckCar라는 인터페이스를 만들고, 그걸 구현하는 CheckCarForBigAndNotExpensive클래스를 만들어서 4명 이상이 탈 수 있고, 가격이 2500이하인 차를 검색합니다.
[실행]해 보고 결과를 확인하세요. [제출]하면 다음 문제로 이동합니다.
*/

import java.util.*;
public class CarExam{
    public static void main(String[] args){
        List<Car> cars = new ArrayList<>();
        cars.add( new Car("작은차",2,800,3) );
        cars.add( new Car("봉고차",12,1500,8) );
        cars.add( new Car("중간차",5,2200,0) );
        cars.add( new Car("비싼차",5,3500,1) );
        
        printCar(cars, new CheckCarForBigAndNotExpensive());
    }
    
    public static void printCar(List<Car> cars, CheckCar tester){
        for(Car car : cars){
            if (tester.test(car)) {
                System.out.println(car);
            }
        }
    }
    
    interface CheckCar{
        boolean test(Car car);
    }
    
    //내부클래스를 만들어서 사용합니다.
    static class CheckCarForBigAndNotExpensive implements CheckCar{
        public boolean test(Car car){
            return car.capacity >= 4 && car.price < 2500;
        }
    }
}

public class Car{
    public String name;
    public int capacity;  
    public int price;
    public int age;
    
    public Car(String name, int capacity, int price, int age){
        this.name = name;
        this.capacity = capacity;
        this.price = price;
        this.age = age;
    }
    
    public String toString(){
        return name;
    }
}