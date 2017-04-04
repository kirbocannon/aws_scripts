import boto3


ec2 = boto3.resource(
                    'ec2',

                    )



#snapshot = ec2.create_snapshot(VolumeId='vol-005af08345b90fb74', Description='RHEL7-copy2')

