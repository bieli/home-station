import hashlib


class Tokenizer:
    def __init__(self):
        pass

    def prepare_token(self, stationId, apiKey, timestamp):
        token = hashlib.sha256()
        token.update(str(stationId) + str(apiKey) + str(timestamp))
        token = token.hexdigest()
        # print "token: ", token
        return token

    def validate_token(self, data_message, token):
        if data_message.token == str(token):
            return True
        else:
            return False
