output "create_query" {
  value = aws_athena_named_query.create_table.name
}

output "db_name" {
  value = aws_athena_database.trail.name
}

