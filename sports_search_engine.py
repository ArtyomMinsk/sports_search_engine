import psycopg2
import csv

conn = psycopg2.connect("dbname=players3 user=Artyom")

cur = conn.cursor()

#def read_file():
try:
    cur.execute("CREATE TABLE  players3 (player_id serial PRIMARY KEY, name varchar(50), position varchar(30), jersey_number integer, club varchar(50), age integer, country varchar(50), captain boolean);")
    with open('players.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            cur.execute("INSERT INTO players3 (name, position, jersey_number, club, age, country, captain) VALUES (%s, %s, %s, %s, %s, %s, %s)", (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    conn.commit()
except psycopg2.ProgrammingError:
    conn.rollback()


def insert_into_database():
    cur.execute("INSERT INTO players3 (name, position, jersey_number, club, age, country, captain) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    (input('Enter name: '), input('Enter position: '), input('Enter jersey number: '), input('Enter club: '),
    input('Enter age: '), input('Enter country: '), input('Enter if player is a captain: ')))
    cur.execute("SELECT * FROM players3;")
    cur.fetchone()
    conn.commit()

def update_database():
    print("To update position type [p]")
    print("To update jersey number type [j]")
    print("To update team type [t]")
    print("To update age type [a]")
    #print("To exit type [x]")
    pick = input("Choose from the above: ")
    if pick == "p":
        cur.execute("UPDATE players3 SET position = %s WHERE name = %s", (input('Update position: '), input('Enter name: ')))

    elif pick == "j":
        cur.execute("UPDATE players3 SET jersey_number = %s WHERE name = %s", (input('Update player\'s number: '), input('Enter name: ')))

    elif pick == "t":
        cur.execute("UPDATE players3 SET club = %s WHERE name = %s", (input('Update club: '), input('Enter name: ')))

    elif pick == "a":
        cur.execute("UPDATE players3 SET age = %s WHERE name = %s", (input('Update player\'s age: '), input('Enter name: ')))


def delete_from_database():
    cur.execute("DELETE FROM players3 WHERE name = %s", (input('Choose player to delete: '),))


def select_from_database():
    print("To search by name type [n]")
    print("To search by position type [p]")
    print("To search by jersey number type [j]")
    print("To search if player is a caprain type [c]")
    print("To search for a team type [t]")
    #print("To exit type [x]")
    pick = input("Choose from the above: ")
    if pick == "n":
        cur.execute("SELECT * FROM players3 WHERE name ILIKE %s", ("%" + input('Type the player\'s name: ') + "%",))
        results = cur.fetchall()
        # conn.commit()
        print(*results, sep = "\n")

    elif pick == "p":
        cur.execute("SELECT * FROM players3 WHERE position ILIKE %s", ("%" + input('Type the player\'s position: ') + "%",))
        results = cur.fetchall()
        # conn.commit()
        print(*results, sep = "\n")

    elif pick == "j":
        cur.execute("SELECT * FROM players3 WHERE jersey_number = %s", (input('Type the player\'s number: '),))
        results = cur.fetchall()
        # conn.commit()
        print(*results, sep = "\n")

    elif pick == "c":
        cur.execute("SELECT * FROM players3 WHERE captain = %s", ("%" + input('Type True/False if you are looking for captains: ') + "%",))
        results = cur.fetchall()
        # conn.commit()
        print(*results, sep = "\n")

    elif pick == "t":
        cur.execute("SELECT * FROM players3 WHERE club = %s", ("%" + input('Type the club you\'re looking for: ') + "%",))
        results = cur.fetchall()
        # conn.commit()
        print(*results, sep = "\n")
    # print(type(results[1]))


def main():
    #read_file()
    print("\nWelcome to the Sports Search Engine of players in the English Premier League!\n")

    while True:
        print("To insert new player type [i]")
        print("To update player's info type [u]")
        print("To delete player type [d]")
        print("To select players type [s]")
        print("To exit type [x]")
        choice = input("Choose what you wish to do: ")

        if choice == "i":
            insert_into_database()

        elif choice == "d":
            delete_from_database()

        elif choice == "u":
            update_database()

        elif choice == "s":
            select_from_database()

        elif choice == "x":
            print("Have a great day!")
            break
        # else:
        #     pass
        conn.commit()

#main()

#cur.execute("SELECT * FROM players3;")
#cur.fetchall()


if __name__ == '__main__':
    main()

#conn.commit()
cur.close()
conn.close()
