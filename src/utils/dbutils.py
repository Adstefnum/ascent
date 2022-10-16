
import pymysql.cursors
import pymysql


def get_connection(data:dict):
    if data["unix_socket"]:
        conn = get_unix_connection(data)

    conn = get_tcp_connection(data)

    return conn

def get_tcp_connection(data:dict,charset='utf8mb4',connect_timeout=15,autocommit=False):
    print(data)
    return pymysql.connect(
        host=data["host"],
        port=int(data["port"]),
        db=data["dbname"],
        user=data["user"],
        passwd=data["dbpass"],
        autocommit=autocommit,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor,  
        connect_timeout=connect_timeout
    )

def get_unix_connection(data:dict,charset='utf8mb4',connect_timeout=15,autocommit=False):
    return pymysql.connect(
        unix_socket=data["unix_socket"],
        port=data["port"],
        db=data["dbname"],
        user=data["user"],
        passwd=data["dbpass"],
        autocommit=autocommit,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor,  # Dict is simpler than tuple
        connect_timeout=connect_timeout
    )


