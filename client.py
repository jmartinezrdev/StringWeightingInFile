import socket
import logging
import string
import random
import time

def generate_random_strings():
    """
    This function generates a random string of characters and spaces,
     where the length of the string, the number of spaces and the positions
      of the spaces are generated randomly.
    
    """
    length = random.randint(50, 100)
    num_spaces = random.randint(3, 5)
    spaces_indices = random.sample(range(1, length - 1), num_spaces)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    for index in spaces_indices:
        random_string = random_string[:index] + ' ' + random_string[index:]
    return random_string

def start_client(string_quantity = 1000000):
    """
    This function starts a client that connects to a server and sends 
    a specified number of strings to the server for processing. 
    In addition, the log events are recorded in a file called "client.log".
     
    """
    logging.basicConfig(filename='client.log', level=logging.INFO)
    server_address = ('localhost', 8888)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    logging.info("Connected to server.")

    with open('chains.txt', 'w') as f:
        for _ in range(string_quantity):
            string_obtained = generate_random_strings()
            f.write(string_obtained + '\n')
            client_socket.send(string_obtained.encode())
            response = client_socket.recv(1024).decode()
            logging.info(f"String: {string_obtained.strip()}, Weight: {response}")

    
    logging.info(f"Process completed in seconds.")
    
    client_socket.close()
    print("Process completed.")


def menu():
    while True:
        print("======= MENU =======")
        print("1. Start process")
        print("2. Exit")
        option = input("Select an option: ")

        if option == "1":
            while True:
                generated_option = input("You want to define the number of strings to generate? (y/n): ")
                if generated_option.lower() == "y":
                    string_quantity = input("Please, define the quantity: ")
                    try:
                        string_quantity = int(string_quantity)
                        # start_client(string_quantity)
                        break
                    except ValueError:
                        print("Error: You must enter a valid number.")
                elif generated_option.lower() == "n":
                    # One million strings will be executed by default.
                    # start_client()
                    break
                else:
                    print("Error: Invalid option.")
        elif option == "2":
            print("Closing...")
            break
        else:
            print("Error: Invalid option.")


if __name__ == "__main__":
    menu()