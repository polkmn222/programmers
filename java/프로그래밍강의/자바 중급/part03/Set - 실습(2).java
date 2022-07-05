/*
문제 설명
Iterator iter의 hasNext와 next메소드를 이용해서 set의 내용을 모두 출력해 보세요.
*/

import java.util.*;

public class SetExam{
    public static void main(String[] args){
        Set<String> set = new HashSet<String>();
        set.add("a");
        set.add("b");
        
        Iterator<String> iter = set.iterator();
        //iter를 이용해서 set의 내용을 출력하세요.
        while(iter.hasNext()) {
            String str = iter.next();
            System.out.println(str);
        }
    }
}