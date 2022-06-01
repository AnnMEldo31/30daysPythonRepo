import argparse

print("Hello, PyCharm!")

parser = argparse.ArgumentParser()
parser.add_argument("base", type=float, help="A number to raise to the specified power.")
parser.add_argument(
    "-e", "--exponent",
    type=float,
    default=2,
    help="A power to raise the provided base to."
)

args = parser.parse_args()

print(args.base)
print(args.exponent)
print(args.base ** args.exponent)