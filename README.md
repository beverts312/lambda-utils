# Bails Lambda Utils

For making lambda's easier

`pip install bails-lambda-utils`

![](https://img.shields.io/pypi/v/bails_lambda_utils)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=beverts312_lambda-utils&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=beverts312_lambda-utils)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=beverts312_lambda-utils&metric=coverage)](https://sonarcloud.io/summary/new_code?id=beverts312_lambda-utils)

## Usage

### Decorators
The libarary provides a decorator `lambda_handler` which should be attached to the any handler recieiving API calls.
The decorator will automatically map exceptions to appriorate response types:
|Exception|Response|
|-|-|
|pynamodb.exceptions.DoesNotExist|404 - Not Found|
|bails_lambda_utils.errors.PermissionError|403 - Forbidden|
|bails_lambda_utils.errors.RequiredParamException|400 - Specifying which param is missing|
|Exception|500 - With reference to aws_request_id|

Example:
```
from bails_lambda_utils.handler import lambda_handler
from bails_lambda_utils.responses import Response

@lambda_handler
def get(event, context={}):
    #... some logic
    return Response(status_code=200, message="ok").to_dict()
```

### Responses + Encoders
Docs coming soon

### Misc Utils
Docs coming soon