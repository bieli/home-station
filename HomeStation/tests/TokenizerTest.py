import unittest

from HomeStation.tools.tokenizer import Tokenizer


class TokenizerTest(unittest.TestCase):

  def test_should_prepare_token_with_no_empty_args(self):
      # given
      expected_token = "58d5a909d0dcd14171190854e9b72a7e55c490d9977ed4c73bc3ac8fdeb7530b"
      stationId = "example--station--id"
      apiKey = "example--api--key"
      timestamp = 1447280723
      tok = Tokenizer()

      # when
      token = tok.prepare_token(stationId, apiKey, timestamp)

      # then
      self.assertEqual(expected_token, token)

if __name__ == '__main__':
    unittest.main()
