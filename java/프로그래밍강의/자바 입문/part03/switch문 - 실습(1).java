/*
문제 설명
변수 month에는 지금이 몇월인지 나타내는 숫자가 들었습니다.1 switch문을 이용해서 season에 현재 계절을 저장하는 코드를 완성해보세요.

편의상 계절은 다음과 같이 나눕니다.

계절	기간
겨울	12월 ~ 2월
봄	3월 ~ 5월
여름	6월 ~ 8월
가을	9월 ~ 11월
*/

import java.util.Calendar;
public class SwitchExam {
    public static void main(String[] args) {
        // month에는 오늘이 몇 월인지 들어 있습니다.
        int month = Calendar.getInstance().get(Calendar.MONTH) + 1;
        String season = "";
        // switch문을 이용해서 season이 오늘은 어떤 계절인지 나타내게 만들어보세요.
        switch(month) {
            case 3: case 4: case 5:
                season = "봄";
                break;
            case 6: case 7: case 8:
                season = "여름";
                break;
            case 9: case 10: case 11:
                season = "가을";
                break;
            case 12: case 1: case 2:
                season = "겨울";
                break;    
        }
        
        System.out.println("지금은 " + month + "월이고, " + season + "입니다.");
    }
}