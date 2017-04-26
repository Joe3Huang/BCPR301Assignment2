import pickle
import os

class Serialization(object):

    """ docstring for Controller"""

    def __init__(self):
        self.__pickle = pickle

    def open(self, path, arg):
        try:
            if os.path.exists(path):
                return open(path, arg)
            else:
                raise IOError
        except IOError:
            return False
        except Exception as e:
            return False

    def dump(self, file, obejct):
        self.__pickle.dump(obejct, file)

    def load(self, file):
        try:
            ob = self.__pickle.load(file)
            return ob
        except EOFError:
            return False
        except Exception as e:
            return False
    def close(self, file):
        file.close()
