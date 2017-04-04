import boto3


if __name__ == "__main__":
    ec2 = boto3.resource('ec2')
    instance_iterator = ec2.instances.all()
    for instance in instance_iterator:
        print(instance.key_name)




