from test_action.main import build_msg


# --------------------------------------------------------
# Fixtures
# --------------------------------------------------------

# --------------------------------------------------------
# Simple Valid Tests: START
# --------------------------------------------------------

def test_canary():
    assert True


def test_build_msg():
    val = 'hi'
    msg = build_msg(val)
    assert msg == 'value: hi'


def test_false():
    assert False
