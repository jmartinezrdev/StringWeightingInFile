import socket
import logging

def start_client(string_quantity = 1000000):
    logging.basicConfig(filename='client.log', level=logging.INFO)
    server_address = ('localhost', 8888)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    logging.info("Connected to server.")

    
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