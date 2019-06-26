def get_fragmented_tables(percent=10, session=None):
    import mysqlsh
    shell = mysqlsh.globals.shell

    if session is None:
        session = shell.get_session()
        if session is None:
            print("No session specified. Either pass a session object to this "
                  "function or connect the shell to a database")
            return
    stmt = "select variable_value from performance_schema.global_variables where variable_name='information_schema_stats_expiry';"
    result = session.run_sql(stmt)
    stats = result.fetch_all()
    if len(stats) > 0:
        for stat in stats:
            if int(stat[0]) > 0:
                print "Warning: information_schema_stats_expiry is set to {0}.".format(*stat)

    stmt = """SELECT CONCAT(table_schema, '.', table_name) as 'TABLE', 
       ENGINE, CONCAT(ROUND(table_rows / 1000000, 2), 'M') `ROWS`, 
       CONCAT(ROUND(data_length / ( 1024 * 1024 * 1024 ), 2), 'G') DATA, 
       CONCAT(ROUND(index_length / ( 1024 * 1024 * 1024 ), 2), 'G') IDX, 
       CONCAT(ROUND(( data_length + index_length ) / ( 1024 * 1024 * 1024 ), 2), 'G') 'TOTAL SIZE', 
       ROUND(index_length / data_length, 2)  IDXFRAC, 
        CONCAT(ROUND(( data_free / 1024 / 1024),2), 'MB') AS data_free,
       CONCAT('(',
        IF(data_free< ( data_length + index_length ), 
        CONCAT(round(data_free/(data_length+index_length)*100,2),'%'),
       '100%'),')') AS data_free_pct
       FROM information_schema.TABLES  WHERE (data_free/(data_length+index_length)*100) > {limit}
       AND table_schema <> 'mysql';""".format(limit=percent)
    result = session.run_sql(stmt)
    shell.dump_rows(result)
