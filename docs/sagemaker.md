## Installation

To use Boto3, you first need to install it and its dependencies.

### Install or update Python

Before installing Boto3, install Python 3.8 or later; support for Python 3.6 and earlier is deprecated. After the deprecation date listed for each Python version, new releases of Boto3 will not include support for that version of Python. For details, including the deprecation schedule and how to update your project to use Python 3.8, see [Migrating to Python 3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationpy3.html#guide-migration-py3).

For information about how to get the latest version of Python, see the official [Python documentation](https://www.python.org/downloads/).

### Install Boto3

Install the latest Boto3 release via **pip**:

```
pip install boto3
```



If your project requires a specific version of Boto3, or has compatibility concerns with certain versions, you may provide constraints when installing:

```
# Install Boto3 version 1.0 specifically
pip install boto3==1.0.0

# Make sure Boto3 is no older than version 1.15.0
pip install boto3>=1.15.0

# Avoid versions of Boto3 newer than version 1.15.3
pip install boto3<=1.15.3
```

## Configuration

Before using Boto3, you need to set up authentication credentials for your AWS account using either the [IAM Console](https://console.aws.amazon.com/iam/home) or the AWS CLI. You can either choose an existing user or create a new one.

For instructions about how to create a user using the IAM Console, see [Creating IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console). Once the user has been created, see [Managing access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) to learn how to create and retrieve the keys used to authenticate the user.

If you have the [AWS CLI](http://aws.amazon.com/cli/) installed, then you can use the **aws configure** command to configure your credentials file:

```
aws configure
```



Alternatively, you can create the credentials file yourself. By default, its location is `~/.aws/credentials`. At a minimum, the credentials file should specify the access key and secret access key. In this example, the key and secret key for the account are specified in the `default` profile:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```



You may also want to add a default region to the AWS configuration file, which is located by default at `~/.aws/config`:

```
[default]
region=us-east-1
```



Alternatively, you can pass a `region_name` when creating clients and resources.

You have now configured credentials for the default profile as well as a default region to use when creating connections. See [Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration) for in-depth configuration sources and options.