import boto3
from config.s3config import s3_config


class s3Connection:


    def verifybucket(self):

        session = boto3.Session(profile_name=s3_config['profile_name'])
        s3client = session.client('s3', region_name=s3_config['region_name'])

        try:
            response = s3client.list_buckets()
            for bucket in response['Buckets']:
                if bucket.get("Name") == s3_config['bucketname']:
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
            session = boto3.Session(profile_name=s3_config['profile_name'])
            s3resource = session.resource('s3', region_name=s3_config['region_name'])

            try:
                s3resource.Bucket(s3_config['bucketname']).upload_file(location_filename, target_filename)
                return self.getfileurl(target_filename)
            except Exception as e:
                return e
        except Exception as e:
            return e

    def getfileurl(self, filename):

        session = boto3.Session(profile_name=s3_config['profile_name'])
        s3client = session.client('s3', region_name=s3_config['region_name'])

        url = s3client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': s3_config['bucketname'],
                'Key': filename, },)
            # ExpiresIn=86400, ) #deberia quitarle el timing o ponerle uno mas alto
        return url