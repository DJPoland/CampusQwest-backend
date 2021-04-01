resource "aws_apigatewayv2_api" "example"{
    name                         = "CampusQwest-API"
    protocol_type                = "HTTP"
}

resource "aws_apigatewayv2_authorizer" "cognito_pool_authorizer" {
    api_id                           = aws_apigatewayv2_api.example.id
    authorizer_type                  = "JWT"
    name                             = "cognito_user_pool"
    identity_sources                 = [
        "$request.header.Authorization",
    ]
    jwt_configuration {
        audience = [
            aws_cognito_user_pool_client.client.id,
        ]
        issuer   = "https://${aws_cognito_user_pool.pool.endpoint}"
    }
}

# All AWS API integrations are defined below for API Gateway
resource "aws_apigatewayv2_integration" "leaderboard_lambda" {
    api_id                 = aws_apigatewayv2_api.example.id
    integration_method     = "POST"
    integration_type       = "AWS_PROXY"
    integration_uri        = aws_lambda_function.leaderboard_handler_lambda.invoke_arn
    payload_format_version = "2.0"
}
resource "aws_apigatewayv2_integration" "qwests_lambda" {
    api_id                 = aws_apigatewayv2_api.example.id
    integration_method     = "POST"
    integration_type       = "AWS_PROXY"
    integration_uri        = aws_lambda_function.qwest_handler_lambda.invoke_arn
    payload_format_version = "2.0"
}
resource "aws_apigatewayv2_integration" "users_lambda" {
    api_id                 = aws_apigatewayv2_api.example.id
    integration_method     = "POST"
    integration_type       = "AWS_PROXY"
    integration_uri        = aws_lambda_function.user_handler_lambda.invoke_arn
    payload_format_version = "2.0"
}
resource "aws_apigatewayv2_integration" "location_lambda" {
    api_id                 = aws_apigatewayv2_api.example.id
    integration_method     = "POST"
    integration_type       = "AWS_PROXY"
    integration_uri        = aws_lambda_function.location_handler_lambda.invoke_arn
    payload_format_version = "2.0"
}
resource "aws_lambda_permission" "leaderboard_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.leaderboard_handler_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn = "${aws_apigatewayv2_api.example.execution_arn}/*"
}
resource "aws_lambda_permission" "qwest_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.qwest_handler_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn = "${aws_apigatewayv2_api.example.execution_arn}/*"
}
resource "aws_lambda_permission" "user_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.user_handler_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn = "${aws_apigatewayv2_api.example.execution_arn}/*"
}
resource "aws_lambda_permission" "location_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.location_handler_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn = "${aws_apigatewayv2_api.example.execution_arn}/*"
}

# All routes for the API Gateway
resource "aws_apigatewayv2_route" "leaderboard_route" {
    api_id               = aws_apigatewayv2_api.example.id
    route_key            = "POST /leaderboard"
    authorization_type   = "NONE"
    target               = "integrations/${aws_apigatewayv2_integration.leaderboard_lambda.id}"
}
resource "aws_apigatewayv2_route" "user_route" {
    api_id               = aws_apigatewayv2_api.example.id
    route_key            = "GET /user"
    authorization_type   = "JWT"
    authorizer_id        = aws_apigatewayv2_authorizer.cognito_pool_authorizer.id
    target               = "integrations/${aws_apigatewayv2_integration.users_lambda.id}"
}
resource "aws_apigatewayv2_route" "start_qwest_route" {
    api_id               = aws_apigatewayv2_api.example.id
    route_key            = "POST /user/qwests/startQwest"
    authorization_type   = "JWT"
    authorizer_id        = aws_apigatewayv2_authorizer.cognito_pool_authorizer.id
    target               = "integrations/${aws_apigatewayv2_integration.qwests_lambda.id}"
}
resource "aws_apigatewayv2_route" "fetch_qwests_route" {
    api_id               = aws_apigatewayv2_api.example.id
    route_key            = "GET /user/qwests/fetchQwests"
    authorization_type   = "JWT"
    authorizer_id        = aws_apigatewayv2_authorizer.cognito_pool_authorizer.id
    target               = "integrations/${aws_apigatewayv2_integration.qwests_lambda.id}"
}
resource "aws_apigatewayv2_route" "next_location_route" {
    api_id               = aws_apigatewayv2_api.example.id
    route_key            = "POST /user/location/nextLocation"
    authorization_type   = "JWT"
    authorizer_id        = aws_apigatewayv2_authorizer.cognito_pool_authorizer.id
    target               = "integrations/${aws_apigatewayv2_integration.location_lambda.id}"
}
resource "aws_apigatewayv2_route" "update_profile_route" {
    api_id               = aws_apigatewayv2_api.example.id
    route_key            = "POST /user/updateProfile"
    authorization_type   = "JWT"
    authorizer_id        = aws_apigatewayv2_authorizer.cognito_pool_authorizer.id
    target               = "integrations/${aws_apigatewayv2_integration.users_lambda.id}"
}

resource "aws_apigatewayv2_stage" "default" {
    api_id               = aws_apigatewayv2_api.example.id
    name = "$default"
}