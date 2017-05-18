package maps.domain;

import lombok.Data;

/**
 * Created by zany on 5/14/17.
 * sub-element of Row.
 */
public @Data class Element {

    private String status;
    private Distance distance;
    private Duration duration;

//    public Element() {}
//
//    public Element(String status, Distance distance, Duration duration) {
//        this.status = status;
//        this.distance = distance;
//        this.duration = duration;
//    }
//
//    public String getStatus() {
//        return status;
//    }
//
//    public void setStatus(String status) {
//        this.status = status;
//    }
//
//    Distance getDistance() {
//        return distance;
//    }
//
//    public void setDistance(Distance distance) {
//        this.distance = distance;
//    }
//
//    Duration getDuration() {
//        return duration;
//    }
//
//    public void setDuration(Duration duration) {
//        this.duration = duration;
//    }
//
//    @Override
//    public String toString() {
//        return  "status: " + status + "\n" +
//                "distance: " + distance +
//                "duration: " + duration + "\n";
//    }
}
