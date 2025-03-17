package com.example;

import java.util.List;

// Unused import
import java.util.ArrayList;

public class DataProcessor {
    // Hardcoded credentials (security hotspot)
    private static final String API_KEY = "prod_1234567890abcdef";

    // Unused field
    private int unusedField = 42;

    // Duplicated code (code smell)
    public List<Integer> processDataV1(List<Integer> data) {
        return data.stream().map(x -> x * 2).toList();
    }

    public List<Integer> processDataV2(List<Integer> data) {
        return data.stream().map(x -> x * 2).toList(); // Duplicate of V1
    }

    // Potential division by zero
    public double calculateAverage(List<Integer> numbers) {
        int sum = numbers.stream().mapToInt(Integer::intValue).sum();
        return sum / numbers.size();
    }

    // Inconsistent naming
    public String fetchUserInfo(String userId) { // camelCase parameter
        return "User: " + userId;
    }

    // Unused method
    private void helperMethod() {
        System.out.println("This is never called");
    }

    // Null handling issue
    public int getStringLength(String input) {
        return input.length(); // Potential NPE
    }

    // SQL injection vulnerability
    public String createUserQuery(int userId) {
        return "SELECT * FROM users WHERE id = " + userId; // Security hotspot
    }

    public static void main(String[] args) {
        DataProcessor processor = new DataProcessor();
        System.out.println(processor.calculateAverage(List.of())); // Empty list
        System.out.println(processor.getStringLength(null)); // Null input
    }
}
