EXEC=./main.py
INSTALL_PYTHON_PACKAGE_MSG="By default agG use python3 to be install"

all: run

run_senario_1:
	echo 'senarios 1'
	$(EXEC) -q 1 -w 1 -w 2 -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_senario_2:
	echo 'senarios 2'
	$(EXEC) -q 1 -w 1 -w 2

run_senario_3:
	echo 'senarios 3'
	$(EXEC) -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_senario_4:
	echo 'senarios 4'
	$(EXEC) -s False -t True -d "Test"

run_senario_5:
	echo 'senarios 5'
	$(EXEC)


run_senario_defaults:
	echo 'senarios defaults'
	$(EXEC) -s True -d "Hello"  -d "World"
