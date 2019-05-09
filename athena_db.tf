resource "aws_athena_database" "trail" {
  name   = "${var.db_name}"
  bucket = "${aws_s3_bucket.reports.bucket}"
}