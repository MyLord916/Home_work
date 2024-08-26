import string
import random
import argparse


def pass_gen(length: int, use_punctuation: bool, use_digit: bool, use_uppercase: bool) -> str:
    simbols = string.ascii_lowercase
    if use_punctuation:
        simbols += string.punctuation
    if use_digit:
        simbols += string.digits
    if use_uppercase:
        simbols += string.ascii_uppercase
    res = random.choices(simbols, k=length)
    return ''.join(res)


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='Length of the generated password', type=int, default=12)
parser.add_argument(
    '-p', '--use_punctuation', help='Indicates the need to use punctuation simbols', action='store_true', default=False
)
parser.add_argument(
    '-d', '--use_digit', help='Indicates the need to use digit simbols', action='store_true', default=False
)
parser.add_argument(
    '-u', '--use_uppercase', help='Indicates the need to use uppercase simbols', action='store_true', default=False
)
args = parser.parse_args()

pass_gen = pass_gen(args.length, args.use_punctuation, args.use_digit, args.use_uppercase)

print(f'\n{pass_gen}\n')