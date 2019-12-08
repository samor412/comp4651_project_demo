import json
def errorMsg(errType):
    return json.dumps({
        'response': 'failed',
        'errType': errType,
    })
