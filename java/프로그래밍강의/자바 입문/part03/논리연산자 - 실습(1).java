/*
문제 설명
어떤 사람이 할인 대상인지 검사하려고 합니다. 나이가 19 이하거나 60 이상이라면 할인 대상입니다.

int형 변수 age가 19 이하거나 60 이상이라면 isDiscount에 true를, 아니라면 isDiscount에 false를 저장하게 빈칸을 채워보세요.
*/

public class LogicalOperatorExam {
    public boolean isAgeDiscountable(int age) {
        boolean isDiscount = false;
        // 아래 빈칸을 채워 코드를 완성하세요.
        if( age <= 19 || age >= 60) {
            isDiscount = true;
        }
        else {
            isDiscount = false;
        }
        return isDiscount;
    }

    public static void main(String[]args) {
        LogicalOperatorExam exam = new LogicalOperatorExam();
        exam.isAgeDiscountable(15);
        exam.isAgeDiscountable(27);
    }
}