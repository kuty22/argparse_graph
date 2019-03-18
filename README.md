# agrparseGraph

## Summary

- [Description](#description)
- [Use it](#user-it)
- [Documentation](#documentation)

## Description
Add senarios logique after using argparse.

# Use it

> For the moment the parameter define with argparse must be named (dest="argsName")if not it will  
> be impossible to find some link between the variable name and the name in the yaml file.

methods to get results:  
```python
agg.get_one()
agg.get_dict()
agg.get_all()
```

_requirements_:
- python=3.5
- pyyaml

## Documentation

_Makefile commands available_:

| **commands name** | **description**                 |
|:-----------------:|:------------------------------- |
|  `make install`   | install `argparseGraph`         |
|                   |                                 |
| `make uninstall`  | uninstall `argparseGraph`       |
|                   |                                 |
|    `make test`    | run test on sources not install |
|                   |                                 |
|  `make test_int`  | run test on the package install |
|                   |                                 |
|  `make example`   | run example                     |
|                   |                                 |


__Reference__:

- [Python3.5 Documentation](https://www.python.org/downloads/release/python-350/)
