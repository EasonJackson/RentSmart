package maps.domain;

import java.util.List;

/**
 * Created by zany on 5/14/17.
 * Model to receive Google maps distance matrix API response.
 * This model maps each field in JSON response.
 */
public class GoogleResponse {

    private String status;
    private List<String> destination_addresses;
    private List<String> origin_addresses;
    private List<Row> rows;

    public GoogleResponse() {}

    public GoogleResponse(String status, List<String> destination_addresses, List<String> origin_addresses, List<Row> rows) {
        this.status = status;
        this.destination_addresses = destination_addresses;
        this.origin_addresses = origin_addresses;
        this.rows = rows;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<String> getDestination_addresses() {
        return destination_addresses;
    }

    public void setDestination_addresses(List<String> destination_addresses) {
        this.destination_addresses = destination_addresses;
    }

    public List<String> getOrigin_addresses() {
        return origin_addresses;
    }

    public void setOrigin_addresses(List<String> origin_addresses) {
        this.origin_addresses = origin_addresses;
    }

    public List<Row> getRows() {
        return rows;
    }

    public void setRows(List<Row> rows) {
        this.rows = rows;
    }

    @Override
    public String toString() {
        return  "status: " + status + "\n" +
                "destination: " + destination_addresses.get(0) + "\n" +
                "origin: " + origin_addresses.get(0) + "\n" +
                "rows: " + rows.get(0) + "\n";
    }

    public DisAndTime toDisAndTime() {
        DisAndTime disAndTime = new DisAndTime();
        disAndTime.setDestination(destination_addresses.get(0));
        disAndTime.setOrigin(origin_addresses.get(0));
        disAndTime.setDistance(rows.get(0).getElements().get(0).getDistance().getText());
        disAndTime.setTime(rows.get(0).getElements().get(0).getDuration().getText());
        return disAndTime;
    }
}
