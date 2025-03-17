package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DataProcessorTest {
    @Test
    void testValidAverage() {
        DataProcessor processor = new DataProcessor();
        assertEquals(2.0, processor.calculateAverage(List.of(1, 2, 3)));
    }

    @Test
    void testEmptyCase() {
        // Empty test method
    }

    @Test
    void testDataProcessing() {
        DataProcessor processor = new DataProcessor();
        assertTrue(processor.processDataV1(List.of(1, 2)).contains(2)); // Poor assertion
    }

    @Test
    @Disabled("TODO: Implement later")
    void testSecurityChecks() {
        // Skipped test
    }
}
