import http.server
import socketserver

# 定义端口号
PORT = 8000

# 创建一个请求处理类，继承自 SimpleHTTPRequestHandler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    # 修改默认的根目录为当前目录
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

# 创建一个 HTTP 服务器
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("HTTP 服务器运行在端口", PORT)
    # 开始监听并处理请求
    httpd.serve_forever()
