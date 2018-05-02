import argparse
from validator.fastq import Validator


def main(fastq_file):
    validator = Validator()
    result = validator.validate(fastq_file)
    if result.state == "VALID":
        print("File is valid")
    else:
        print("File is " + result.state + "\n")
        print(result.errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validates a FASTQ file.')
    parser.add_argument("file", type=str, help='FASTQ file to validate')
    args = parser.parse_args()
    main(args.file)
