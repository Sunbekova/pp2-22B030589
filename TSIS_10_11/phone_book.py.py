import psycopg2
import csv

conn = psycopg2.connect(
    host = "localhost"
    , dbname = 'postgres'
    , user = 'postgres'
    , password = ''
    , port = 5432
)

conn.autocommit = True
cur = conn.cursor()




#create Table:
cur.execute(
    """CREATE TABLE IF NOT EXISTS contacts (
    name VARCHAR(50)
    , mobile VARCHAR(50)
    );
""")

#print(f'Table created')

# Implement two ways of inserting data into the PhoneBook.
out = "yes"
while True:
    print("Insert (csv) file? yes or no")
    out = input()
    if out == "no":
        break
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO contacts VALUES (%s,%s)", row)
    break


while True:
        options = input("Select one of the options: Create (C)\n Read_person (RP)\n Read (R)\n Update (U)\n Delete (D)\n Quit (Q)\n")

        if options.lower() == 'c':
            name = input("Enter name: ")
            mobile = input("Enter phone number: ")
            cur.execute(f'''INSERT INTO contacts (name, mobile) VALUES ('{name}', '{mobile}'); ''')
            print("New record added!")

        elif  options.lower() == 'rp':
            name = input("Enter a name: ")
            cur.execute(f"""SELECT * FROM contacts WHERE name = '{name}'; """)
            print(cur.fetchone())

        elif options.lower() == 'r':
            cur.execute("""SELECT * FROM contacts""")
            for row in cur.fetchall():
             print(row)
            

        elif options.lower() == "u":
            print("For update number - print num\n For update name - print name\n")
            ans = input()
            if ans == 'num':
                name = input("Enter name to change num: ")
                mobile = input("Input new data: ")
                cur.execute(f'''UPDATE contacts SET mobile = '{mobile}' WHERE name = '{name}'; ''')
                print("Changed!")
            elif ans == "name":
                mobile = input("Enter a num to change name: ")
                name = input("Input new data: ")
                cur.execute(f'''UPDATE contacts SET name = '{name}' WHERE mobile = '{mobile}'; ''')
                print("Changed!")
            else: print("No options!")

        elif options.lower() == "d":
            name = input("Enter person to delete: ")
            cur.execute(f"""DELETE FROM contacts WHERE name='{name}';""")
            print(f"{name} was Deleted")

        elif options.lower() == "q":
            print("Bye Bye")
            quit()

        else:
            print(f"No option {options} available!")


