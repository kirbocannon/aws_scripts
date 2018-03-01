# This script will update the principal (allowed accounts) on the bucket policy of network engineering bucket
# in AWS account. Principal/Account # are interchangeable terms in AWS
# You must run this script prior to running cloud formation because all lambda scripts are
# hosted in this s3 bucket. A bucket policy must already exist on the bucket for the script to work


import boto3
import json
import argparse
from botocore import exceptions as awserr

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--add-account', dest='add_account', type=str, help='Enter 12 Digit AWS Account #')
group.add_argument('--remove-account', dest='rm_account', type=str, help='Enter 12 Digit AWS Account #')
group.add_argument('--list-account', dest='list_account', const=True, action='store_const',
                    help='List accounts currently allowed access to bucket policy')
args = parser.parse_args()
bucket_name = 'my-bucket'


if __name__ == "__main__":
    try:
        s3 = boto3.client('s3')
        # check if account # entered by user is 12 digits
        if args.add_account and len(args.add_account) != 12:
            print('AWS Account # should be 12 digits only. Please try again...')
            quit()
        # get the lambda function bucket
        response = s3.get_bucket_policy(Bucket=bucket_name)
        # policy is string format, convert to json
        from_json = json.loads(response['Policy'])
        bucket_policy = from_json
        # get currently allowed accounts
        current_principals = bucket_policy['Statement'][0]['Principal']['AWS']
        # if list account argument used
        if args.list_account:
            if type(current_principals) is list:
                print('There are currently {} accounts with access to {} bucket:'.format(len(current_principals), bucket_name))
                for account in current_principals:
                    print(account)
            elif type(current_principals) is str:
                print(current_principals)
        # if add account argument used
        elif args.add_account:
            # if only one principal in existing policy, create list and append both accounts
            if type(current_principals) is str:
                new_principal_list = list()
                new_principal_list.append(current_principals)
                new_principal_list.append('arn:aws:iam::' + args.add_account + ':root')
                # update 'AWS' key with value of new principal list
                bucket_policy['Statement'][0]['Principal']['AWS'] = new_principal_list
            # if multiple principals in existing policy
            elif type(current_principals) is list:
                current_principals.append(args.add_account)
            # serialize in json string format using json.dumps. push new bucket policy to bucket.
            new_policy = json.dumps(from_json, sort_keys=True, indent=4)
            apply_bucket = s3.put_bucket_policy(Bucket=bucket_name, Policy=new_policy)
            # print(new_policy)
            status_code = apply_bucket['ResponseMetadata']['HTTPStatusCode']
            print('Account {} was successfully granted access to the {} bucket! Status code {}.'.format(args.add_account, bucket_name, status_code))
        elif args.rm_account:
            if 'arn:aws:iam::{}:root'.format(args.rm_account) in current_principals:
                current_principals.remove('arn:aws:iam::{}:root'.format(args.rm_account))
                new_policy = json.dumps(from_json, sort_keys=True, indent=4)
                apply_bucket = s3.put_bucket_policy(Bucket=bucket_name, Policy=new_policy)
                # print(new_policy)
                status_code = apply_bucket['ResponseMetadata']['HTTPStatusCode']
                print('Account {} was successfully removed from the {} bucket! Status code {}.'.format(
                    args.add_account, bucket_name, status_code))
    except awserr.ClientError as e:
        print(e)

