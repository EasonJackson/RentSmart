package maps;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

/**
 * Created by zany on 5/14/17.
 */
@SpringBootApplication
@EnableEurekaClient
public class MapsApp {

    public static void main(String[] args) {
        SpringApplication.run(MapsApp.class, args);
    }
}
