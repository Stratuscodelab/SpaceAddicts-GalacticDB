

                                                                                                                     
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

space_addicts_banner = pyfiglet.figlet_format("\nSPACE ADDICTS", font="colossal", width=columns)
print(space_addicts_banner)

#Welcome message and disclaimer

print("--=-=-=-= Welcome to Asteroid City Record Database -=-=-=-=-=\n")
# Pause for 2 seconds
time.sleep(2)

# connect to an existing database file
conn = sqlite3.connect('sa23.db')

# create a cursor object to execute SQL commands
c = conn.cursor()

while True:
    # perform a lookup based on name
    name = input("Enter name of suspect: ")
    name = name.lower() # convert to lowercase
    c.execute("SELECT * FROM people WHERE LOWER(name)=?", (name,))
    result = c.fetchone()

    if result:
        print("\n>>Subject: ", end='', flush=True)
        for char in result[0]:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print("\n")
        time.sleep(2)
        print(">>Occupation: ", end='', flush=True)
        for char in result[1]:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print("\n")
        time.sleep(2)
        print(">>Description: ", end='', flush=True)
        for char in result[2]:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print("\n")
    else:
        print(f"\nNo record found for {name}\n")

    # ask if the user wants to perform another lookup
    again = input("Perform another lookup? (y/n): ")
    if again.lower() != 'y':
        break

# close the cursor and database connection
c.close()
conn.close()
