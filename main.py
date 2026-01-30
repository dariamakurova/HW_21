
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost" # Адрес для доступа по сети
serverPort = 8000 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_contacts(self):
        try:
            with open("contacts.html", "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"""
            <html>
                <head><title>Ошибка</title></head>
                <body>
                    <h1>Не удалось загрузить страницу с контактами</h1>
                    <p>{e}</p>
                </body>
            </html>
            """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__get_contacts()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8")) # Тело ответа

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")