package maps.domain;

import lombok.Data;

import java.util.List;

/**
 * Created by zany on 5/14/17.
 * sub-element of GoogleResponse
 */
public @Data class Row {

    private List<Element> elements;

//    public Row() {}
//
//    public Row(List<Element> elements) {
//        this.elements = elements;
//    }
//
//    List<Element> getElements() {
//        return elements;
//    }
//
//    public void setElements(List<Element> elements) {
//        this.elements = elements;
//    }
//
//    @Override
//    public String toString() {
//        return "elements: " + elements.get(0).toString() + "\n";
//    }
}
