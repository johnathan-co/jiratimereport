Jira Time Report Generator {AVR}
==========================

The Jira Time Report Generator will provide an overview of the work spent on issues of a particular Jira project in a 
timespan period. By default, the From_Date is the first day of the previous month and the To_Date is the last day of the 
previous month of the {today} month. For example, running the script on 1/1/2021 will give you From_Date 12/01/2020 and To_Date 12/31/2020.

By default, the output will be sent via excel.

    export PYTHONIOENCODING=UTF-8  
    read -s -p "Enter Password: " mypassword
    python jiratimereport.py project

Usage of the script:

    usage: jiratimereport.py [-h] [--to_date TO_DATE]
                             [--output {excel,csv,console}]
                             [--ssl_certificate SSL_CERTIFICATE]
                             project  
    
    example: python jiratimereport.py BPAPA
    
    positional arguments:
      jira_url              The Jira URL
      user_name             The user name to use for connecting to Jira
      api_token             The API token to use for connecting to Jira
      project               The Jira project to retrieve the time report
      from_date             The date to start the time report, format yyyy-mm-dd
    
    optional arguments:
      -h, --help            show this help message and exit
      --to_date TO_DATE     The date to end the time report (the end date is
                            inclusive), format yyyy-mm-dd
      --output {excel,csv,console}
                            The output format
      --ssl_certificate SSL_CERTIFICATE
                            The location of the SSL certificate, needed in case of
                            self-signed certificates
                            

