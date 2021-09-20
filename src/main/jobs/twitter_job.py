from src.main.jobs.abstract_job import AbstractJob


class TwitterJob(AbstractJob):
    def try_execute(self, sc, spark, gc, config):
        self.logger.info("JOB logic here")

def execute( sc, spark, gc, config):
    job = TwitterJob( sc, spark, gc, config)
    job.execute()
