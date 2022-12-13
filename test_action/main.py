import pandas as pd


def get_empty_df():
    """
    Gets an empty dataframe
    :return: an empty dataframe
    """
    return pd.DataFrame([])


def build_msg(val):
    """
    Build a message
    :param val: a value
    :return: a message
    """
    return f'value: {val}'


def main():
    msg = build_msg('hi')
    print(msg)


if __name__ == '__main__':
    main()
