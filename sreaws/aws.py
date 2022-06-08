"""aws module for SREAWS package."""
import sys

import boto3

from sreaws.errors import errorNotify


def bSession(profile=None, region="eu-west-2"):
    """returns a boto3 session."""
    try:
        sess = boto3.session(profile_name=profile, default_region=region)
        return sess
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def botoClient(service="iam", profile=None, region="eu-west-2"):
    """returns a boto3 client for the named service."""
    try:
        sess = bSession(profile=profile, region=region)
        bcli = sess.client(service)
        return bcli
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def botoResource(service="ec2", profile=None, region="eu-west-2"):
    """returns a boto3 resource for the named service."""
    try:
        sess = bSession(profile=profile, region=region)
        bres = sess.resource(service)
        return bres
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
