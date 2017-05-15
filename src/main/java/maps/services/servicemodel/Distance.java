package maps.services.servicemodel;

/**
 * Created by zany on 5/14/17.
 * sub-element of Element
 */
public class Distance {

    private String text;
    private int value;

    public Distance() {}

    public Distance(String text, int value) {
        this.text = text;
        this.value = value;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return  "text: " + text + "\n" +
                "value: " + value + "\n";
    }
}
