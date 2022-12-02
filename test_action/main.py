import pandas as pd


def get_empty_df():
    return pd.DataFrame([])


def build_msg(val):
    return f'value: {val}'


def main():
    msg = build_msg('hi')
    print(msg)


if __name__ == '__main__':
    main()
