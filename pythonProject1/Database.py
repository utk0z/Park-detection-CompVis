import sqlite3 as sql
def create_table():
    conn=sql.connect('IsFree.db')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS COORDİNATES(
    id integer PRIMARY KEY,
    X_coordinate integer,
    Y_coordinate integer,
    UpdateTime text,
    isFree integer 
    )""")
    conn.commit()
    conn.close()
def insert(X_coordinate,Y_coordinate,isFree):
    conn = sql.connect('IsFree.db')
    cursor = conn.cursor()
    add_command = """INSERT INTO COORDİNATES(X_coordinate,Y_coordinate,isFree) VALUES {}"""
    data = (X_coordinate,Y_coordinate,isFree)
    cursor.execute(add_command.format(data))
    conn.commit()
    conn.close()
def update_isfree(X_coordinate,Y_coordinate,isFree):
    conn = sql.connect('IsFree.db')
    cursor = conn.cursor()

    upd_command = """UPDATE COORDİNATES SET isFree = {} WHERE X_coordinate = {} AND Y_coordinate = {} """
    cursor.execute(upd_command.format(isFree,X_coordinate,Y_coordinate))
  #  updtime_command ="""UPDATE CROORDİNATES SET UpdateTime DateTime('now', 'localtime') WHERE X_coordinate = {} AND Y_coordinate = {}"""
   # cursor.execute(updtime_command.format(X_coordinate,Y_coordinate))
    #firebase güncelleme yap
    conn.commit()
    conn.close()
def delete_coordinate():
    conn = sql.connect('IsFree.db')
    cursor = conn.cursor()

    dlt_command = """DELETE FROM COORDİNATES WHERE ID = (SELECT MAX(ID) FROM COORDİNATES)"""
    cursor.execute(dlt_command)

    conn.commit()
    conn.close()





