resource "aws_iam_role" "assume_role_lambda" {
  name               = "assume_role_lambda"
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
  role       = aws_iam_role.assume_role_lambda.name
  policy_arn = aws_iam_policy.dynamo-access-rw.arn
}
resource "aws_iam_role_policy_attachment" "basic-exec-role" {
  role       = aws_iam_role.assume_role_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

// Below defines all of the lambda functions and their respective environments that are zipped.
resource "aws_lambda_function" "user_handler_lambda" {
  filename         = "user_handler.zip"
  function_name    = "user_handler_lambda"
  role             = aws_iam_role.assume_role_lambda.arn
  handler          = "user_handler.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("user_handler.zip")
}
resource "aws_lambda_function" "qwest_handler_lambda" {
  filename         = "qwest_handler.zip"
  function_name    = "qwest_handler_lambda"
  role             = aws_iam_role.assume_role_lambda.arn
  handler          = "qwest_handler.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("qwest_handler.zip")
}
resource "aws_lambda_function" "leaderboard_handler_lambda" {
  filename         = "leaderboard_handler.zip"
  function_name    = "leaderboard_handler_lambda"
  role             = aws_iam_role.assume_role_lambda.arn
  handler          = "leaderboard_handler.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("leaderboard_handler.zip")
}
resource "aws_lambda_function" "location_handler_lambda" {
  filename         = "location_handler.zip"
  function_name    = "location_handler_lambda"
  role             = aws_iam_role.assume_role_lambda.arn
  handler          = "qwest_information.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("location_handler.zip")
}
resource "aws_lambda_function" "confirmation_handler_lambda" {
  filename         = "confirmation_handler.zip"
  function_name    = "confirmation_handler_lambda"
  role             = aws_iam_role.assume_role_lambda.arn
  handler          = "confirmation_handler.lambda_handler"
  runtime          = "python3.8"
  timeout          = 10
  source_code_hash = base64sha256("confirmation_handler.zip")
}
