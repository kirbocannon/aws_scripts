import boto3
from botocore.exceptions import ClientError, ParamValidationError
import json


ec2 = boto3.resource(
    'ec2'
)
client = boto3.client(
    'ec2'
)


# duplicate_test_filter = [{'Name':'tag:Name', 'Values':['*test']}]
# duplicate_test_subnet_id = client.describe_subnets(Filters=duplicate_test_filter)['Subnets'][0]['SubnetId']
# print(duplicate_test_subnet_id)
#
# dmvpn_filter = [{'Name':'tag:Name', 'Values':['*DMVPN*']}]
# dmvpn_subnets = client.describe_subnets(Filters=dmvpn_filter)['Subnets']
# for subnet in dmvpn_subnets:
#     print(subnet['SubnetId'])

#vpc = ec2.Vpc('id')




# get default vpc
vpc_filter = [{'Name': 'isDefault', 'Values': ['true']}]
vpc_id =  client.describe_vpcs(DryRun=False, Filters=vpc_filter)['Vpcs'][0]['VpcId']
# filters for describing  vpc resources
ig_filter = [{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}]
rt_tbl_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}]
subnet_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}]
sg_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}]
nacl_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'default', 'Values': ['false']}]
# describe vpc associated resources
rt_tbls = client.describe_route_tables(DryRun=False, Filters=rt_tbl_filter)
int_gateways = client.describe_internet_gateways(DryRun=False, Filters=ig_filter)
subnets = client.describe_subnets(DryRun=False, Filters=subnet_filter)
security_groups = client.describe_security_groups(DryRun=False, Filters=sg_filter)
nacls = client.describe_network_acls(DryRun=False, Filters=nacl_filter)

def except_error(function):
    def checked_function(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except (ClientError, ParamValidationError) as e:
            print(e)
        return function
    return checked_function

@except_error
def delete_default_subnets():
    for subnet in subnets['Subnets']:
        client.delete_subnet(DryRun=False, SubnetId=subnet['SubnetId'])

@except_error
def delete_default_route_tables():
    for table in rt_tbls['RouteTables']:
        client.delete_route_table(DryRun=False, RouteTableId=table['RouteTableId'])

@except_error
def delete_default_network_acls():
    for nacl in nacls['NetworkAcls']:
        client.delete_network_acl(DryRun=False, NetworkAclId=nacl['NetworkAclId'])

@except_error
def delete_default_security_groups():
    for security_group in security_groups['SecurityGroups']:
        if security_group['GroupName'] != 'default':
            client.delete_security_group(DryRun=False, GroupId=security_group['GroupId'])

@except_error
def delete_default_internet_gateways():
    for gateway in int_gateways['InternetGateways']:
        client.detach_internet_gateway(DryRun=False, InternetGatewayId=gateway['InternetGatewayId'], VpcId=vpc_id)
        client.delete_internet_gateway(DryRun=False, InternetGatewayId=gateway['InternetGatewayId'])

@except_error
def delete_default_vpc():
    client.delete_vpc(DryRun=False, VpcId=vpc_id)

delete_default_subnets()
delete_default_route_tables()
delete_default_network_acls()
delete_default_security_groups()
delete_default_internet_gateways()
delete_default_vpc()



#print(json.dumps(nacls, sort_keys=True, indent=4))

#print(json.dumps(int_gateways, sort_keys=True, indent=4))


#json.dumps(response, sort_keys=True, indent=4)


#client.delete_vpc(DryRun=False, VpcId=default_vpc_id)




# internet_filter = [{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'tag:Name', 'Values': ['*INTERNET*']}]
# internet_subnets = client.describe_subnets(DryRun=False, Filters=internet_filter)
# internet_route_table = client.describe_route_tables(DryRun=False, Filters=internet_filter)
# internet_route_table_id = internet_route_table['RouteTables'][0]['RouteTableId']
#
# for subnet in internet_subnets['Subnets']:
#     associate_subnet = client.associate_route_table(
#         DryRun=False,
#         SubnetId=subnet['SubnetId'],
#         RouteTableId=internet_route_table_id
#    )




#json.dumps(response, sort_keys=True, indent=4)
#print(duplicate_test_subnet)















# group_name = 'test-sec-group'
#
# create_sec_group = client.create_security_group(
#     GroupName= group_name,
#     Description='This is a test group',
# )
#
# group_id = create_sec_group.id





# delete_sec_group = client.delete_security_group(
#     GroupName=group_name,
#     GroupId=group_id,
# )