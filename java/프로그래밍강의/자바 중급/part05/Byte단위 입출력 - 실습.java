/*
문제 설명
data.txt의 내용을 그대로 읽어서 copy.txt로 복사하려고 합니다. 12번째 줄 부터 fis와 fos를 이용해서 코드를 완성해 보세요.
*/

import java.io.*;

public class ByteReadWriteExam{
    public static void main(String[] args){
        FileInputStream fis = null;
        FileOutputStream fos = null;
        try{
            fis = new FileInputStream("data.txt");
            fos = new FileOutputStream("copy.txt");
            //data.txt의 파일을 읽어서 그대로 copy.txt에 복사하려고 합니다.
            //이 아래에서 fis와 fos를 이용해서 파일 복사를 완성해 보세요.
            
            int readData = -1;
            while((readData = fis.read()) != -1) {
                fos.write(readData);
            }
            
        }
        catch(Exception e){
            System.out.println(e);
        } 
        finally{
            //fis와 fos를 사용하고 나면 close해야 합니다.    
            try{
                fis.close();
                fos.close();
            }
            catch(Exception e){
                System.out.println(e);
            }
        }
    }
}