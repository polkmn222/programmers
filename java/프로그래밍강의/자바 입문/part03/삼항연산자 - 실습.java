/*
문제 설명
변수 hour에는 현재 시각이 들었습니다.1 hour가 12보다 작으면 "오전", 그렇지 않으면 "오후"라는 값을 ampm에 저장하도록 빈칸을 채워주세요.
*/

import java.util.Calendar;
public class TernaryExam {
    public static void main(String[] args) {
        // hour에는 현재 시간이 24시간 단위로 들어 있습니다. 
        int hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
        String ampm;
        // 삼항연산자를 이용해서 ampm의 값을 "오전" 또는 "오후"로 만들어보세요.
        ampm = 12 > hour ? "오전" : "오후";

        System.out.println("지금시간은 " + hour + "시이고, " + ampm + "입니다.");
    }
}