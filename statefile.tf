terraform {
  backend "s3" {
    bucket  = "terraform-trackit"
    key     = "cloudtrail_athena/"
    region  = "us-west-2"
    encrypt = "true"
  }
}

