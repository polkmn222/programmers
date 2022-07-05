/*
문제 설명
products는 상품의 이름을 key로 가격을 값으로 가지는 Map입니다. "가위"는 2500원, "크레파스"는 5000원이 되도록 products에 값을 추가해 보세요.
*/

import java.util.*;

public class MapExam{
    public Map<String, Integer> makeMap(){
        Map<String, Integer> products = new HashMap<>();
        //상품의 이름과 값을 products에 추가해 보세요.
        products.put("가위", 2500);
        products.put("크레파스", 5000);
        
        return products;
    }
    
    public static void main(String[] args){
    }
}