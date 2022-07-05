/*
문제 설명
hundredDaysAfter메소드에서 지금부터 100일 이후가 몇 월 며칠인지를 문자열로 만들어서 return하세요. 예를 들어 100일 이후가 2016년 1월 1일 19시라면 "2016년1월1일"라는 문자열을 return하면 됩니다.
*/

import java.util.*;

public class CalendarExam{
    public String hundredDaysAfter(){
        //오늘부터 100일 뒤의 날짜를 "2016년1월1일"의 형식으로 return하세요.
        Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE, 100);
        int yyyy = cal.get(Calendar.YEAR);             
        int month = cal.get(Calendar.MONTH) + 1;      
        int date = cal.get(Calendar.DATE);
        String arr = "";
        arr = yyyy + "년" + month + "월" + date + "일";
        return arr;

    }
    public static void main(String[] args){}
}