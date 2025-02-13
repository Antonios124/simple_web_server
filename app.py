# simple_web_server.py

import http.server
import socketserver
import os

PORT = 8000  # Порт, на котором будет работать сервер

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Указываем путь к файлу index.html
        if self.path == '/':
            self.path = 'index.html'

        try:
            # Открываем файл и отправляем его содержимое
            with open(os.getcwd() + self.path, 'rb') as file:
                content = file.read()

            # Отправляем ответ
            self.send_response(200)  # Код состояния 200 (OK)
            self.send_header("Content-type", "text/html; charset=utf-8")  # Тип контента
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            # Если файл не найден, отправляем код 404
            self.send_error(404, "File Not Found")

def run(server_class=http.server.HTTPServer, handler_class=MyHttpRequestHandler):
    # Создаем и запускаем сервер
    server_address = ("", PORT)  # Пустая строка означает, что сервер будет доступен по всем интерфейсам
    httpd = server_class(server_address, handler_class)
    print(f"Запуск веб-сервера на порту {PORT}...")
    try:
        httpd.serve_forever()  # Запускаем сервер
    except KeyboardInterrupt:
        print("\nОстановка сервера...")
        httpd.server_close()

if __name__ == "__main__":
    run()