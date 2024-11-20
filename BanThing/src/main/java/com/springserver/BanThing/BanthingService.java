package com.springserver.BanThing;

import com.springserver.BanThing.BanthingRequest;
import com.springserver.BanThing.banthingtest;
import com.springserver.BanThing.BanthingRepository;
import com.springserver.BanThing.BanthingService;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import jakarta.transaction.Transactional;
import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class BanthingService {
    private final BanthingRepository banthingRepository;
    // 글 수정
    @Transactional
    public Long update(Long id, BanthingRequest requestDto) {
        banthingtest banthing = banthingRepository.findById(id).orElseThrow(
                () -> new IllegalArgumentException("해당 아이디가 존재하지 않습니다.")
        );
        banthing.update(requestDto);
        return banthing.getId();
    }

}