from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("Testando", 3) == "seT_odnat"
    assert encrypt_message("Testando", 4) == "odna_tseT"
    assert encrypt_message("Testando", 9) == "odnatseT"

    with pytest.raises(TypeError):
        encrypt_message(9, 9)

    with pytest.raises(TypeError):
        encrypt_message(9, "9")
