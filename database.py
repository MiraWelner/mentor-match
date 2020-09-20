import sqlite3


def open_db(name):
    global userdb
    userdb = sqlite3.connect(name)
    global pointer
    pointer = userdb.cursor()

def add_qnnaire(name, questionct):
    pointer.execute("CREATE TABLE " + name + " (id INTEGER PRIMARY KEY AUTOINCREMENT);")
    for q in range(questionct):
        headname = "q" + str(q)
        pointer.execute("ALTER TABLE " + name + " ADD " + headname + " TEXT;")
    userdb.commit()


def add_user(qnnaire, answers):
    n=len(answers)
    hnamemat=["q"+str(i) for i in range(n)]
    print(hnamemat)
    cmd = "INSERT INTO " + qnnaire + " "+str(tuple(hnamemat))+" VALUES ("
    for q in range(n):
        cmd += "?,"
    cmd=cmd[:len(cmd)-1]
    cmd += ");"
    print(cmd)
    pointer.execute(cmd, tuple(answers))
    userdb.commit()


def pull_data(qnnaire):
    rows = []
    cmd = "SELECT * from " + qnnaire + ";"
    for entry in pointer.execute(cmd):
        rows.append(entry[1:])
    return rows


def pull_sorted_data(qnnaire, colidx, ascending):
    rows = []
    cmd = "SELECT * from " + qnnaire
    if len(colidx) > 0:
        cmd += " ORDER BY"
        for i in range(len(ascending)):
            cmd += " q" + str(colidx[i]) + " "
            if ascending[i]:
                cmd += "ASC,"
            else:
                cmd += "DESC,"
        cmd=cmd[:len(cmd)-1]
    cmd += ";"
    for entry in pointer.execute(cmd):
        rows.append(entry[1:])
    return rows



