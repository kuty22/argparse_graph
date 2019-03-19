# agrparseGraph

## Summary

- [Description](#description)
- [Install](#install)
- [Use it](#user-it)
- [Tests](#test)
- [Documentation](#documentation)

## Description
Add logic in argpars object with argparsGraph.  
This package help you to avoid the if/else forests after `argparse`

## Install

Install package:
```shell
make install
```

Uninstall package:
```shell
make uninstall
```

## Use it

> The parameter define with argparse must be named (dest="argsName")if not it will  
> be impossible to find some link between the variable name and the name in the yaml file.

example of argparse object:

**python script**
```python
from argparseGraph.argparseGraph import argparseGraph as agG

def parsarg():
    parser = argparse.ArgumentParser(description="random options for senarios")
    parser.add_argument("-q", dest="argv1", help="test", type=int)
    parser.add_argument("-w", dest="argv2", help="test", type=int, action='append')
    parser.add_argument("-e", dest="argv3", help="test", type=str, default="test3")
    parser.add_argument("-t", dest="argv4", help="test", type=str, default=False)
    parser.add_argument("-a", dest="argv5", help="test", type=str)
    parser.add_argument("-s", dest="argv6", help="test", type=bool)
    parser.add_argument("-d", dest="argv7", help="test", type=str, action='append')
    args = parser.parse_args()

    return args

res = parsarg()
agg = agg("senarios.yml", res_args, verbose=False)
```

**senario.yml**
```yaml
# if all arguments are note None
# cmd: ./main.py -q 1 -w 1 -w 2 -e t -t o -a o -s t -d "Hello"  -d "World"
senario_1:
  options: "all"
# if argv3, argv4 are not None and other are None
# format list [v1, v2]
# cmd: ./main.py -e toto -t ok
senario_2:
  options: [argv3, argv4]
# if argv3, argv4, argv5, argv6, argv7 are not None and other are None
# format list     
#    - argv3
#    - argv4
#    - argv5
#    - argv6
#    - argv7
# cmd: ./main.py -e toto -t ok -a ok -s True -d "Hello"  -d "World"
senario_3:
  options:
    - argv3
    - argv4
    - argv5
    - argv6
    - argv7
# if argv3, argv4, argv6, argv7 are not None and other are None
# format str argv3, argv4, argv6, argv7
# cmd: ./main.py -s False -t True -d "Test"
senario_4:
  options: argv3, argv4, argv6, argv7
```

With the `argparseGraph` object you can get 3 differents result format,
with these method:  
```python
# Return the name of the strategie in the yaml file.
agg.get_one()
# example:
# 'senario_test'

# Return a dict
agg.get_dict()
# { 'senario': 'senario_test', 'options': ['argv3', 'argv4', 'argv5', 'argv6', 'argv7'], 'status': None}

agg.get_all()
# {
#  'senario_1': {'options': 'all', 'name': 'senario_1', 'status': 'Fail'},
#  'senario_2': {'options': ['argv3', 'argv4'], 'name': 'senario_2', 'status': 'Fail'},
#  'senario_3': {'options': ['argv3', 'argv4'], 'name': 'senario_3', 'status': 'Fail'},
#  'senario_4': {'options': ['argv3', 'argv4', 'argv6', 'argv7'], 'name': 'senario_4', 'status': 'Fail'},
#  'senario_test': {'options': ['argv3', 'argv4', 'argv5', 'argv6', 'argv7'], 'name': 'senario_test', 'status': None},
#  'senario_5': {'options': '', 'name': 'senario_5', 'status': 'Fail'}
# }
```

## Tests

Tow type of tests are available, the first one is run on the sources in the project directory,
the second one is run on the package install on your system.

run test on the package not install:
```
make test
```

run test on the package install:
```
make test_install
```


## Documentation

_Makefile commands available_:

|          **commands name**           | **description**                       |
|:------------------------------------:|:------------------------------------- |
|            `make install`            | install `argparseGraph`               |
|                                      |                                       |
|           `make uninstall`           | uninstall `argparseGraph`             |
|                                      |                                       |
|             `make test`              | run test on sources not install       |
|                                      |                                       |
|         `make test_install`          | run test on the package install       |
|                                      |                                       |
|              `make run`              | run example                           |
| `make run senarios=[1 , 2, 3, 4, 5]` | run example with a specifique senario |
|                                      |                                       |

you can specify makefile options:

|   **commands name**   | **default** | **description**                             |
|:---------------------:|:----------- | ------------------------------------------- |
|  `EXEC_DEFAULT_TEST`  | pytest      | Tools for run test                          |
|                       |             |                                             |
| `PYTHON_DEFAULT_EXEC` | python3     | Python use to run  test and install package |
|                       |             |                                             |


__Reference__:

- [Python3.5 Documentation](https://www.python.org/downloads/release/python-350/)
- [argparse (python3)](https://docs.python.org/3/library/argparse.html)
- [pip](https://pip.pypa.io/en/stable/)
- [setuptools](https://setuptools.readthedocs.io/en/latest/)
