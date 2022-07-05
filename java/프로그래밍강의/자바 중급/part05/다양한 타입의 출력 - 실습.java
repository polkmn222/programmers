/*
문제 설명
다음 파일의 out을 이용해서 data.txt에 int값 100, double값 3.14를 순서대로 저장하세요.
*/

import java.io.*;

public class DataOutputStreamExam{
    public static void main(String[] args){
        
        try(
            //try의 뒤에나오는 괄호()사이에서 만든 stream은 별도로 close하지 않아도 됩니다.
            DataOutputStream out = new DataOutputStream(new FileOutputStream("data.txt"));
        ){
        //이 아래에 out을 이용해서 data.txt에 int값 100, double값 3.14를 저장하세요.
            out.writeInt(100);           
            // out.writeBoolean(true);      
            out.writeDouble(3.14);
        
        }
        catch(Exception e){      
        }
    }
}