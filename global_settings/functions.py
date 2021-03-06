import boto3
from time import time
from botocore.exceptions import NoCredentialsError
from .models import CloudfrontDistribution

def invalidate_cloudfront_caches():
    try:
        distribution = CloudfrontDistribution.objects.all()[0]
        client = boto3.client('cloudfront')
        response = client.create_invalidation(
            DistributionId=distribution.distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        '/apps/cms/api/*' # invalidate the entire cache for the website
                    ],
                },
                'CallerReference': str(time()).replace(".", "")
            }
        )
    except CloudfrontDistribution.DoesNotExist:
        return
    except IndexError:
        return
    except NoCredentialsError:
        print('No AWS credentials set - unable to invalidate cache')