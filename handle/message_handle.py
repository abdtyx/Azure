# coding=utf-8
# message_handle.py
# Handle message event
from socket_operate.client import send_msg
from handle.msg_handle import get_message_type

#--------------------------------------------------------
# Private message general detection
def private_msg_general_detection(message):
    reply=''
    return reply

# Private message database detection
def private_msg_db_detection(message):
    reply=''
    return reply

# Private message error catch
def private_msg_error(message):
    reply=''
    return reply

# Handle private message
def private_msg_handle(message):
    msg_dict={
            "msg_type" : "private",
            "number" : get_number(message),
            "msg" : "I cannot hear that." # The string here is non-sense
    }
    general_detect = private_msg_general_detection(message)
    db_detect = private_msg_db_detection(message)
    if general_detect != '':
        msg_dict["msg"] = general_detect
    elif db_detect != '':
        msg_dict["msg"] = db_detect
    else:
        msg_dict["msg"] = private_msg_error(message)
    send_msg(msg_dict)
    return

#--------------------------------------------------------
# Group message general deetection
def group_msg_general_detection(message):
    reply=''
    return reply

# Group message database detection
def group_msg_db_detection(message):
    reply = ''
    return reply

# Group message error catch
def group_msg_error(message):
    reply = ''
    return reply

# Handle group message
def group_msg_handle(msg):
    msg_dict = {
            "msg_type" : "group",
            "number" : get_number(message),
            "msg" : "Non-sense"
    }
    # detection
    general_detect = group_msg_general_detection(message)
    db_detect = group_msg_db_detection(message)

    if general_detect != '':
        msg_dict["msg"] = general_detect
    elif db_detect != '':
        msg_dict["msg"] = db_detect
    else:
        msg_dict["msg"] = group_msg_error(message)
    send_msg(msg_dict)
    return 

#--------------------------------------------------------

def message_handle(msg):
    if get_message_type(msg) == 'private':
        private_msg_handle(msg)
    elif get_message_type(msg) == 'group':
        group_msg_handle(msg)
    return 0
