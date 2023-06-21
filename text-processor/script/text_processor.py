import socket
import os
from threading import Thread, Lock
from colorama import Fore, Back, Style

# Global variables
global_count = 0
counters_number = int(os.environ.get('COUNTER_NUMBER'))
host_name = ''
port = 1201
address_pattern_counters = "ppd-project_word-counter_{}"
lock = Lock()

def handle_new_client(client_socket: socket.socket, addr, data: str):
    while True:
        global global_count
        try:
            # Send file content fragment for one of child containers
            client_socket.send(data.encode())
            partial_count = client_socket.recv(1048576).decode()
            print(f'Partial count from {addr}: {partial_count}')

            # Lock/unlock mutex for global counter value change
            lock.acquire()
            global_count += int(partial_count)
            lock.release()
            break
        except:
            break
    client_socket.close()

def check_empty_space(content, pos):
    try:
        if pos <= 1:
            return pos
        while content[pos] != ' ':
            pos += 1

        return(pos)
    except IndexError:
        return pos

def init_orchestrator():
    # Reads file content
    content = get_file_content('./large_text.txt')

    # Defines file content fragments for each child container
    increment_value = len(content) // counters_number
    parts = [content[check_empty_space(content, i):check_empty_space(content, i+increment_value)].strip() for i in range(0, len(content), increment_value)]
    parts = list(filter(lambda x: x != '', parts))

    if len(parts) > counters_number:
        parts[-2] += f' {parts[-1]}'
        parts = parts[:-1]

    print(f'Text divided in {len(parts)} parts, sending to counters...')
    global global_count

    # STREAM constant for TCP connections
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set up TCP socket connection environment
    socket_instance.bind((host_name, port))
    socket_instance.listen(counters_number)

    i = 0
    threads = []

    while True:
        try:
            # Has to be made in different threads so the connection remains when another is started
            connection, addr = socket_instance.accept()
            threads.append(Thread(target=handle_new_client, args=(connection, addr, parts[i])))
            threads[i].start()

            i += 1
            if i >= len(parts):
                break 
        except Exception as e:
            break
    
    # Sync all threads
    for thread in threads:
        thread.join()

    print(f'{Back.MAGENTA}{Fore.WHITE}Total final count received: {Back.WHITE}{Fore.MAGENTA}{global_count}{Style.RESET_ALL}')

    # Close socket
    socket_instance.close()

def get_file_content(file_name: str) -> str:
    # Read file and close it when 'with' statement finishes
    content = ''
    with open(file_name, 'r') as file:
        lines = file.readlines()
        content = '\r'.join(lines)
        clean_content = content.replace('\n','').replace('.', '').replace(',', '').replace('!', '').replace('?', '')

    return clean_content

if __name__ == "__main__":
    init_orchestrator()
    