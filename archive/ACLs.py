import boto3

ec2 = boto3.resource(
    'ec2'
)
client = boto3.client(
    'ec2'
)

network_acl = ec2.NetworkAcl('id')
security_group = ec2.SecurityGroup('sg-7113fa0b')

security_group_iterator = ec2.security_groups.all()

# filter kwargs are a list of dictionaries that return dictionary data back
# adding filter kwargs means each filter specified must all match to return a result
# below will look at all security groups and print the ones containing an access rule for
# 96.91.235.1/32 for ssh
security_group_filter = ec2.security_groups.filter(
    Filters=[
        {
            'Name': 'ip-permission.cidr',
            'Values': [
                '96.91.235.1/32',
            ]
        },
        {
            'Name': 'ip-permission.from-port',
            'Values': [
                '22',
            ]
        },
        {
            'Name': 'ip-permission.to-port',
            'Values': [
                '22',
            ]
        },
    ]
)

# create a list security groups which match the name specified. This should never be more than one!
#list = [s.id for s in security_group_filter if s.id == 'sg-dc4f1fa6']
#print(list)

# print security group id only
for sec_group in security_group_filter:
    print(sec_group.id)

#for sec_group in security_group_iterator:
#    print(sec_group)

# below prints out all details about all security groups, vpc associated, rules, etc
#response = client.describe_security_groups()
#print(response)