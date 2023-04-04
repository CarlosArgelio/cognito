import boto3

cognito = boto3.client('cognito-idp')

def add_user_to_group(*args):

    groups = args

    for group in groups:
    
        response = cognito.admin_add_user_to_group(
            UserPoolId='',
            Username='user-10',
            GroupName=group
        )

    return response

if __name__ == '__main__':
    add_user_to_group('develop','admin')