#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pydantic>=2.11",
#     "pyyaml>=6.0",
# ]
# ///
"""Validate an AIP skill folder. Thin wrapper over `aip-spec validate`.

Works from a plain git clone of this repo with no install step: it adds the sibling
`src/` to the path so `aip_spec` is importable, and PEP 723 pulls the two dependencies.
If the `aip-spec` package is installed, that is used instead.

Output contract:
- Exit 0 on success (no errors; warnings allowed); 1 on any error.
- stdout: single-line human summary.
- stderr: JSON Lines, one record per issue: `path`, `kind`, `message`,
  optional `location`, and `severity` ("error" or "warning"; absent = "error").
"""

import sys
from pathlib import Path

_src = Path(__file__).resolve().parent.parent / "src"
if (_src / "aip_spec").is_dir():
    sys.path.insert(0, str(_src))

from aip_spec.cli import validate_command  # noqa: E402

if __name__ == "__main__":
    sys.exit(validate_command(sys.argv[1:]))
