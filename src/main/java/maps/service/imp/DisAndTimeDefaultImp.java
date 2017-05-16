package maps.service.imp;

import maps.domain.DisAndTime;
import maps.domain.GoogleResponse;
import maps.service.DisAndTimeService;
import org.springframework.stereotype.Service;
import org.apache.http.client.utils.URIBuilder;
import org.springframework.web.client.RestTemplate;


/**
 * Created by zany on 5/14/17.
 * Serve calculation of distance and traveling time from origin and destination
 */
@Service
public class DisAndTimeDefaultImp implements DisAndTimeService {


    private static final String HOST = "maps.googleapis.com";
    private static final String PATH = "/maps/api/distancematrix/json";
    private static final String KEY = "AIzaSyCicbo5g2QmMOfViB1WHz3ua8kyP1oXDlU";

    /**
     * This method provides core service logic. It takes three inputs and gives a DisAndTime object
     * as output.
     * @param origin address depart from
     * @param desti address arrive at
     * @param mode the mean of transportation
     * @return DisAndTime object
     */
    public DisAndTime getDisAndTime(String origin,
                                    String desti,
                                    String mode) {
        // build uri for google maps API call
        URIBuilder builder = new URIBuilder();
        builder.setScheme("https");
        builder.setHost(HOST);
        builder.setPath(PATH);
        builder.addParameter("units","imperial");   // response unit in mile
        builder.addParameter("origins", origin);
        builder.addParameter("destinations", desti);
        builder.addParameter("mode", mode);
        builder.addParameter("key", KEY);                //  distance matrix key


        RestTemplate restTemplate = new RestTemplate();
        GoogleResponse response = restTemplate.getForObject(builder.toString(), GoogleResponse.class);

        // convert google response to DisAndTime object
        DisAndTime disAndTime = response.toDisAndTime();
        disAndTime.setMode(mode);
        return disAndTime;
    }
}
