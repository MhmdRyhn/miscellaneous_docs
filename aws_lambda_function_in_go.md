# AWS Lambda Function in GoLang
AWS Lambda is a well known and great cloud Function as a Service (FaaS). And Google's **GoLang** is a statically typed, 
compiled programming language. It is widely popular for its being super fast and it's built in concurrency.

In this blog post, we will discuss about how can we use GoLang in AWS Lambda function. In this demonstration I'm using 
Go version 1.15. Following things are assumed: 
- You know how to setup GoLang for development in Unix systems
- You are familiar with **AWS Lambda** 

As **Go** is a compiled language, we cannot use the Lambda Function's editor to edit the source code which we can do in 
the case of scripting languages like Python, NodeJS etc. In this case, we will build the lambda function's file which 
will create an executable binary that is to be deployed to AWS Lambda. Let's see step by step how a **GoLang** function 
can be created and deployed to AWS Lambda. We will use the following project structure in this demo, but you can use 
any structure as your convenience.

```text
lambda-function-in-golang/
    cmd/
        main.go
        main_test.go
        ...
    deploy/
        ...
    scripts/
        ...
    go.mod
    go.sum
```


# Lambda Handler
Let's look at how `cmd/main.go` look like:
```text
package main


import (
	"fmt"

	"github.com/aws/aws-lambda-go/lambda"
)


type LambdaEvent struct {
	Name string `json:"name"`
	Age int `json:"age"`
}


type LambdaResponse struct {
	Message string `json:"message"`
}


func LambdaHandler(event LambdaEvent) (LambdaResponse, error) {
	return LambdaResponse {
		Message: fmt.Sprintf("%s is %d years old.", event.Name, event.Age),
	}, nil
}


func main ()  {
	lambda.Start(LambdaHandler)
}
```

`github.com/aws/aws-lambda-go/lambda` is the aws SDK for GoLang. `LambdaEvent` is used to store the event and this is 
a custom event. Instead of using this custom event, different AWS service specific events can be used. For AWS service 
events `github.com/aws/aws-lambda-go/events` this package can be used. `LambdaResponse` is used store the response to 
be returned.

Some rules regarding the Lambda Handler are as follows:
- The **Handler** must be a function.
- Handler may take 0 to 2 arguments. 
    - If there is only one argument, it must be an event from `github.com/aws/aws-lambda-go/events` this package or 
    any custom event.  
    - If there are 2 arguments used, the first one must be `context.Context`.
- Handler may return 0 to 2 value.
    - If there is only one value, it must implement `error`.
    - If there are 2 return values, the second value must implement `error`.

Valid Handler function signature is one of the following:
- func ()
- func () error
- func (TIn), error
- func () (TOut, error)
- func (context.Context) error
- func (context.Context, TIn) error
- func (context.Context) (TOut, error)
- func (context.Context, TIn) (TOut, error)

Here `TIn` and `TOut` is the event and response respectively.

**NOTE:** Global variables that are independent of your Lambda function's handler code can be declared and modified. 
Handler may declare an `init` function that is executed when your handler is loaded.


# Create Compiled Executable And Prepare For AWS Lambda
- To build the executable, run the following command in project root directory.
```shell script
GOOS=linux go build cmd/main.go
```
`GOOS=linux` will ensure that the compiled executable is linux environment compatible, even if it is compiled in non-Linux 
environment.
- Zip the compiled executable.
```shell script
zip function.zip main
```


# Create The Function
- Create the lambda function using the following command
```shell script
aws lambda --profile craftsmen --region us-east-2 create-function --function-name lambda-go --runtime go1.x \
--zip-file fileb://function.zip --handler main --role arn:aws:iam::{account-id}:role/service-role/basic_lambda_execution
```
Replace `{account-id}` in the above command with your actual account id. You can use your own role ARN too.


# Test The Function
- Configure test event as follows
```json
{
    "name": "Rayhan",
    "age": 25
}
```
- Test the function. This will give **{ "message": "Rayhan is 25 years old." }** as response.


# Lambda Layers
You may wonder that external package (AWS GoLang SDK) has been used but there is no Lambda Layer for the external 
packages. Actually when the application is compiled, the compiled executable includes all the external packages used. 
To get benefit from the AWS Lambda Layer, GoLang Plugins can be used. Golang Plugins is the feature released in the 
Go1.8. It allows you to dynamically load shared libraries (`.so` files). It gives you an opportunity to export some of 
your code to the separate library or use the plugin prepared and compiled by someone else.


The full project source code along with the **terraform** configuration can be found 
[**here**](https://github.com/mhmdryhn/lambda-function-in-golang).

**Stay in Peace and keep coding !!!** 


# References
- [Building Lambda functions with Go](https://docs.aws.amazon.com/lambda/latest/dg/lambda-golang.html)
- [AWS Lambda function handler in Go](https://docs.aws.amazon.com/lambda/latest/dg/golang-handler.html)
- [AWS Lambda deployment package in Go](https://docs.aws.amazon.com/lambda/latest/dg/golang-package.html)
- [How to build pluggable Golang application and benefit from AWS Lambda Layers.](https://medium.com/nordcloud-engineering/how-to-build-pluggable-golang-application-and-benefit-from-aws-lambda-layers-154c8117df9b)
