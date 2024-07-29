import boto3
import logging
import tempfile

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ssm_param_name = '/sample/lambda-extract'
s3_bucket_name = 'dcx-sample-bucket'
s3_file_name = 'ssm_params.txt'


def lambda_handler(event, context):
    try:
        logger.info("Connecting to SSM")
        ssm_client = boto3.client('ssm')
        s3_client = boto3.client('s3')

        response = ssm_client.get_parameter(Name=ssm_param_name)
        logger.info(f"response: {response}")

        parameter_value = response['Parameter']['Value']

        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_file.write(parameter_value)
        temp_file.close()

        s3_client.upload_file(temp_file.name, s3_bucket_name, s3_file_name)

        return parameter_value
    except Exception as e:
        raise e

