from __future__ import print_function
import boto3
from botocore.exceptions import ClientError, ParamValidationError


def internet_association(event, context):
    client = boto3.client('ec2')
    site_code = 'myVPC'
    # set up filters and describe calls
    vpc_filter = [{'Name': 'tag:Name', 'Values': [site_code]}]
    vpc_id = client.describe_vpcs(DryRun=False, Filters=vpc_filter)['Vpcs'][0]['VpcId']
    internet_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'tag:Name', 'Values': ['*INTERNET*']}]
    default_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'tag:Name', 'Values': ['*DEFAULT*']}]
    internet_subnets = client.describe_subnets(DryRun=False, Filters=internet_filter)
    default_route_table = client.describe_route_tables(DryRun=False, Filters=default_filter)
    internet_route_table = client.describe_route_tables(DryRun=False, Filters=internet_filter)
    internet_route_table_id = internet_route_table['RouteTables'][0]['RouteTableId']
    default_rt_assoc = default_route_table['RouteTables'][0]['Associations']
    lst_of_internet_subnets = [k.get('SubnetId') for k in internet_subnets['Subnets']]

    # disassociate INTERNET subnets from DEFAULT. Then set INTERNET subnets to INTERNET route table
    for association in default_rt_assoc:
        if association.get('SubnetId') in lst_of_internet_subnets:
            client.disassociate_route_table(
                DryRun=False,
                AssociationId=association['RouteTableAssociationId']
            )
            client.associate_route_table(
                DryRun=False,
                SubnetId=association['SubnetId'],
                RouteTableId=internet_route_table_id
            )

