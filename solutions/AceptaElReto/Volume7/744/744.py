#  https://aceptaelreto.com/problem/statement.php?id=744
# https://cs.stackexchange.com/questions/151112/greedy-algorithm-for-postive-interval-covering

import sys

while True:
    line = sys.stdin.readline()
    if not line:
        # No mre inputs
        break
    time = int(line.strip())

    mensajes = 0
    limite = -1

    while True:
        # Iterate this way to reduce memory usage
        n = ""
        while True:
            char = sys.stdin.read(1)
            if char == " " or char == "\n" or not char:
                break
            n += char

        if not n or n == "0":
            break
        n = int(n)

        if n > limite:
            mensajes += 1
            limite = n + time

    print(mensajes)


"""
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while ((line = reader.readLine()) != null && !line.isEmpty()) {
            int time = Integer.parseInt(line.trim());

            int mensajes = 0;
            int limite = -1;

            while (true) {
                StringBuilder nBuilder = new StringBuilder();
                int charInt;

                // Read one character at a time
                while ((charInt = reader.read()) != -1) {
                    char ch = (char) charInt;
                    if (ch == ' ' || ch == '\n') {
                        break;
                    }
                    nBuilder.append(ch);
                }

                String nStr = nBuilder.toString();
                if (nStr.isEmpty() || nStr.equals("0")) {
                    break;
                }

                int n = Integer.parseInt(nStr);

                if (n > limite) {
                    mensajes++;
                    limite = n + time;
                }
            }

            System.out.println(mensajes);
        }
    }
}
"""