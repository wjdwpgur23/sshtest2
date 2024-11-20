package com.springserver.BanThing;

import lombok.Getter;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@Getter
public class BanthingRequest {

    private String hashtag;

    private String content;

    public BanthingRequest(String hashtag, String content) {
        this.hashtag = hashtag;
        this.content = content;
    }
}