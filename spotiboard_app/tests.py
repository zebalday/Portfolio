from django.test import TestCase
from util import get_user_tokens

# Create your tests here.

token = "duvgp958f7gnboy26h4buw9h6nymctc0"
token2 = "9y9lsl7wvkiorj1b9z0iivghluhsr1yt"

print(get_user_tokens(token))
print(get_user_tokens(token2))



