from bluer_sandbox.arvancloud.seed import generate_seed


def test_test_arvancloud_seed():
    success, seed = generate_seed()
    assert success
    assert seed
