/*
문제 설명
main에서는 다양한 조건의 Car객체를 만들어서 cars라는 리스트에 넣습니다. 이 cars라는 리스트에 있는 차를 검색해서 조건에 맞는 차를 출력하는 예제들을 살펴볼 텐데요. 첫 번째로 가격이 2000보다 싼 차량을 검색해서 이름을 출력하는 printCarCheaperThan이라는 함수가 있습니다.
코드를 확인하고 [실행]해서 결과를 확인하세요. [제출]하면 다음 문제로 이동합니다.
*/

import java.util.*;
public class CarExam{
    public static void main(String[] args){
        //Car객체를 만들어서 cars에 넣습니다.
        List<Car> cars = new ArrayList<>();
        cars.add( new Car("작은차",2,800,3) );
        cars.add( new Car("봉고차",12,1500,8) );
        cars.add( new Car("중간차",5,2200,0) );
        cars.add( new Car("비싼차",5,3500,1) );
        
        printCarCheaperThan(cars, 2000);
    }
    
    public static void printCarCheaperThan(List<Car> cars, int price){
        for(Car car : cars){
            if(car.price < price){
                System.out.println(car);
            }
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