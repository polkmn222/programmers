/*
문제 설명
data.txt에는 int형의 숫자가 3개 연속으로 들어있습니다. DataInputStream을 이용해 값을 읽어들인 다음 sum에 저장하세요.
*/

import java.io.*;

public class DataInputStreamExam{
    public static int read3(){
        int sum = 0;
        //data.txt로부터 int값 3개를 읽어들여서 sum에 더하세요.
       try(DataInputStream dis=new DataInputStream(new FileInputStream("data.txt"));) {
            int num=-1;
            while((num=dis.readInt())!=-1) {
                sum+=num;
            }
        } catch(Exception e){
        }
        
        //아래는 테스트를 위한 코드입니다. 수정하지 마세요.     
        return sum;
    }
}