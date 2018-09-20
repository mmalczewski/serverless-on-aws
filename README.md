# Serverless + AWS

<img src="img/serverless-logo.png" height="100">

----------


This is repository for lightning talk about Serverless framework on AWS.

## Example

#### Requirements
- [Serverless framework](https://serverless.com/framework/docs/providers/aws/guide/installation/) installed.
- [AWS CLI](https://aws.amazon.com/cli/) installed and proper profile created

  ~/.aws/config
  ```
  [profile demo-aws-profile]
  output = json
  region = eu-central-1
  ```

  ~/.aws/credentials
  ```
  [demo-aws-profile]
  aws_access_key_id = XXXXXXXXXXXXXXXXXXXX
  aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  ```
- [jq JSON processor](https://stedolan.github.io/jq/) installed (optional).

#### Deploy

deploy and run example:
- go to `example` directory
- deploy serverless service

  ```bash
  # default dev stage
  serverless deploy

  # prod stage
  serverless deploy --stage prod
  ```

- test API call

  ```bash
  # call dev stage
  curl -v -H "x-api-key: DEV-API-KEY" https://DEV-API-ID.execute-api.eu-central-1.amazonaws.com/dev/example | jq

  # call prod stage
  curl v -H "x-api-key: PROD-API-KEY" https://PROD-API-ID.execute-api.eu-central-1.amazonaws.com/dev/example | jq
  ```

**NOTE:**  The URL displayed next to Invoke URL should look something like this, where `API-ID` is the identifier API Gateway assigns to your API, `REGION-ID` is the AWS region identifier (for example, us-east-1 ) where you deployed your API, and `STAGE-NAME` is the name of the stage for the API you want to call:
```
https://API-ID.execute-api.REGION-ID.amazonaws.com/STAGE-NAME/RESOURCE-PATH
```

#### Cleanup

cleanup AWS environment:
- go to `example` directory
- remove serverless service

  ```bash
  # default dev stage
  serverless remove

  # prod stage
  serverless remove --stage prod
  ```

## Links
- [Serverless AWS Guide](https://serverless.com/framework/docs/providers/aws/guide/intro/)
- [Invoking an API in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html#how-to-call-api-console)


## License

The MIT License, see [LICENSE](LICENSE)
