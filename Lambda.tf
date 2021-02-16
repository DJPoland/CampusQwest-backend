resource "aws_iam_role" "user_information_lambda" {
  name               = "user_information_lambda"
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
      "arn:aws:dynamodb:*:*:*",
    ]
  }
}

resource "aws_iam_policy" "dynamo-access-rw" {
  name   = "dynamo-access-rw"
  path   = "/"
  policy = data.aws_iam_policy_document.dynamo-access-rw.json
}

resource "aws_iam_role_policy_attachment" "dynamo-access-rw" {
  role       = aws_iam_role.user_information_lambda.name
  policy_arn = aws_iam_policy.dynamo-access-rw.arn
}

resource "aws_iam_role_policy_attachment" "basic-exec-role" {
  role       = aws_iam_role.user_information_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "user_information_lambda" {
  filename         = "user_information.zip"
  function_name    = "user_information_lambda"
  role             = aws_iam_role.user_information_lambda.arn
  handler          = "user_information.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("user_information.zip")
}

resource "aws_lambda_function" "post_confirmation_lambda" {
  filename = "post_confirmation.zip"
  function_name = "post_confirmation_lambda"
  role = aws_iam_role.user_information_lambda.arn
  handler = "post_confirmation.lambda_handler"
  runtime = "python3.8"
  timeout = 10
  source_code_hash = base64sha256("post_confirmation.zip")
}
