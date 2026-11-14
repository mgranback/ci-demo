# ci-demo

Ett litet Python-projekt som visar tester och lint i GitHub Actions.

`find_brute_force` letar efter IP-adresser som har minst `tries_threshold` försök inom `time_threshold` sekunder. Standardvärdena är 3 försök och 60 sekunder. `count_errors` räknar loggrader som innehåller texten `ERROR`.

## Krav

- Python 3.14 eller nyare
- [uv](https://docs.astral.sh/uv/)

## Kom igång

```bash
uv sync
```

`pyproject.toml` och `uv.lock` ska följa med i git. Toml-filen beskriver projektet och vilka verktyg som behövs. Låsfilen låser versionerna, och CI kör `uv sync --locked` mot just den.

## Köra brute force-demo

```bash
uv run python brute_force.py
```

Skriptet läser `events.csv` och skriver ut händelserna och de IP-adresser som träffar trösklarna. Med exempeldatan och standardtrösklarna blir resultatet `1.1.1.1`.

`events.csv` har kolumnerna `time` och `ip`. Tiden anges som `HH:MM:SS`.

## Tester och lint

```bash
uv run pytest
uv run ruff check .
```

## CI

Workflowen i `.github/workflows/ci.yml` körs vid push och pull request. Den gör tre saker:

1. `uv sync --locked`
2. `uv run ruff check .`
3. `uv run pytest`
