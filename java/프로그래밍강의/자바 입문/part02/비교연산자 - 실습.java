/*
문제 설명
int 형 변수 a와 b가 주어집니다.1 주석이 지시하는 대로 다음 코드를 완성해 보세요.

c에는 a가 b보다 큰지 비교한 결과를 저장
d에는 a와 b가 같은지 비교한 결과를 저장
e에는 a와 b가 다른지 비교한 결과를 저장
c, d, e는 모두 boolean형 변수이므로 저장되는 값은 true 또는 false이어야 합니다.
*/

public class OperatorExam {
    public boolean[] calculate(int a, int b) {
        //변수 a와 b는 int형 변수입니다. 각각 어떤 값을 가지고 있는지는 비교해 보기 전에는 모릅니다.
        //a와 b가 주어져 있다고 가정하고 아래 지시에 따라 문제를 풀어 보세요.

        //a가 b보다 큰 지 비교한 결과(true 또는 false)를 c에 저장하세요.
        boolean c = (a > b);


        //a와 b가 같은지 비교한 결과를 d에 저장하세요.
        boolean d = (a == b);


        //a와 b가 다른지 비교한 결과를 e에 저장하세요.
        boolean e = (a != b);


        //이 아래 코드는 결과 테스트를 위한 코드입니다.
        boolean ret[] = {c, d, e};
        return ret;
    }

    public static void main(String[]args){
        int a = (int)(Math.random() * 10);
        int b = (int)(Math.random() * 10);
        new OperatorExam().calculate(a, b);
    }
}