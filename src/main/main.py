import importlib
import os
import sys

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)


args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
gc = GlueContext(sc)
spark = gc.spark_session
job = Job(gc)
job.init(args['JOB_NAME'], args)

logger.info(f'{args["JOB_NAME"]} Starting ............  ')
job_module = importlib.import_module(f'src.main.jobs.{args["JOB_NAME"]}')
job_module.execute(sc, spark, gc, {})

#TwitterJob.start(glueContext, args)
job.commit()


