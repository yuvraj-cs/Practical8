# Python Calculator (Travis CI demo)

[![Build Status](https://app.travis-ci.com/USER/REPO.svg?branch=main)](https://app.travis-ci.com/USER/REPO)

A minimal Python project with a test suite, ready to push to GitHub and hook up to Travis CI.

## Run locally

```bash
pip install -r requirements.txt
python calculator.py
pytest -q
```

## Files

- `calculator.py` — the module (add, subtract, multiply, divide, is_even)
- `test_calculator.py` — pytest test suite
- `.travis.yml` — Travis CI config (runs `pytest -q` on Python 3.10 and 3.11)
