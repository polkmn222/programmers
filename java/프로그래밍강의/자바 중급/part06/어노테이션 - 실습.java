/*
문제 설명
어노테이션은 메소드가 특정한 방식으로 동작하도록 표시하는데 쓸 수 있는데요. @RunTwice 어노테이션을 AnnotationExam의 원하는 메소드에 붙여보고 [제출]을 눌러보세요. 해당 메소드가 두 번 실행되는 걸 확인할 수 있습니다.
*/

import java.lang.reflect.Method;

public class AnnotationExam{
    //메소드1~3중 원하는 부분에 @RunTwice 어노테이션을 붙여보세요.
    
    @RunTwice
    public void method1(){
        System.out.println("메소드 1 입니다.");
    }
    
    public void method2(){
        System.out.println("메소드 2 입니다.");
    }
    
    public void method3(){
        System.out.println("메소드 3 입니다.");
    }
    
    public static void main(String[] args){
        AnnotationExam exam = new AnnotationExam();
        
        try {
            Method method = exam.getClass().getDeclaredMethod("method1");
            if(method.isAnnotationPresent(RunTwice.class)){
                exam.method1();exam.method1();
            }
        
        method = exam.getClass().getDeclaredMethod("method2");
        if(method.isAnnotationPresent(RunTwice.class)){
            exam.method2();exam.method2();
        }
        
        method = exam.getClass().getDeclaredMethod("method3");
        if(method.isAnnotationPresent(RunTwice.class)){
            exam.method3();exam.method3();
        }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface RunTwice{

}