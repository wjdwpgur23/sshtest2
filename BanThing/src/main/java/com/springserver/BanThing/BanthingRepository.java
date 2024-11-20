package com.springserver.BanThing;

import com.springserver.BanThing.banthingtest;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BanthingRepository extends JpaRepository<banthingtest, Long> {
}