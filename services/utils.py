from constants import OK_CODE, ERROR_CODE, NOT_REGISTERED_ERROR


def check_errors(data):
    if data:
        return OK_CODE
    else:
        return ERROR_CODE
