import os

import dotenv

dotenv.load_dotenv()
from hume import HumeBatchClient
from hume.models.config import FaceConfig
#todo: add key to secret

client = HumeBatchClient("kMENaHiAP3PCuEkdaUPbCx1JfUHvN2PRsN7Aaoe6GvPTkpzS")


def get_facial_analytics(file_path):
    filepaths = [
        file_path
    ]
    config = FaceConfig()
    # print(f" FILEPATHS: {file_path}")
    # print(f" workingdir: {os.getcwd()}")
    job = client.submit_job(None, [config], files=filepaths)

    print(job)
    # print("Running...")

    details = job.await_complete()
    data = job.get_predictions()
    return data