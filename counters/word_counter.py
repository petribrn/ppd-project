import general.config as config
import socket

def init_counter_instance():
    # STREAM constant for TCP connections
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_instance.connect((config.host, config.port))

    while True:
        try:
            # Cada processo recebe um array de palavras do processor? Ou uma de cada vez como string?
            word_received = socket_instance.recv(1024).decode()

            count = 0
            finished = True

            if (finished):
                socket_instance.send(count.encode())
                break
        except Exception:
            break

    socket_instance.close()

if __name__ == "__main__":
    init_counter_instance()