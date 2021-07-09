import mysql.connector
from mysql.connector import errorcode;
def main():
    config = {
        "user" : "pysports_user",
        "password" : "3512fred",
        "host" : "127.0.0.1",
        "database" : "pysports",
        "raise_on_warnings" : True
        }
    try:
        db = mysql.connector.connect(**config)
        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
        cursor=db.cursor()
        cursor.execute("insert into player (first_name, last_name, team_id) values('Smeagol','Shire Folk',1);")
        
        cursor=db.cursor()
        cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id=team.team_id;")
        infos=cursor.fetchall()
        print("-- DISPLAYING RECORDS AFTER INSERT --")
        for info in infos:
            print("Player ID: {}".format(info[0]))
            print("First Name: {}".format(info[1]))
            print("Lastt Name: {}".format(info[2]))
            print("Team Name: {}".format(info[3]))
            print()
        print()
        cursor=db.cursor()
        cursor.execute("update player set team_id=2, first_name='Gollum', last_name ='Ring Stealer' where first_name='Smeagol';")
        cursor=db.cursor()
        cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id=team.team_id;")
        infos=cursor.fetchall()
        print("-- DISPLAYING RECORDS AFTER UPDATE --")
        for info in infos:
            print("Player ID: {}".format(info[0]))
            print("First Name: {}".format(info[1]))
            print("Lastt Name: {}".format(info[2]))
            print("Team Name: {}".format(info[3]))
            print()
        print()
        cursor=db.cursor()
        cursor.execute("delete from player where first_name = 'Gollum';")
        cursor=db.cursor()
        cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id=team.team_id;")
        infos=cursor.fetchall()
        print("-- DISPLAYING RECORDS AFTER DELETE --")
        for info in infos:
            print("Player ID: {}".format(info[0]))
            print("First Name: {}".format(info[1]))
            print("Lastt Name: {}".format(info[2]))
            print("Team Name: {}".format(info[3]))
            print()
        print()
        print("Press any key to continue...")#faked to the end
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")
        else:
            print(err)
    finally:
        db.close()
main()
