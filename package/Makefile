EXEC=setup.py
INSTALL_PYTHON_PACKAGE_MSG="By default agG use python3 to be install"
PYTHON_DEFAULT_EXEC=python3

install:
ifndef python_exec
	echo $(INSTALL_PYTHON_PACKAGE_MSG)
	$(PYTHON_DEFAULT_EXEC) $(EXEC) install --record uninstall.txt
else
	$(python_exec) $(EXEC) install --record uninstall.txt
endif

uninstall:
	cat uninstall.txt | xargs sudo rm -rf
