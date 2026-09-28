#!/usr/bin/env python
"""Build the lambeq API reference `.qmd` files with quartodoc.

Thin wrapper: the renderer patches and build entry point live in the shared
``build_api_common.py`` shipped by ``@quantinuum/docs-build``, whose
``docs-build`` CLI puts it on ``PYTHONPATH`` before running this script.

Usage: run ``docs-build`` from the repo root, or by hand from this directory::

    PYTHONPATH=<documentation-ui>/docs-build/quartodoc uv run python build_api.py
"""
from __future__ import annotations

import os

try:
    from build_api_common import build
except ImportError as exc:
    raise SystemExit(
        "build_api_common not found: run via `docs-build`, or put "
        "<documentation-ui>/docs-build/quartodoc on PYTHONPATH."
    ) from exc


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    build()
