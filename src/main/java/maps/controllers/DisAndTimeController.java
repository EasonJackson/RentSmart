package maps.controllers;

import maps.DisAndTime;
import maps.services.DisAndTimeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.atomic.AtomicLong;

/**
 * Created by zany on 5/14/17.
 */
@RestController
public class DisAndTimeController {

    // service instance
    @Autowired
    private DisAndTimeService disAndTimeService;


    /**
     * Entrance of distance and time service. Use DisAndTime service to return a DisAndTime object which
     * has the distance and time information between two addresses.s
     * @param origin address depart from, could be either string address or coordinate
     * @param desti address arrive at, could be either string address or coordinate
     * @param mode mean of transportation, driving(default), walking, bicycling, and transit
     * @return
     */
    @RequestMapping("/disandtime")
    public DisAndTime getDisAndTime(@RequestParam(value = "origin") String origin,
                                    @RequestParam(value = "desti") String desti,
                                    @RequestParam(value = "mode", defaultValue = "driving") String mode) {


        return disAndTimeService.getDisAndTime(origin,desti,mode);

    }
}
