.PHONY: test check

test:
	tests/run_tests

check:
	shellcheck ./sash
