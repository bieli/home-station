import hashlib


class Tokenizer:
    def __init__(self):
        pass

    def prepare_token(self, stationId, apiKey, timestamp, verbose=False):
        stationId = str(stationId).encode('utf-8')
        apiKey = str(apiKey).encode('utf-8')
        timestamp = str(timestamp).encode('utf-8')
        token = hashlib.sha256(stationId + apiKey + timestamp).hexdigest()

        if verbose:
            print("Tokenizer -> prepare_token stationId: '%s'" % stationId)
            print("Tokenizer -> prepare_token apiKey: '%s'" % apiKey)
            print("Tokenizer -> prepare_token timestamp: '%s'" % timestamp)
            print("Tokenizer -> prepare_token =========== result: '%s'" % token)

        return token

    def validate_token(self, data_message, token):
        if str(data_message.token) == str(token):
            return True
        else:
            return False
