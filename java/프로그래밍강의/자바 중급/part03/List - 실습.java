/*
문제 설명
List는 길이가 정해져 있지 않기 때문에 길이를 알 수 없는 배열을 더할때 유용하게 사용할 수 있습니다. 다음 코드의 addArray는 매개변수로 두개의 String배열을 받고 있는데요. arr1과 arr2의 각 값을 순서대로 list에 저장해서 return하도록 만들어 보세요.
*/

import java.util.*;

public class ListExam{
    public List<String> addArray(String[]arr1, String[]arr2){
        List<String> list = new ArrayList<String>();
        
        for(String str : arr1){
            System.out.println(str);   
            list.add(str);
        }

        for(String str : arr2){
            System.out.println(str);
            list.add(str);    
        }
//         for(int i=0; i<list.size(); i++) {
//             list.add(arr1[i]);
//         }
        
//         for(int i=0; i<list.size(); i++) {
//             list.add(arr2[i]);
//         }
        
//         for(String str : arr1){
//             System.out.println(str);     
//         }
        
       
        
//         for(String str : arr2){
//             System.out.println(str);
//         }
        
        
        
        
        return list;
    }
    
    public static void main(String[] args){
    }
}