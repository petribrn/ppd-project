import socket
from colorama import Fore, Back, Style

host_name = 'text-processor'
port = 1201

def count_words(content: str) -> int:
    return len(content.split(' '))


def init_counter_instance():
    # STREAM constant for TCP connections
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.connect((host_name, port))

    # Receives a content part of the text iterable
    content_received: str = socket_instance.recv(1048576).decode()
    print('Received text part.')

    # Counts number of words
    count = count_words(content_received)
    print(f'{Back.YELLOW}{Fore.BLACK}Count: {Back.WHITE}{count}{Style.RESET_ALL}')

    # Sends back the count to the main container (fragmenter) and close socket
    socket_instance.send(str(count).encode())
    socket_instance.close()


if __name__ == "__main__":
    init_counter_instance()