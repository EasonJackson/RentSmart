package maps.service;

import maps.domain.DisAndTime;

/**
 * Created by zany on 5/16/17.
 * Interface of distance and time calculation. This interface provides isolation between
 * concrete implementation and usage from DisAndTimeController
 */
public interface DisAndTimeService {

    DisAndTime getDisAndTime(String origin,
                                    String desti,
                                    String mode);
}
