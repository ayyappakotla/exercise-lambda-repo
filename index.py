import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ssm_param_name = '/sample/lambda-extract'


def lambda_handler(event, context):
    try:
        ssm = boto3.client('ssm')
        response = ssm.get_parameter(Name=ssm_param_name)
        logger.info(f"response: {response}")

        parameter_value = response['Parameter']['Value']

        response_data = {
            'String': parameter_value
        }

        return response_data
    except Exception as e:
        raise e

