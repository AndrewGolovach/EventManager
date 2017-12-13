import importlib
from inspect import getmembers, isfunction
from os.path import isdir, abspath, join
from os import listdir

import imp

from eventmanager.action import Action
from eventmanager.action_decorator import ActionDecorator

import warnings
warnings.filterwarnings("ignore")


class Collector(object):

    def __init__(self, package_name):
        self.package_name = package_name

    def collect(self):
        if isdir(self.package_name):
            return self._collect_from_package(self.package_name)
        else:
            mod = importlib.import_module(self.package_name)
            return self._collect_from_module(mod)

    def _collect_from_package(self, package_name):
        file_tree = listdir(package_name)
        actions = []

        for file_name in file_tree:
            if isdir(file_name):
                actions += self._collect_from_package(file_name)
            elif ".py" == file_name[-3:]:
                path = join(abspath(package_name), file_name)
                mod = imp.load_source(path, path)
                actions += self._collect_from_module(mod)
        return actions

    def _collect_from_module(self, mod):
        functions = [f for (name, f) in getmembers(mod, isfunction)]
        decorated_functions = filter(self._is_action, functions)

        actions = []
        for action in decorated_functions:
            decorator_info = action.func_dict[ActionDecorator.action_key].get_decorator_info()
            actions.append(Action(action, *decorator_info))
        return actions

    def _is_action(self, module_member):
        return ActionDecorator.action_key in module_member.func_dict
