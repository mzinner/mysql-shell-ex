def show_password_expire(show_expired=True, session=None):
    import mysqlsh
    shell = mysqlsh.globals.shell

    if session is None:
        session = shell.get_session()
        if session is None:
            print("No session specified. Either pass a session object to this "
                  "function or connect the shell to a database")
            return

    if show_expired:
        stmt = """select concat(sys.quote_identifier(user),'@',sys.quote_identifier(host)), 
              password_last_changed, IF((cast(
              IFNULL(password_lifetime, @@default_password_lifetime) as signed)
              + cast(datediff(password_last_changed, now()) as signed) > 0),
              concat(
               cast(
              IFNULL(password_lifetime, @@default_password_lifetime) as signed)
              + cast(datediff(password_last_changed, now()) as signed), ' days'), 'expired') expires_in
              from mysql.user
              where 
              user not like 'mysql.%'"""
    else:
        stmt = """select concat(sys.quote_identifier(user),'@',sys.quote_identifier(host)), 
              password_last_changed,
              concat(
               cast(
              IFNULL(password_lifetime, @@default_password_lifetime) as signed)
              + cast(datediff(password_last_changed, now()) as signed), ' days') expires_in
              from mysql.user
              where 
              cast(
               IFNULL(password_lifetime, @@default_password_lifetime) as signed)
              + cast(datediff(password_last_changed, now()) as signed) >= 0 
              and user not like 'mysql.%';"""

    result = session.run_sql(stmt)
    shell.dump_rows(result)
