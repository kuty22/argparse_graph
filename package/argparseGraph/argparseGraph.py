#!/usr/bin/env python3

#import
import yaml

class argparseGraph:

    def __init__(self, configuration_file, argpars, verbose=False):
        self.__conf_path = configuration_file
        try:
            with open(configuration_file, 'r') as stream_file:
                self.__conf = yaml.load(stream_file)
        except OSError as err:
            print("OS error: {0}".format(err))
            exit(-1)
        if verbose:
            for key, value in self.__conf.items():
                print("strategie: {}".format(key))

        self.__args = argpars.__dict__
        self.__loop_options_available()

    def __loop_options_available(self):
        for title, senario in self.__conf.items():

            senario.update(dict({"status": None}))
            none_present = False
            options_list = []

            if type(senario["options"]) is str:
                # one line list
                if "," in senario["options"]:
                    senario["options"] = senario["options"].replace(" ", '').split(",")
                    self.__check_option_senario(senario)
                # all
                if senario["options"] == "all":
                    for k, item in self.__args.items():
                        if item is None:
                            none_present = True
                            break
                    if none_present:
                        senario["status"] =  "Fail"
            else:
                # list format
                self.__check_option_senario(senario)

    def __check_option_senario(self, senario):
        for needed_args in senario["options"]:
            if needed_args in self.__args:
                senario["status"] = "Fail" if self.__args[needed_args] is None else None
            else:
                print("APG error: Bad param name in {}".format(self.__conf_path))
                exit(-1)
        for k, item in self.__args.items():
            if k not in senario["options"] and item != None:
                senario["status"] = "Fail"

    def get_one(self):
        for senario, obj in self.__conf.items():
            if obj["status"] == None:
                return senario
        return dict({"Error": "Not senario found", "status": -1})

    def get_dict(self):
        for senario, obj in self.__conf.items():
            if obj["status"] == None:
                return obj
        return dict({"Error": "Not senario found", "status": -1})

    def get_all(self):
        return self.__conf
