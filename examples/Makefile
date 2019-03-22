EXEC=main.py
PYTHON_DEFAULT_EXEC=python3
INSTALL_PYTHON_PACKAGE_MSG="By default agG use python3 to be install"

all: run

run_senario_1:
	echo 'senarios 1'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -q 1 -w 1 -w 2 -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_senario_2:
	echo 'senarios 2'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -q 1 -w 1 -w 2

run_senario_3:
	echo 'senarios 3'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_senario_4:
	echo 'senarios 4'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -s False -t True -d "Test"

run_senario_5:
	echo 'senarios 5'
	$(PYTHON_DEFAULT_EXEC) $(EXEC)


run_senario_defaults:
	echo 'senarios defaults'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -s True -d "Hello"  -d "World"
