package com.application1.analysisbroker.web;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import org.springframework.http.HttpHeaders;
import org.springframework.web.util.UriComponents;
import org.springframework.web.util.UriComponentsBuilder;

@RequiredArgsConstructor
@RestController
public class AnalysisApiController {

    @GetMapping("/analysis/module1")
    public String request(@RequestParam("url") String crawlUrl) {
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders header = new HttpHeaders();
        HttpEntity<?> entity = new HttpEntity<>(header);
        String host = "http://localhost:5001";
        UriComponents uri = UriComponentsBuilder.fromHttpUrl(host+"/curl/"+crawlUrl).build();

        ResponseEntity<String> resultString = restTemplate.exchange(uri.toString(), HttpMethod.GET, entity, String.class);
        ObjectMapper mapper = new ObjectMapper();
        String responseString = "";
        try {
            responseString = mapper.writeValueAsString(resultString.getBody());
        }
        catch (Exception e) {
            System.out.print(e.toString());
        }
        return responseString;
    }
}
