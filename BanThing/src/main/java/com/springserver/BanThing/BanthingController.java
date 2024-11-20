package com.springserver.BanThing;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController // JSON으로 데이터를 주고받음을 선언합니다.
public class BanthingController {
    private final BanthingService banthingService;

    public BanthingController(BanthingService banthingService) {
        this.banthingService = banthingService;
    }

    // 글 수정
    @RequestMapping(value="/banthing",method=RequestMethod.PATCH)
    public String update(@RequestBody BanthingRequest requestDto) {
        //System.out.println("성공");
        //return banthingService.update(id,requestDto);
        return "성공";
    }

}