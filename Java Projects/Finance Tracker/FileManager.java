import java.io.*;
import java.util.List;

public class FileManager {

    private static final String FILE_NAME = "transactions.dat";

    public static void save(List<Transaction> transactions) {
        try (ObjectOutputStream out =
                     new ObjectOutputStream(new FileOutputStream(FILE_NAME))) {

            out.writeObject(transactions);

        } catch (IOException e) {
            System.err.println("Failed to save transactions");
            e.printStackTrace();
        }
    }

    @SuppressWarnings("unchecked")
    public static List<Transaction> load() {
        File file = new File(FILE_NAME);
        if (!file.exists()) {
            return null;
        }

        try (ObjectInputStream in =
                     new ObjectInputStream(new FileInputStream(FILE_NAME))) {

            return (List<Transaction>) in.readObject();

        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Failed to load transactions");
            e.printStackTrace();
            return null;
        }
    }
}
