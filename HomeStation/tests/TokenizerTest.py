import unittest

from HomeStation.message import DataMessage_pb2
from HomeStation.tools.tokenizer import Tokenizer


class TokenizerTest(unittest.TestCase):
    def setUp(self):
        self.unit = Tokenizer()

    def test_should_prepare_token_with_no_empty_args(self):
        # given
        expected_token = "58d5a909d0dcd14171190854e9b72a7e55c490d9977ed4c73bc3ac8fdeb7530b"
        stationId = "example--station--id"
        apiKey = "example--api--key"
        timestamp = 1447280723

        # when
        token = self.unit.prepare_token(stationId, apiKey, timestamp)

        # then
        self.assertEqual(expected_token, token)

    def test_should_validate_token_for_good_token_in_data_message(self):
        # given
        validated_token = "58d5a909d0dcd14171190854e9b72a7e55c490d9977ed4c73bc3ac8fdeb7530b"

        data_message = DataMessage_pb2.DataMessage()
        data_message.token = validated_token

        # when
        result = self.unit.validate_token(data_message, validated_token)

        # then
        self.assertTrue(result)
