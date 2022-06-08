"""EC2 module for SREAWS package."""
import sys

from sreaws.aws import botoClient
from sreaws.errors import errorNotify


# example of writing pagination without using
# boto3's built in paginators
def getWhileTrueInstances(profile=None, region="eu-west-2"):
    """Return a list of instances in the account/region"""
    try:
        kwargs = {
            "service": ec2,
            "profile": profile,
            "region": region,
        }
        ec2 = botoClient(**kwargs)
        instances = []
        kwargs = {}
        while true:
            res = ec2.describe_instances(**kwargs)
            if "Reservations" in res:
                instances.extend(res["Reservations"])
            if "NextToken" not in res:
                break
            kwargs["NextToken"] = res["NextToken"]
        return instances
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def getInstances(profile=None, region="eu-west-2"):
    """Returns a list of instances in the region in the account."""
    try:
        kwargs = {
            "service": ec2,
            "profile": profile,
            "region": region,
        }
        ec2 = botoClient(**kwargs)
        pag = ec2.get_paginator("describe_instances")
        iterator = pag.paginate()
        instances = [x for x in iterator]
        return instances
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
