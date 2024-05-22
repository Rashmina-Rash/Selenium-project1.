import logging
class Loggen:
    @staticmethod
    def loggen():
        logger=logging.getLogger() # create logger
        fhandler=logging.FileHandler(filename=".\\Logs\\automation.log",mode="a") #create file handler
        formatter=logging.Formatter("%(asctime)s: %(levelname)s %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO) # set logger level
        return logger