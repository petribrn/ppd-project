import general.config as config
import socket
import os

text = """
    Hello world! This is a sample text.
"""
counters_number = os.environ.get('COUNTERS_NUMBER')

def init_orchestrator():
    # ['Hello', 'world!', ...]
    text_words = text.split(' ')
    text_words_count = len(text_words)
    words_per_counter = text_words_count / counters_number


    # STREAM constant for TCP connections
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_instance.bind((config.host, config.port))
    socket_instance.listen(1)

    connection, address = socket_instance.accept()

    while True:
        try:
            connection.send("Uma palavra aleatória...".encode())

            global_count = connection.recv(1024).decode()
        except Exception:
            break

    connection.close()
    socket_instance.close()

if __name__ == "__main__":
    init_orchestrator()