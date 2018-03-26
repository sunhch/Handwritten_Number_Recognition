# From https://github.com/heihualv5/mnistServer/blob/master/database_Control.py

from datetime import datetime
from cassandra.cluster import Cluster
def database_ini():
    cluster = Cluster(contact_points = ["172.25.0.2"], port = 9042)
    session = cluster.connect()
    keyspacename='mnist'
    session.execute("create keyspace if not exists mnist with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};")
    session.set_keyspace('mnist')
    session.execute("create table if not exists picdatabase(time text, filedata text ,answer int ,primary key(time));")
    return session
def database_insert(session,file,pre):
    times=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    params=[times,file,pre]
    session.execute("INSERT INTO picdatabase (time,filedata,answer) VALUES (%s, %s,%s)",params)
    result=session.execute("SELECT * FROM picdatabase")
    for x in result:
        print (x.time,x.filedata,x.answer)
    return 0
