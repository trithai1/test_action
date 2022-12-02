import pandas as pd

from test_action import main


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
    msg = main.build_msg(val)
    assert msg == 'value: hi'


def test_get_empty_df():
    df = main.get_empty_df()
    pd.testing.assert_frame_equal(df, pd.DataFrame([]))
