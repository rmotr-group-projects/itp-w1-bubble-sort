.PHONY: test test-cov

TAG="\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PACKAGE=bubble_sort

run:
	@echo $(TAG)Executing main.py:$(END)
	@PYTHONPATH=. python $(PACKAGE)/main.py

test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=$(PACKAGE) tests

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=$(PACKAGE) $(shell which py.test) ./tests -q --tb=no >/dev/null; true
	@coverage report
