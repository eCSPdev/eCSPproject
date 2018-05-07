import boto3 as boto3

from config.s3config import s3_config
import boto
import boto.s3.connection


class s3Connection:

    def getfilesfroms3(self):
        conn = boto.connect_s3(
            aws_access_key_id=s3_config['puak'],
            aws_secret_access_key=s3_config['prak'],
            host='us-east-2',
            # is_secure=False,               # uncomment if you are not using ssl
            calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        )


    def verifybucket(self):

        session = boto3.Session(profile_name="default")
        s3client = session.client('s3', region_name="us-east-2")
        bucketname = "ecspdoctorsegarrapatientsfiles"

        try:
            response = s3client.list_buckets()
            for bucket in response['Buckets']:
                if bucket.get("Name") == bucketname:
                    print("Bucket name exist")
                    return True
                else:
                    print("Bucket Name does not exist")
                    return False
        except Exception as e:
            return e

    def uploadfile(self, location_filename, target_filename):

        try:
            # self.verifybucket()         #verifies if the bucket is valid
            session = boto3.Session(profile_name="default")
            s3resource = session.resource('s3', region_name="us-east-2")
            bucketname = "ecspdoctorsegarrapatientsfiles"

            try:
                s3resource.Bucket(bucketname).upload_file(location_filename, target_filename)
                return self.getfileurl(target_filename)
            except Exception as e:
                return e
        except Exception as e:
            return e

    def getfileurl(self, filename):

        session = boto3.Session(profile_name="default")
        s3client = session.client('s3', region_name="us-east-2")
        bucketname = "ecspdoctorsegarrapatientsfiles"

        url = s3client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucketname,
                'Key': filename, },
            ExpiresIn=86400, )
        return url