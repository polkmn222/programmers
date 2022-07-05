/*
문제 설명
LocalDateTime을 이용해서 지금이 몇 월인지를 영어로 출력해 보세요. 예를들어 지금이 1월이면 "JANUARY", 2월이면 "FEBRUARY"라고 출력되어야 합니다.
*/

import java.time.LocalDateTime;


public class TimeExam{
    public static void main(String[] args){
        //지금이 몇월인지를 영어로(예. 1월이면 JANUARY, 2월이면 FEBRUARY) 출력하세요
        LocalDateTime LDT = LocalDateTime.now();
        String mon = LDT.getMonth() + "";
        System.out.println(mon);
        
    }
}