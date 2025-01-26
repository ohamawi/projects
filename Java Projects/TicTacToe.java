import java.util.Scanner;
import java.util.Random;

public class TicTacToe {

    public static void main(String[] args) {
        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }

        boolean playerTurn = true;
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        while (true) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(board[i][j] + " ");
                }
                System.out.println();
            }

            if (playerTurn) {
                int row, col;
                while (true) {
                    System.out.println("Enter your move (row and column): ");
                    row = scanner.nextInt();
                    col = scanner.nextInt();
                    if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == '-') {
                        board[row][col] = 'X';
                        break;
                    } else {
                        System.out.println("This move is not valid. Try again.");
                    }
                }
            } else {
                int row, col;
                while (true) {
                    row = random.nextInt(3);
                    col = random.nextInt(3);
                    if (board[row][col] == '-') {
                        board[row][col] = 'O';
                        System.out.println("AI moves to " + row + " " + col);
                        break;
                    }
                }
            }

            boolean win = false;
            for (int i = 0; i < 3; i++) {
                if ((board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != '-') ||
                    (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != '-')) {
                    win = true;
                }
            }
            if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != '-') ||
                (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != '-')) {
                win = true;
            }

            if (win) {
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        System.out.print(board[i][j] + " ");
                    }
                    System.out.println();
                }
                System.out.println((playerTurn ? "Player" : "AI") + " wins!");
                break;
            }

            boolean draw = true;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == '-') {
                        draw = false;
                    }
                }
            }

            if (draw) {
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        System.out.print(board[i][j] + " ");
                    }
                    System.out.println();
                }
                System.out.println("It's a draw!");
                break;
            }

            playerTurn = !playerTurn;
        }
    }
}
