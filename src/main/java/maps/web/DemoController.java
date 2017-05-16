package maps.web;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by zany on 5/14/17.
 * A demo controller example
 */
@RestController
public class DemoController {

    @RequestMapping("/demo")
    public String demo() {
        return "controller configuration successful.";
    }
}
