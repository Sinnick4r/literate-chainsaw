#!/usr/bin/env python3
import argparse
import json
import logging
from pathlib import Path

from .scanner import CodeScanner
from .patcher import PatchGenerator

def parse_args():
    parser = argparse.ArgumentParser(
        description='Security Chainsaw: scan code and suggest patches.'
    )
    parser.add_argument('path', type=str, help='Directory or file to scan')
    parser.add_argument('--report', type=str, default='findings.json',
                        help='Path to save the JSON report')
    parser.add_argument('--log-level', choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'],
                        default='INFO', help='Set the logging level')
    return parser.parse_args()

def setup_logging(level: str):
    logging.basicConfig(
        level=getattr(logging, level),
        format='%(asctime)s %(levelname)s %(message)s'
    )

def main() -> int:
    args = parse_args()
    setup_logging(args.log_level)

    code_path = Path(args.path)
    if not code_path.exists():
        logging.error(f"Path not found: {code_path}")
        return 1

    scanner = CodeScanner(code_path)
    findings = scanner.run_scan()
    logging.info(f"Found {len(findings)} issues")

    patcher  = PatchGenerator(findings)
    patches  = patcher.generate_patches()

    report = {'findings': findings, 'patches': patches}
    Path(args.report).write_text(json.dumps(report, indent=2))
    logging.info(f"Report saved to {args.report}")
    return 0

if __name__ == '__main__':
    exit(main())
