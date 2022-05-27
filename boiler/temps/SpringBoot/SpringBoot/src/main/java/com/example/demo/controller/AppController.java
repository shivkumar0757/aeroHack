package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;


@RestController
public class AppController {
	@CrossOrigin
	@GetMapping("/")
	public String index() {
		String data= "{status':'success','data':[{'id':1,'employee_name':'Tiger Nixon','employee_salary':320800,'employee_age':61,'profile_image':''},{'id':2,'employee_name':'Garrett Winters','employee_salary':170750,'employee_age':63,'profile_image':''}],'message':'Successfully! All records has been fetched.'}";

		return data;
	}
	@CrossOrigin
	@GetMapping("/ping")
	ResponseEntity<String> ping() {
    return new ResponseEntity<>("OK", HttpStatus.OK);
}

}