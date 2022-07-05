/*
문제 설명
다음 클래스의 main 메소드에서는 별모양 문자(*)가 10,000개 이어진 문자열을 만들기 위해 두가지 방법을 사용합니다. 하나는 String에 +연산을 이용하고, 다른 하나는 StringBuffer의 append()를 이용하는데요. 똑같은 문자열을 만들어 내는데 걸리는 시간을 측정해서 마지막 줄에서 출력하고 있습니다.
제출을 눌러 실행 결과를 비교해 보세요. 똑같은 작업을 수행하는데 성능에서 수십배의 차이가 나는걸 확인할 수 있나요?
*/

public class StringBufferPerformanceTest{
    public static void main(String[] args){
        // (1) String의 +연산을 이용해서 10,000개의 *를 이어붙입니다.
        //시작시간을 기록합니다.(millisecond단위)
        long startTime1 = System.currentTimeMillis();
        String str="";
        for(int i=0;i<10000;i++){
            str=str+"*";
        }
        //종료시간을 기록합니다.(millisecond단위)
        long endTime1 = System.currentTimeMillis();
        
        // (2) StringBuffer를 이용해서 10,000개의 *를 이어붙입니다.
        //시작시간을 기록합니다.(millisecond단위)                
        long startTime2 = System.currentTimeMillis();
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<10000;i++){
            sb.append("*");
        }
        //종료시간을 기록합니다.(millisecond단위)
        long endTime2 = System.currentTimeMillis();
        
        // 방법(1)과 방법(2)가 걸린 시간을 비교합니다.
        long duration1 = endTime1-startTime1;
        long duration2 = endTime2-startTime2;
        
        System.out.println("String의 +연산을 이용한 경우 : "+ duration1);
        System.out.println("StringBuffer의 append()을 이용한 경우 : "+ duration2);
    }
}