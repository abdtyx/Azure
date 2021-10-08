# coding=utf-8
# msg_handle.py
# The main content of this file is method for getting key data from the dictionary of main file.
# Get type of post: message, notice, request
def get_post_type(msg):
    return msg['post_type']

# Get type of info Group/Private
def get_message_type(msg):
    return msg['message_type']

# Get Group_id/User_id
def get_number(msg):
    if get_message_type(msg) == 'group':
        return msg['group_id']
    elif get_message_type(msg) == 'private':
        return msg['user_id']
    else:
        print('Cannot find this group/user')
        exit()

# Get poster's user_id
def get_user_id(msg):
    return msg['user_id']

# Get raw message
def get_raw_message(msg):
    return msg['raw_message']

