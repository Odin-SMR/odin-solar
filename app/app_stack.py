from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_s3 as s3,
)
from constructs import Construct


class OdinSolarStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        solar_bucket = s3.Bucket.from_bucket_name(
            self, "SolarBucket", "odin-solar"
        )

        download_solar = _lambda.DockerImageFunction(
            self,
            "OdinSolarDownloadFunction",
            code=_lambda.DockerImageCode.from_image_asset("./app/handler"),
            architecture=_lambda.Architecture.X86_64,
            timeout=Duration.seconds(60),
            memory_size=256,
        )

        # Define the CloudWatch event rule
        rule = events.Rule(
            self,
            "OdinSolarScheduleRule",
            schedule=events.Schedule.cron(minute="15", hour="01"),
        )

        # Add the Lambda function as a target of the rule
        rule.add_target(targets.LambdaFunction(download_solar))
        solar_bucket.grant_read_write(download_solar)
