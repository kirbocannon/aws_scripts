import boto3

def callServerStatus():

    ec2 = boto3.resource(
        'ec2',
        region_name='us-east-1',
        aws_access_key_id = 'AKIAJGU2DOXY6RNO64HA',
        aws_secret_access_key = '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',

    )

    #check running instances and their health
    instance_cnt = 0
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        instance_cnt +=1
        print('Instance ID: ', instance.id, '\n' + 'Instance Type: ', instance.instance_type)
        for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
            print('Health Check: ', status['InstanceStatus']['Details'][0]['Status'].upper())

            if status['InstanceStatus']['Details'][0]['Status'].upper() == 'PASSED':
                returned_status = 1
                return returned_status
            else:
                returned_status = 0
                return returned_status

    print('\n' + 'Amount of running instances :', instance_cnt)

#callServerStatus()



