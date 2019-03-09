EXEC=./main.py

all: run

run:
ifndef senarios
	$(MAKE) run_senario_1
else ifeq ($(senarios), 2)
	$(MAKE) run_senario_2
else ifeq ($(senarios), 3)
	$(MAKE) run_senario_3
else
	$(MAKE) run_senario_defaults
endif

run_senario_1:
	echo 'senarios 1'
	$(EXEC) -q 1 -w 1 -w 2 -e toto -t ok -a ok -s True -d "Hello"  -d "World"

run_senario_2:
	echo 'senarios 2'
	$(EXEC) -q 1 -w 1 -w 2

run_senario_3:
	echo 'senarios 3'
	$(EXEC) -e toto -t ok

run_senario_defaults:
	echo 'senarios defaults'
	$(EXEC) -s True -d "Hello"  -d "World"
