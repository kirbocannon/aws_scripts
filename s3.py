#!/Users/Kennyb/Documents/VirtualEnvironments/mongoDB/bin/python3

import boto3, argparse
from botocore import exceptions


# create args
parser = argparse.ArgumentParser()
parser.add_argument("action", choices=['download', 'upload', 'remove'])
parser.add_argument("bucket_name", help= "Enter the source s3 bucket name")
parser.add_argument("source_filename", help= "Enter the source file name")
parser.add_argument("-d", "--destination-filename", help= "Enter the destination file name. For uploads and downloads,"
                                                          " if not specified then the name will be the same as the source"
                                                          " filename and the location will be the client's current directory"
                                                          " This option is not needed for removing files"
                    )

parser.add_argument("-v", "--verbose", action = "store_true", help= "Verbose output")
args = parser.parse_args()
complete_flag = 0

s3_client = boto3.client(
    's3',
    #region_name='us-east-1',
    aws_access_key_id='AKIAJGU2DOXY6RNO64HA',
    aws_secret_access_key='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',

                        )

s3 = boto3.resource(
    's3',
    #region_name='us-east-1',
    aws_access_key_id='AKIAJGU2DOXY6RNO64HA',
    aws_secret_access_key='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',

                    )

# upload/download/remove files form the bucket specified
if args.action.lower() == 'download':
    try:
        if args.destination_filename: # if we were given a destination filename, then include that
            s3.meta.client.download_file(args.bucket_name, args.source_filename, args.destination_filename)
            complete_flag = 1
        else: # if no destination filename has been specified, use the same path as source filename
            s3.meta.client.download_file(args.bucket_name, args.source_filename, args.source_filename)
            complete_flag = 1
        if args.verbose and complete_flag:
            print("File {} was downloaded from the {} bucket.".format(args.source_filename, args.bucket_name))
        elif complete_flag:
            print("Download complete!")
    except exceptions.ClientError as e:
        print(e)

elif args.action.lower() == 'upload':
    try:
        if args.destination_filename: # if we were given a destination file name, then include that
            s3.meta.client.upload_file(args.source_filename, args.bucket_name, args.destination_filename)
            complete_flag = 1
        else: # if no destination filename has been specified, simply use the source argument
            s3.meta.client.upload_file(args.source_filename, args.bucket_name, args.source_filename)
            complete_flag = 1
        if args.verbose and complete_flag:
            print("File {} was uploaded to the {} bucket.".format(args.source_filename, args.bucket_name))
        elif complete_flag:
            print("Upload complete!")
    except exceptions.ClientError as e:
        print(e)

elif args.action.lower() == 'remove':
    # put code to search before deletion
    try:
        response = s3_client.delete_objects(
            Bucket= args.bucket_name,
            Delete={
                'Objects': [
                    {
                        'Key': args.source_filename,
                    },
                ],
                'Quiet': False
            },
        )
        complete_flag = 1
        if args.verbose and complete_flag:
            print("File {} was removed to the {} bucket.".format(args.source_filename, args.bucket_name))
        elif complete_flag:
            print("Deleted the following file:", response['Deleted'][0]['Key'])
    except exceptions.ClientError as e:
        print(e)
else:
    print("Please specify download, upload, or delete action.")