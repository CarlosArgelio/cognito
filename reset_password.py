import boto3


cognito = boto3.client('cognito-idp')

def reset_password():
    response = cognito.admin_set_user_password(
    UserPoolId='',
    Username='user-01',
    Password='$Rancho32$',
    Permanent=True
)
    return response


if __name__ == '__main__':
    reset_password()