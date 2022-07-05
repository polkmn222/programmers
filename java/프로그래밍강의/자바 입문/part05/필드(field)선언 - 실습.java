/*
문제 설명
※ 본 문제는 두 코드 파일, Song.java와 SongExam.java로 구성되어있습니다. 파일 이름을 클릭하면 파일 내용물을 볼 수 있습니다.

음악 정보를 나타내는 클래스, Song을 완성하려 합니다. Song 클래스에 다음 필드를 선언해보세요.

필드의 의미	필드 이름	필드 타입
노래 제목을 저장	songTitle	String
가수 이름을 저장	singer	String
속한 앨범 이름을 저장	albumName	String
앨범의 트랙 번호를 저장	trackNumber	int
*/

public class Song {
    // 이곳에 코드를 작성하세요.
    String songTitle;
    String singer;
    String albumName;
    int trackNumber;
    
}

// Song.java 코드를 실행하기 위한 코드입니다. 이 코드는 수정하지 마세요.
public class SongExam {
    public static void main(String[] args) {
        Song song = new Song();
        song.songTitle = new String("곡명");
        song.singer = new String("가수");
        song.albumName = new String("앨범");
        song.trackNumber = 5;
    }
}
