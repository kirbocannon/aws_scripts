import boto3


ec2 = boto3.resource(
                    'ec2',
                    region_name='us-west-2',
                    aws_access_key_id = 'AKIAJGU2DOXY6RNO64HA',
                    aws_secret_access_key = '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',

                    )



#snapshot = ec2.create_snapshot(VolumeId='vol-005af08345b90fb74', Description='RHEL7-copy2')

