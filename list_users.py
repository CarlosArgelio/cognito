import boto3

cognito = boto3.client('cognito-idp')


def list_users():

    response = cognito.list_users(
        UserPoolId='',
        AttributesToGet=[
            'email' 
        ],
        Limit=20,
        # PaginationToken='string',
        # Filter='string'
    )
    return print(response)

if __name__ == '__main__':
    list_users()