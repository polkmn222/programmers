/*
문제 설명
PrintWriter를 통해 data.txt파일에 "안녕하세요. PrintWriter입니다."라고 적어보세요.
*/

import java.io.*;

public class CharIOExam{
    public static void main(String[]args){
        PrintWriter pw = null;
        try{
            pw = new PrintWriter(new FileWriter("data.txt"));
            pw.println("안녕하세요. PrintWriter입니다.");

        }catch(Exception e){
            e.printStackTrace();
        }finally{
            pw.close();
        }
    }
}