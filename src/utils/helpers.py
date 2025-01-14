def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description='Popis vaší aplikace.')
    parser.add_argument('--option', type=str, help='Popis volby.')
    return parser.parse_args()