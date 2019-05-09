import boto3
import sys, argparse
import time

class Athena:
    def __init__(self,s3_bucket,database,sql_file):
        self.s3_bucket = s3_bucket
        self.database   = database
        self.sql_file  = sql_file
        self.athena = boto3.client('athena')

    def query_athena(self):
        sql=open(self.sql_file).read()
        try:
            execution = self.athena.start_query_execution(
                        QueryString=sql,
                        QueryExecutionContext={
                            'Database': self.database
                        },
                        ResultConfiguration={
                            'OutputLocation': f's3://{self.s3_bucket}/'
                        }
                    )
            exe_id = execution['QueryExecutionId']
            result = self.athena.get_query_execution(QueryExecutionId=exe_id)
            query_state = result['QueryExecution']['Status']['State']
            sys.stdout.write('Running Query.')
            while query_state == 'RUNNING':
                result = self.athena.get_query_execution(QueryExecutionId=exe_id)
                query_state = result['QueryExecution']['Status']['State']
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(2)
        except Exception as e:
                sys.exit(e)
    
def arg_parse(*args, **kwargs):
    parser = argparse.ArgumentParser( prog=sys.argv[0], description="An utility to run the SQL files in Athena")

    parser.add_argument(
        "-rb", "--reports-bucket",
        action='store',
        help="Reports Bucket Name",
        dest='reports_bucket_name'
    )

    parser.add_argument(
        "-db", "--database",
        action='store',
        help="DataBase Name",
        dest='database'
    )

    parser.add_argument(
        "-s", "--sql-file",
        action='store',
        help="SQL File",
        dest='sql_file'
    )

    parsed = parser.parse_args()
    main(parsed)


def main(parsed):
    ath = Athena(parsed.reports_bucket_name,parsed.database,parsed.sql_file)
    ath.query_athena()
    # for query_id in client.list_named_queries()['NamedQueryIds']:
    #     named_query=client.get_named_query(NamedQueryId=query_id)['NamedQuery']
    #     if  named_query['Name'] == 'Create-Cloudtrail-Table':
    #         databse=named_query['Database']
    #         sql=named_query['sql']

if __name__ == '__main__':
    try:
        sys.exit(arg_parse(*sys.argv))
    except KeyboardInterrupt:
        exit('CTL-C Pressed.')
    except Exception as e:
        exit(f'Unknown Error: {e}')