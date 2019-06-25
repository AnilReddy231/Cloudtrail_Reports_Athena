resource "aws_cloudtrail" "trail" {
  name                          = "actions-trail"
  s3_bucket_name                = aws_s3_bucket.logs.id
  include_global_service_events = false
}

