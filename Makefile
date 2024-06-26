install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 brain_games
