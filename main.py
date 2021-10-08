# coding=utf-8
# main.py
import socket_operate.server
import handle.main_handle

def main():
    while 1:
        all_message = socket_operate.server.rev_msg()
        try:
            handle.main_handle.main_handle(all_message)
        except:
            continue

if (__name__ == "__main__"):
    main()

