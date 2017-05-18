package maps.domain;

import lombok.Data;

/**
 * Created by zany on 5/14/17.
 * sub-element of Element
 */
public @Data class Duration {

    private String text;
    private int value;

//    public Duration() {}
//
//    public Duration(String text, int value) {
//        this.text = text;
//        this.value = value;
//    }
//
//    String getText() {
//        return text;
//    }
//
//    public void setText(String text) {
//        this.text = text;
//    }
//
//    public int getValue() {
//        return value;
//    }
//
//    public void setValue(int value) {
//        this.value = value;
//    }
//
//    @Override
//    public String toString() {
//        return  "text: " + text + "\n" +
//                "value: " + value + "\n";
//    }
}
