import urllib.request
import socket
def get_gongwangip():
    a = urllib.request.urlopen("http://ifconfig.me/ip")
    return a.read().decode().strip()
my_ip = get_gongwangip()
print(my_ip)
def bang_ding():
    server = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    try:
        server.bind((my_ip,8080))
        server.listen()
        print("yes")
        print("服务器启动成功🤓")
        print(f"请访问http//[{my_ip}]:8080")
        while True:
            conn,addr = server.accept()
            print(f"收到{addr[0]}的连接") 
            data = conn.recv(1024)
            if data:
                print(f"收到消息{data[:50]}")
                response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>棍母!</h1>"
            conn.send(response.encode())
            conn.close()
            print("关闭")
    except Exception as e:
        print(f"错误{e}")
        return None
    
bang_ding()        
   