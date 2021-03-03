import os
import src.dbt_test_coverage as dbt_test_coverage
import argparse
from pkg_resources import get_distribution
import logging

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recursive",
        help="If you want to search sub directories for yml-files (default: True)",
   )
    parser.add_argument(
        "--doc_thresh",
        help="Percentage to use a threshold to fail for total documentation coverage (default: 0)",
        default=0,
        type=float
    ) 
    parser.add_argument(
        "--test_thresh",
        help="Percentage to use a threshold to fail for total model test test-coverage (default: 0)",
        default=0,
        type=float
    ) 

    args = parser.parse_args()

    if args.recursive:
        recursive = args.recursive
    else:
        recursive = True

    if args.doc_thresh != 0 or args.test_thresh != 0:
        level = logging.INFO
    else:
        level = logging.DEBUG
    logging.basicConfig(format='%(message)s',level=level)

    logging.debug("")
    logging.debug("Running dbt-test-coverage " + get_distribution("dbt-test-coverage").version)
    logging.debug("")

    try:
        dbt_test_coverage.test_coverage(os.getcwd(), recursive=recursive, doc_thresh=args.doc_thresh, test_thresh=args.test_thresh)
    except KeyboardInterrupt:
        logging.warning("Interupted by user")

if __name__ == "__main__":
    main()
