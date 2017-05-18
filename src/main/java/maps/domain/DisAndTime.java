package maps.domain;

import lombok.Data;

/**
 * Created by zany on 5/14/17.
 * The instance of this class is treated as response from DisAndTime service
 */
public @Data class DisAndTime {

    private String distance;
    private int disValue;
    private String time;
    private int timeValue;
    private String origin;
    private String destination;
    private String mode;
//
//    DisAndTime() {}
//
//    public DisAndTime(String distance, String time, String origin, String destination, String mode) {
//        this.distance = distance;
//        this.time = time;
//        this.origin = origin;
//        this.destination = destination;
//        this.mode = mode;
//    }
//
//    public String getOrigin() {
//        return origin;
//    }
//
//    void setOrigin(String origin) {
//        this.origin = origin;
//    }
//
//    public String getDestination() {
//        return destination;
//    }
//
//    void setDestination(String destination) {
//        this.destination = destination;
//    }
//
//    public String getMode() {
//        return mode;
//    }
//
//    public void setMode(String mode) {
//        this.mode = mode;
//    }
//
//    public String getDistance() {
//        return distance;
//    }
//
//    void setDistance(String distance) {
//        this.distance = distance;
//    }
//
//    public String getTime() {
//        return time;
//    }
//
//    void setTime(String time) {
//        this.time = time;
//    }
}
