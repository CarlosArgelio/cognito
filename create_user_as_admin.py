import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


cognito = boto3.client('cognito-idp')


def create_user():

    logger.info("# Procesing created of user")

    response = cognito.admin_create_user(
        UserPoolId='',
        Username='user-10',
        UserAttributes=[
            {
                'Name': 'email',
                'Value': 'palaciosrcarlosa2@gmail.com',
            },
            {
                'Name': 'custom:gener',
                'Value': 'Masculino',
            },
        ],
        # ValidationData=[
        #     {
        #         'Name': 'custom:cedula',
        #         'Value': '30032692'
        #     },
        # ],
        TemporaryPassword='$ElGuanabanoNoEsBueno0800MALUCOS$',
        DesiredDeliveryMediums=[
            'EMAIL'
        ],
        ClientMetadata={
            'Name': 'custom:cedula',
            'Value': '30032692'
        }
    )

    return print(response)


if __name__ == '__main__':
    create_user()