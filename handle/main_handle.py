# coding=utf-8
# main_handle.py
# Handle information from main file

import handle.msg_handle

import handle.message_handle
import handle.notice_handle
import handle.request_handle


# Error of event type
def default():
    print("Event type error")
    return 0

# Handle variable event to corresponding program
def main_handle(msg):
    post_type = handle.msg_handle.get_post_type(msg)
    if post_type == 'message': # msg event
        handle.message_handle.message_handle(msg)
    elif post_type == 'notice': # notice event
        handle.notice_handle.notice_handle(msg)
    elif post_type == 'request': # post event
        handle.request_handle.request_handle(msg)
    else:
        default()
    return 0
