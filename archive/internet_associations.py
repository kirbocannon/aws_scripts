import boto3
from botocore.exceptions import ClientError, ParamValidationError
import json


ec2 = boto3.resource(
    'ec2'
)
client = boto3.client(
    'ec2'
)

# set up filters and describe calls
vpc_filter = [{'Name': 'tag:Name', 'Values': ['BK']}]
vpc_id =  client.describe_vpcs(DryRun=False, Filters=vpc_filter)['Vpcs'][0]['VpcId']
internet_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'tag:Name', 'Values': ['*INTERNET*']}]
internal_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'tag:Name', 'Values': ['*DEFAULT*']}]
internet_subnets = client.describe_subnets(DryRun=False, Filters=internet_filter)
default_route_table = client.describe_route_tables(DryRun=False, Filters=internal_filter)
internet_route_table = client.describe_route_tables(DryRun=False, Filters=internet_filter)
internet_route_table_id = internet_route_table['RouteTables'][0]['RouteTableId']
default_rt_assoc = default_route_table['RouteTables'][0]['Associations']
lst_of_internet_subnets = [k.get('SubnetId') for k in internet_subnets['Subnets']]

# disassociate INTERNET subnets from DEFAULT Moody's. Then set INTERNET subnets to INTERNET route table
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


    #if association['SubnetId'] in 'blah':
    #    print("yes")

    #print(associaiton)


#for subnet in internet_subnets['Subnets']:



#print(internal_rt_assoc)

#print(json.dumps(internal_route_table, sort_keys=True, indent=4))