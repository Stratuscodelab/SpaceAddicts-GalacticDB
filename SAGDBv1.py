

                                                                                                                     
#@@@@@@   @@@@@@@    @@@@@@    @@@@@@@  @@@@@@@@      @@@@@@   @@@@@@@   @@@@@@@   @@@   @@@@@@@  @@@@@@@   @@@@@@   
#@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@   
#!@@       @@!  @@@  @@!  @@@  !@@       @@!          @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@         @@!    !@@       
#!@!       !@!  @!@  !@!  @!@  !@!       !@!          !@!  @!@  !@!  @!@  !@!  @!@  !@!  !@!         !@!    !@!       
#!!@@!!    @!@@!@!   @!@!@!@!  !@!       @!!!:!       @!@!@!@!  @!@  !@!  @!@  !@!  !!@  !@!         @!!    !!@@!!    
# !!@!!!   !!@!!!    !!!@!!!!  !!!       !!!!!:       !!!@!!!!  !@!  !!!  !@!  !!!  !!!  !!!         !!!     !!@!!!   
#     !:!  !!:       !!:  !!!  :!!       !!:          !!:  !!!  !!:  !!!  !!:  !!!  !!:  :!!         !!:         !:!  
#    !:!   :!:       :!:  !:!  :!:       :!:          :!:  !:!  :!:  !:!  :!:  !:!  :!:  :!:         :!:        !:!   
#:::: ::    ::       ::   :::   ::: :::   :: ::::     ::   :::   :::: ::   :::: ::   ::   ::: :::     ::    :::: ::   
#:: : :     :         :   : :   :: :: :  : :: ::       :   : :  :: :  :   :: :  :   :     :: :: :     :     :: : :    
# =-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- @Arm_710 -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-   2023   -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  


import sqlite3
import pyfiglet
import shutil
import time

# Get the width of the console
columns, _ = shutil.get_terminal_size()

space_addicts_banner = pyfiglet.figlet_format("\n>>SPACE ADDICTS<<", font="colossal", width=columns)
galactic_database_banner = pyfiglet.figlet_format("-=-=-=-= Galactic Database=-=-=-=-", font="rowancap", width=columns)
disclaimer = ("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Disclaimer=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Welcome, intrepid space traveler! 
This database contains records of the most notorious space criminals, smugglers, and other shady characters in the galaxy.
But be warned, using this database for anything other than lawful purposes is strictly prohibited, and may result in a run-in with the Asteroid City Law.
The creators of this database assume no responsibility for any misuse of the information contained herein. Use at your own risk!.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""")
print(space_addicts_banner + galactic_database_banner + disclaimer)


# connect to an existing database file
conn = sqlite3.connect('sa24.db')

# create a cursor object to execute SQL commands
c = conn.cursor()

while True:
    print("\n\n--=-=-=-= Menu -=-=-=-=-=")
    print("1. Find a random record")
    print("2. Look up a name")
    print("3. List all character names")
    print("4. Clear screen")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # find a random record
        c.execute("SELECT * FROM people ORDER BY RANDOM() LIMIT 1")
        result = c.fetchone()
        if result:
            print("\n>>Subject: ", end='', flush=True)
            for char in result[0]:
                print(char, end='', flush=True)
                time.sleep(0.02)
            print("\n")
            time.sleep(2)
            print(">>Occupation: ", end='', flush=True)
            for char in result[1]:
                print(char, end='', flush=True)
                time.sleep(0.02)
            print("\n")
            time.sleep(2)
            print(">>Profile:\n")
            desc = result[2].strip().split('.')
            for sentence in desc:
                print("   ", end='', flush=True)
                for char in sentence:
                    print(char, end='', flush=True)
                    time.sleep(0.02)
                print('.')
                time.sleep(0.5)
            print("\n")
        else:
            print("\nNo records found!\n")

    elif choice == "2":
    # look up a name
        name = input("\nEnter name of suspect: ")
        name = name.lower() # convert to lowercase
        c.execute("SELECT * FROM people WHERE LOWER(name)=?", (name,))
        result = c.fetchone()

        if result:
            print("\n>>Subject: ", end='', flush=True)
            for char in result[0]:
                print(char, end='', flush=True)
                time.sleep(0.02)
            print("\n")
            time.sleep(2)
            print(">>Occupation: ", end='', flush=True)
            for char in result[1]:
                print(char, end='', flush=True)
                time.sleep(0.02)
            print("\n")
            time.sleep(2)
            print(">>Profile:\n")
            desc = result[2].strip().split('.')
            for sentence in desc:
                print('   ', end='', flush=True)
                for desc_char in sentence:
                    print(desc_char, end='', flush=True)
                    time.sleep(0.02)
                print('.')
                time.sleep(0.02)
            print("\n")
        
    elif choice == "3":
        # list all character names
        print("\n>>List of all character names<<\n")
        c.execute("SELECT name, occupation, profile FROM people")
        results = c.fetchall()
        if results:
            # Find the maximum length for each column
            max_name_len = max(len(result[0]) for result in results)
            max_occ_len = max(len(result[1]) for result in results)
            max_desc_len = max(len(result[2]) for result in results)

            # Print the table header
            print(f"+{'-' * (max_name_len + 2)}+{'-' * (max_occ_len + 2)}+{'-' * (max_desc_len + 2)}+")
            print(f"| {'Name'.ljust(max_name_len)} | {'Occupation'.ljust(max_occ_len)} | {'Description'.ljust(max_desc_len)} |")
            print(f"+{'-' * (max_name_len + 2)}+{'-' * (max_occ_len + 2)}+{'-' * (max_desc_len + 2)}+")

            # Print the table rows
            for result in results:
                name = result[0].ljust(max_name_len)
                occupation = result[1].ljust(max_occ_len)
                description = result[2].ljust(max_desc_len)
                print(f"| {name} | {occupation} | {description} |")

            # Print the table footer
            print(f"+{'-' * (max_name_len + 2)}+{'-' * (max_occ_len + 2)}+{'-' * (max_desc_len + 2)}+")
            print("\n")
        else:
            print("\nNo records found!\n")


    elif choice == "4":
        # clear the screen
            print("\033c", end="")
            print(space_addicts_banner + disclaimer)


    elif choice == "5":
        print("\n>>Shutdown Signal sent<<")
        print("\n**Good Bye**")
        print("\n>>Connection Terminated<<")
        break

    else:
        print("\nInvalid choice. Please try again.\n")


