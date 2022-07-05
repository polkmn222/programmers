/*
문제 설명
array는 길이를 알 수 없는 int형 배열입니다. array의 원소를 모두 합한 값을 sum에 저장하세요.

힌트: array의 길이를 알 수 없다면 어떻게 해야 할까요?

array.length를 사용하면 array 배열의 길이를 읽어올 수 있습니다.
다음은 배열의 원소를 모두 곱한 값을 출력하는 코드입니다.

// 곱을 저장할 변수는 반복문 밖에서 선언합니다.
int mul = 1;

for(int i = 0; i < array.length; i++){ 
    mul = mul * array[i];
}

System.out.println(mul);
*/

public class ArrayExam {
    public int sum(int[] array) {
        int sum = 0;
        // array는 길이를 알 수 없는 int형 배열입니다.
        // 변수 sum에 array의 모든 값을 더해보세요.
        for(int i=0; i<array.length; i++) {
            sum += array[i];
        }
        // 아래는 결과 평가를 위한 코드입니다. 수정하지 마세요.
        return sum;
    }
    
    // 아래는 실행을 위한 코드입니다. 수정하지 마세요.
    public static void main(String[] args) {
        int[] testcase1 = {1, 2, 3, 4};
        int[] testcase2 = {5, 6, 7};
        ArrayExam exam = new ArrayExam();

        int answer1 = exam.sum(testcase1);        
        int answer2 = exam.sum(testcase2);        
        if (answer1 == 10 && answer2 == 18)
            System.out.println("정답입니다. [제출]을 누르세요.");
        else {
            System.out.println("틀렸습니다.");
            System.out.printf("1, 2, 3, 4를 더했는데 %d가 나왔네요.\n", answer1);
            System.out.printf("5, 6, 7을 더했는데 %d가 나왔네요.\n", answer2);
        }
    }
}