EXEC=main.py
PYTHON_DEFAULT_EXEC=python3
INSTALL_PYTHON_PACKAGE_MSG="By default agG use python3 to be install"

all: run

run_scenario_1:
	echo 'scenario 1'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -q 1 -w 1 -w 2 -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_scenario_2:
	echo 'scenario 2'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -q 1 -w 1 -w 2

run_scenario_3:
	echo 'scenario 3'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_scenario_4:
	echo 'scenario 4'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -s False -t True -d "Test"

run_scenario_5:
	echo 'scenario 5'
	$(PYTHON_DEFAULT_EXEC) $(EXEC)


run_scenario_defaults:
	echo 'scenario defaults'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -s True -d "Hello"  -d "World"
