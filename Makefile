.PHONY: all check test

all: check test

check:
	shellcheck ./sash

test:
	tests/run_tests
