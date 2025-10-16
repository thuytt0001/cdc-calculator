
# cdc — Complex `dc` Calculator (ECSE 428)

This is a **TDD-first skeleton**. It intentionally contains:
- Only minimal scaffolding for the CLI and core modules.
- Two **failing tests** to start the TDD cycle.
- No implementation of `PUSH/POP` yet.

## Quickstart

```bash
python -m venv .venv
# Windows (PowerShell): . .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest

# Run tests 
pytest -q
or pytest -v #if you want to see message

# Run CLI
python -m cdc push 5 pop
```

# After each run / test
Screenshot result from CLI and upload to folder: cdc-calculator\docs\img_update