# General mysql connector file

# Version 0.0.12 Are Casilla 20190315 -> 20191004
# json cache Version 1.0.0 Are Casilla 20220620, Szeged

# https://flask.palletsprojects.com/en/1.0.x/tutorial/database/  LEARN
# https://stackoverflow.com/questions/15083967/when-should-flask-g-be-used
# https://speakerdeck.com/mitsuhiko/advanced-flask-patterns-1?slide=20

"""
REPEATABLE READ
https://stackoverflow.com/questions/5943418/chronic-stale-results-using-mysqldb-in-python
https://dev.mysql.com/doc/refman/8.0/en/set-transaction.html#isolevel_repeatable-read
https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-model.html
"""
import config
import pymysql.cursors
import os
import time
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

mydbhost = os.getenv("DB_HOST", 'localhost')
mydbport = int(os.getenv("DB_PORT", '3306'))
mydbname = os.getenv("DB_JSON_DATABASE", '')
if not mydbname:
    mydbname = os.getenv("DB_DATABASE", 'jsonlab') 

mydbuser = os.getenv("DB_USERNAME", 'root')
mydbpass = os.getenv("DB_PASSWORD", 'topsecret')


config.logging.info(f"Using DB host: {mydbhost}:{str(mydbport)} db: {mydbname}"
                    f"User: {mydbuser}")


def get_connection(autocommit=True):
    return pymysql.connect(
        host=mydbhost,
        port=mydbport,
        db=mydbname,
        user=mydbuser,
        passwd=mydbpass,
        autocommit=autocommit,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,  # Dict is simpler than tuple
        connect_timeout=15
    )



def sql_exec(sql, param=None, cursor=None, fetch_one=False, fetch_all=False, commit=False):
    """Used to execute MySQL statements. We try to execute SQL via this function. This enfore things like cnx.ping
       Usage example: bgmysql.sql_exec(cur, sql, commit = True)"""
    # https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.ping
    # ping(reconnect=True) Check if the server is alive. Connection will timeout if we do not use this
    if cursor is not None:
        cur = cursor
    else:
        conn = get_connection()
        cur = conn.cursor()
    rows = []

    if not param:
        ret = cur.execute(sql)
    else:
        ret = cur.execute(sql, param)

    if commit and not cursor:
        conn.commit()

    if fetch_one:
        rows = cur.fetchone()

    if fetch_all:
        rows = cur.fetchall()

    if not fetch_one and not fetch_all:
        rows = ret

    if not cur:
        cur.close()
        conn.close()
    return rows


def sql_fetchall(sql, param=None):
    """
        Used to execute MySQL statements with autocommit. We try to execute SQL via this function.
    """
    conn = get_connection(autocommit=True)
    cur = conn.cursor()

    if param is None:
        cur.execute(sql)
    else:
        cur.execute(sql, param)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def sql_fetchone(sql, param=None):
    """
        Used to execute MySQL statements with autocommit. We try to execute SQL via this function.
    """
    conn = get_connection(autocommit=True)
    cur = conn.cursor()

    if param is None:
        cur.execute(sql)
    else:
        cur.execute(sql, param)
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def sql_update(sql, param=None, cursor=None, autocommit=False):
    """
        Used to update or insert MySQL
    """
    if cursor is not None:
        cur = cursor
    else:
        conn = get_connection(autocommit=autocommit)
        cur = conn.cursor()

    if param is None:
        ret = cur.execute(sql)
    else:
        ret = cur.execute(sql, param)
    if cursor is None:
        cur.close()
        conn.close()
    return ret


def test_mysql():
    start = time.time()
    sql = "select * from contract_registers"
    rows = sql_fetchall(sql)
    for row in rows:
        config.logging.info('Row %s', row)
    end = time.time()
    config.logging.info('Tenants Total rows %s', len(rows))
    config.logging.info('Elapsed  time %s', time.strftime(
        '%H:%M:%S', time.gmtime(end - start)))
    # config.logging.info(time.isoformat(sep=' ', timespec='milliseconds'))

# https://stackoverflow.com/questions/22699807/python-mysql-using-pymysql-auto-reconnect
# https://pymysql.readthedocs.io/en/latest/modules/connections.html
# https://www.python.org/dev/peps/pep-0249/#connection-objects
# pymysql.err.OperationalError:
# (2006, "MySQL server has gone away (ConnectionResetError(104, 'Connection reset by peer'))")


if __name__ == '__main__':
    pass
    test_mysql()
