EXEC=./main.py
EXEC_DEFAULT_TEST=pytest
INSTALL_PYTHON_PACKAGE_MSG="By default agG use python3 to be install"
PYTHON_DEFAULT_EXEC=python3

all: run

run:
ifndef senarios
	$(MAKE) -C examples run_senario_1
else ifeq ($(senarios), 2)
	$(MAKE) -C examples run_senario_2
else ifeq ($(senarios), 3)
	$(MAKE) -C examples run_senario_3
else ifeq ($(senarios), 4)
	$(MAKE) -C examples run_senario_4
else ifeq ($(senarios), 5)
	$(MAKE) -C examples run_senario_5
else
	$(MAKE) -C examples run_senario_defaults
endif

test_install:
ifndef exec_test
	$(PYTHON_DEFAULT_EXEC) -m $(EXEC_DEFAULT_TEST) -q tests -s
else
	$(PYTHON_DEFAULT_EXEC) -m  $(exec_test) -q tests -s
endif

test:
ifndef exec_test
	$(PYTHON_DEFAULT_EXEC) -m $(EXEC_DEFAULT_TEST) -q package/test -s
else
	$(PYTHON_DEFAULT_EXEC) -m $(exec_test) -q package/test -s
endif

install:
	echo "install argparseGraph package"
	$(MAKE) -C package install

uninstall:
	echo "uninstall argparseGraph"
	$(MAKE) -C package uninstall
