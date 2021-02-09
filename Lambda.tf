resource "aws_iam_role" "query_dynamodb_lambda" {
  name               = "query_dynamodb_lambda"
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
  name   = "dynamo-access-rw"
  path   = "/"
  policy = data.aws_iam_policy_document.dynamo-access-rw.json
}

resource "aws_iam_role_policy_attachment" "dynamo-access-rw" {
  role       = aws_iam_role.query_dynamodb_lambda.name
  policy_arn = aws_iam_policy.dynamo-access-rw.arn
}

resource "aws_iam_role_policy_attachment" "basic-exec-role" {
  role       = aws_iam_role.query_dynamodb_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "query_dynamodb_lambda" {
  filename         = "lambda_test.zip"
  function_name    = "query_dynamodb_lambda"
  role             = aws_iam_role.query_dynamodb_lambda.arn
  handler          = "lambda_test.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("lambda_test.zip")
}
