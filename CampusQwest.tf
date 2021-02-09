terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# aws_cognito_user_pool.pool:
resource "aws_cognito_user_pool" "pool" {
    alias_attributes           = [
        "email",
    ]
    auto_verified_attributes   = [
        "email",
    ]
    mfa_configuration          = "OPTIONAL"
    name                       = "CampusQwestUserPool"
    tags                       = {
        "CampusQwest" = "Cognito User Pool for the CampusQwest application"
    }

    account_recovery_setting {
        recovery_mechanism {
            name     = "verified_email"
            priority = 1
        }
        recovery_mechanism {
            name     = "verified_phone_number"
            priority = 2
        }
    }

    admin_create_user_config {
        allow_admin_create_user_only = false

        invite_message_template {
            email_message = "Your username is {username} and temporary password is {####}. "
            email_subject = "Your temporary password"
            sms_message   = "Your username is {username} and temporary password is {####}. "
        }
    }

    email_configuration {
        email_sending_account = "COGNITO_DEFAULT"
    }

    password_policy {
        minimum_length                   = 7 
        require_lowercase                = false 
        require_numbers                  = false
        require_symbols                  = false
        require_uppercase                = false
        temporary_password_validity_days = 7
    }

    schema {
        attribute_data_type      = "String"
        developer_only_attribute = false
        mutable                  = true
        name                     = "email"
        required                 = true

        string_attribute_constraints {
            max_length = "2048"
            min_length = "0"
        }
    }

    software_token_mfa_configuration {
        enabled = true
    }

    username_configuration {
        case_sensitive = false
    }

    verification_message_template {
        default_email_option  = "CONFIRM_WITH_LINK"
        email_message         = "Your verification code is {####}. "
        email_message_by_link = "Please click the link below to activate your account. {##Verify Email##} "
        email_subject         = "Welcome to CampusQwest!"
        email_subject_by_link = "Welcome to CampusQwest!"
        sms_message           = "Your verification code is {####}. "
    }
}

resource "aws_cognito_identity_pool" "identity_pool" {
    allow_unauthenticated_identities = false
    identity_pool_name               = "campusqwest_identity"
    openid_connect_provider_arns     = []
    saml_provider_arns               = []
    supported_login_providers        = {}
    tags                             = {}

    cognito_identity_providers {
      client_id = "56vsgokcpa2cfog3alqvocgusb"
      provider_name = "cognito-idp.us-east-1.amazonaws.com/us-east-1_BaXu0YkaN"
    }
}

resource "aws_iam_role" "query_dynamodb_lambda" {
    name = "query_dynamodb_lambda"
    assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

data "aws_iam_policy_document" "dynamo-access-rw" {
    statement {
        actions = [
            "dynamodb:DeleteItem",
            "dynamodb:GetItem",
            "dynamodb:PutItem",
            "dynamodb:Query",
            "dynamodb:Scan",
            "dynamodb:UpdateItem",
        ]
        resources = [
            "arn:aws:dynamodb:::*",
        ]
    }
}

resource "aws_iam_policy" "dynamo-access-rw" {
    name = "dynamo-access-rw"
    path = "/"
    policy = data.aws_iam_policy_document.dynamo-access-rw.json
}

resource "aws_iam_role_policy_attachment" "dynamo-access-rw" {
    role = aws_iam_role.query_dynamodb_lambda.name
    policy_arn = aws_iam_policy.dynamo-access-rw.arn
}

resource "aws_iam_role_policy_attachment" "basic-exec-role" {
    role       = aws_iam_role.query_dynamodb_lambda.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "query_dynamodb_lambda" {
    filename = "lambda_test.zip"
    function_name = "query_dynamodb_lambda"
    role = aws_iam_role.query_dynamodb_lambda.arn
    handler = "lambda_test.lambda_handler"
    runtime = "python3.8"
    timeout = 10
    source_code_hash = base64sha256("lambda_test.zip")
}
