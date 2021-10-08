# coding=utf-8
# client.py
# From aspect of port 5700, we are client sending message.
import socket
import urllib.parse


# Ask bot to sent message by sending a http post
# In parameter resp_dict, we must asssign type, responding and user_id(group_id)
def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))
    msg_type = resp_dict['msg_type']    # respond type(group/private)
    number = resp_dict['number']    # Respond account(group_id/user_id)
    msg = resp_dict['msg']      # message to be respond

    # Url encode
    msg = urllib.parse.quote(msg)

    if msg_type == 'group':
        payload = "GET /sent_group_msg?group_id=" + str(number) + "&message=" + msg + "HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(number) + "&message=" + msg + "HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("Sending..." + payload)
    client.send(payload.encode("utf-8"))
    client.close()


    return 0
