import logging

'''
Modified default logger to log information in two saperate log-files 
'''
class Logger(logging.getLoggerClass()):

    def __init__(self, filename, name=''):
        if not name:
            name = filename

        super().__init__(name)
        
        self.propagate = True
        self.__fh_main = logging.FileHandler(f"logs/main.log")
        self.__fh_module = logging.FileHandler(f"logs/{filename}.log")
        self.__formatter = logging.Formatter("%(levelname)s (%(asctime)s) %(name)s.%(funcName)s (%(lineno)s) - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        self.__fh_main.setFormatter(self.__formatter)
        self.__fh_module.setFormatter(self.__formatter)

        self.addHandler(self.__fh_main)
        self.addHandler(self.__fh_module)