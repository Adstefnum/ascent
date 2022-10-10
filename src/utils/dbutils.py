
import pymysql.cursors
import pymysql


def get_connection(data:dict):
    if data["unix_socket"]:
        conn = get_unix_connection(data)

    conn = get_tcp_connection(data)

    return conn

def get_tcp_connection(data:dict,host,port,dbname,dbuser,dbpass,charset='utf8mb4',connect_timeout=15,autocommit=False):
    return pymysql.connect(
        host=data["host"],
        port=data["port"],
        db=data["dbname"],
        user=data["dbuser"],
        passwd=data["dbpass"],
        autocommit=autocommit,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor,  
        connect_timeout=connect_timeout
    )

def get_unix_connection(data:dict,unix_socket,port,dbname,dbuser,dbpass,charset='utf8mb4',connect_timeout=15,autocommit=False):
    return pymysql.connect(
        unix_socket=data["unix_socket"],
        port=data["port"],
        db=data["dbname"],
        user=data["dbuser"],
        passwd=data["dbpass"],
        autocommit=autocommit,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor,  # Dict is simpler than tuple
        connect_timeout=connect_timeout
    )


