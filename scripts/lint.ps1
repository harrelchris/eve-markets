.venv\Scripts\activate

black app --line-length 120 --extend-exclude='^(.*/)?(migrations|fixtures)/'

flake8 --max-line-length 120 --extend-exclude app/*/migrations/ app

isort app --profile black --line-length 120 --src-path app
