/*
문제 설명
다음 코드는 set에 a를 두 번 더하고, b를 한 번 더합니다. 출력해 보면 a와 b가 각각 한 번씩만 출력되는데요. set은 이미 있는 값이면 값을 더해도 2개가 아니라 하나의 값만 유지하기 때문입니다. [제출]을 눌러서 출력을 확인해 보세요.

참고: set의 내용은 for each문 또는 Iterator를 활용해서 출력할 수 있습니다. for each문을 복습하려면 이 링크를 참고하세요.
*/

import java.util.*;

public class SetExam{
    public static void main(String[] args){
        Set<String> set = new HashSet<String>();
        set.add("a");
        set.add("a");
        set.add("b");
        
        System.out.println("set의 내용을 출력합니다.");
        for(String str : set){
            System.out.println(str);
        }
    }
}