package com.springserver.BanThing;

import com.springserver.BanThing.BanthingRequest;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import jakarta.persistence.*;

@Setter
@Getter // get 함수를 일괄적으로 만들어줍니다.
@NoArgsConstructor // 기본 생성자를 만들어줍니다.
@Entity
public class banthingtest extends Timestamped {
    // 글 고유 아이디
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    private Long id;

    // 글 제목
    @Column(nullable = false)
    private String hashtag;

    // 글 내용
    @Column(nullable = false)
    private String content;

    // requestDto 정보를 가져와서 entity 만들 때 사용
    public banthingtest(BanthingRequest requestDto) {
        this.hashtag = requestDto.getHashtag();
        this.content = requestDto.getContent();
    }

    // 업데이트 메소드
    public void update(BanthingRequest requestDto) {
        this.hashtag = requestDto.getHashtag();
        this.content = requestDto.getContent();
    }
}