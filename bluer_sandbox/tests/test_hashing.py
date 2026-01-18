from bluer_options import string

from bluer_sandbox.radar.hashing import hash_of


def test_hashing_hash_of():
    input_string = string.random()

    hash_string = hash_of(input_string)

    hash_string_repeat = hash_of(input_string)

    assert hash_string == hash_string_repeat
