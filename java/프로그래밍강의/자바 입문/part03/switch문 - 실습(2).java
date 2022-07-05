/*
문제 설명
같은 동작을 하는 case문은 이렇게 한 번에 처리할 수 있습니다. 코드를 실행해 결과를 확인해 보세요.
*/

import java.util.Calendar;
public class SwitchExam {
    public static void main(String[] args) {
        // 오늘이 몇 월인지 month에 저장합니다.
        int month = Calendar.getInstance().get(Calendar.MONTH) + 1;
        String season = "";
        
        // 다음과 같이 case문을 한번에 사용하면 더 짧게 코드를 짤 수 있습니다.
        switch(month) {
            case 1: case 2: case 12:
                season = "겨울";
                break;
            case 3: case 4: case 5:
                season = "봄";
                break;
            case 6: case 7: case 8:
                season = "여름";
                break;
            case 9: case 10: case 11:
                season = "가을";
                break;
        }
        System.out.println("지금은 " + month + "월이고, " + season + "입니다.");
    }
}