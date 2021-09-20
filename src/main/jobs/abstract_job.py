import logging
from abc import abstractmethod, ABCMeta


class AbstractJob(metaclass=ABCMeta):
    '''AbstractJob provides common functionality for jobs that executes various set of tasks on spark.'''

    def __init__(self, sc, spark, gc, config):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.sc = sc
        self.spark = spark
        self.gc = gc
        self.config = config


    @abstractmethod
    def try_execute(self, sc, spark, gc, config):
        pass


    def execute(self):
        self.logger.info("Executing job %s", (self.__class__.__name__,))
        try:
            self.try_execute( self.sc, self.spark, self.gc, self.config)
            self.logger.error("Executing job %s completed", self.__class__.__name__)
        except Exception as exception:
            # unexpected error, should retry
            self.logger.error("Error while executing job %s", self.__class__.__name__, exc_info=exception)


