import java.util.Scanner;

public class WordCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter a sentence:");
        String input = scanner.nextLine();
        
        int wordCount = countWords(input);
        
        System.out.println("Number of words: " + wordCount);
    }
    
    public static int countWords(String input) {
        if (input == null || input.trim().isEmpty()) {
            return 0;
        }
        String[] words = input.trim().split("\\s+");
        return words.length;
    }
}