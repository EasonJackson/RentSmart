package maps.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by zany on 5/14/17.
 */
@RestController
public class DemoController {

    @RequestMapping("/demo")
    public String demo() {
        return "controller configuration successful.";
    }
}
