class BittrexKey:
  _key = None
  _secret = None

  def __init__(self):
    self._key = ''
    self._secret = ''

  def get_key(self):
    return self._key

  def get_secret(self):
    return self._secret
