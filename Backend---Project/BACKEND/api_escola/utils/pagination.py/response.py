def success_response(data, message="Sucesso"):
    return {
        "message": message,
        "data": data
    }

def error_response(message, status_code):
    return {
        "error": message,
        "statusCode": status_code
    }