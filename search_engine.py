import psycopg2
import csv

conn = psycopg2.connect("dbname=players user=Artyom")

cur = conn.cursor()

cur.execute("CREATE TABLE IF not EXISTS players (player_id serial PRIMARY KEY, name varchar(50), position varchar(30), jersey_number integer, club varchar(50), age integer, country varchar(50), captain boolean);")

with open('players.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        cur.execute("INSERT INTO players (name, position, jersey_number, club, age, country, captain) VALUES (%s, %s, %s, %s, %s, %s, %s)", (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


def sport_engine():
    while True:
        print("To insert new player type [i]")
        print("To update player's info type [u]")
        print("To delete player type [d]")
        print("To select players type [s]")
        print("To exit type [x]")
        choice = input("Choose what you wish to do: ")

        if choice == "i":
            cur.execute("INSERT INTO players (name, position, jersey_number, club, age, country, captain) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (input('Enter name: '), input('Enter position: '), input('Enter jersey number: '), input('Enter club: '),
            input('Enter age: '), input('Enter country: '), input('Enter if player is a captain: ')))

        elif choice == "d":
            cur.execute("DELETE FROM players WHERE name = %s",
            (input('choose name to delete: '),))

        elif choice == "u":
            cur.execute("UPDATE players SET height=(%s) WHERE name = (%s)", (input('Enter new height: '), input('Enter name: ')))

        elif choice == "s":
            print("To search by name type [n]")
            print("To search by position [p]")
            print("To search by jersey number [j]")
            print("To search if player is a caprain type [c]")
            print("To search for a team type [t]")
            #print("To exit type [x]")
            pick = input("Choose from the above: ")
            if pick == "n":
                cur.execute("SELECT * FROM players WHERE name = %s", (input('Type the player\'s name: '),))
                results = cur.fetchall()
                # conn.commit()
                print(*results, sep = "\n")
            elif pick == "p":
                cur.execute("SELECT * FROM players WHERE position = %s", (input('Type the player\'s position: '),))
                results = cur.fetchall()
                # conn.commit()
                print(*results, sep = "\n")
            elif pick == "j":
                cur.execute("SELECT * FROM players WHERE jersey_number = %s", (input('Type the player\'s number: '),))
                results = cur.fetchall()
                # conn.commit()
                print(*results, sep = "\n")
            elif pick == "c":
                cur.execute("SELECT * FROM players WHERE captain = %s", (input('Type True/False if you are looking for captains: '),))
                results = cur.fetchall()
                # conn.commit()
                print(*results, sep = "\n")
            elif pick == "t":
                cur.execute("SELECT * FROM players WHERE club = %s", (input('Type the club you\'re looking for: '),))
                results = cur.fetchall()
                # conn.commit()
                print(*results, sep = "\n")
            # print(type(results[1]))

        elif choice == "x":
            break
        # else:
        #     pass
        conn.commit()

sport_engine()
#
# cur.execute("SELECT * FROM players;")
#cur.fetchall()
conn.commit()


cur.close()
conn.close()
