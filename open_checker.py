def check_file(file_name):
    try:
        with open(r'<File path>{}'.format(file_name), 'r+') as r:
            r.close()
        message = True
    except PermissionError:
        message = False
    return message
