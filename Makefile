IMAGE=chimera

setup:
	python -m pip install --upgrade pip
	python -m pip install -e .[dev]

test:
	docker build -t $(IMAGE) .
	docker run --rm $(IMAGE)

spec-check:
	python scripts/spec_check.py
