"""HEIC to JPG — Convert iPhone HEIC photos to JPEG and keep a copy of the original."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='heic_to_jpg',
        description='Convert iPhone HEIC photos to JPEG and keep a copy of the original.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('HEIC to JPG')
    print('HEIC that Windows apps can actually open.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
