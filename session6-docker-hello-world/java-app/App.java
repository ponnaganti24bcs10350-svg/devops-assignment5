import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class App {
    public static void main(String[] args) throws IOException {
        int port = 8080;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", new HelloHandler());
        server.setExecutor(null);
        System.out.println("Java HTTP Server started on port " + port);
        server.start();
    }

    static class HelloHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = "<!DOCTYPE html>\n" +
                    "<html lang=\"en\">\n" +
                    "<head>\n" +
                    "  <meta charset=\"UTF-8\">\n" +
                    "  <title>Hello World - Java</title>\n" +
                    "  <style>\n" +
                    "    body {\n" +
                    "      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;\n" +
                    "      display: flex;\n" +
                    "      justify-content: center;\n" +
                    "      align-items: center;\n" +
                    "      height: 100vh;\n" +
                    "      margin: 0;\n" +
                    "      background: #0f172a;\n" +
                    "      color: #f8fafc;\n" +
                    "    }\n" +
                    "    .card {\n" +
                    "      background: #1e293b;\n" +
                    "      padding: 2.5rem 3.5rem;\n" +
                    "      border-radius: 12px;\n" +
                    "      box-shadow: 0 10px 25px rgba(0,0,0,0.3);\n" +
                    "      text-align: center;\n" +
                    "      border: 1px solid #334155;\n" +
                    "    }\n" +
                    "    h1 { color: #f97316; margin-bottom: 0.5rem; }\n" +
                    "    p { color: #94a3b8; font-size: 1.1rem; }\n" +
                    "  </style>\n" +
                    "</head>\n" +
                    "<body>\n" +
                    "  <div class=\"card\">\n" +
                    "    <h1>Hello World!</h1>\n" +
                    "    <p>Running on Java inside Docker</p>\n" +
                    "  </div>\n" +
                    "</body>\n" +
                    "</html>";
            exchange.getResponseHeaders().set("Content-Type", "text/html; charset=UTF-8");
            exchange.sendResponseHeaders(200, response.getBytes().length);
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
