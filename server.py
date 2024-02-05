import logging
import socket

def calculate_metric(string):
    count_letters = 0
    count_numbers = 0
    count_spaces = 0
    metrics = 0

    for character in string:
        """
        If the character is a letter, digit or space the corresponding counter
         will be incremented.
        """
        if character.isalpha():
            count_letters += 1
        elif character.isdigit():
            count_numbers += 1
        elif character.isspace():
            count_spaces += 1
    # The metric is calculated
    try:
        metrics = (count_letters * 1.5 + count_numbers * 2) / count_spaces
    except Exception as error:
        logging.warning(error)

    return metrics

def start_server():
    logging.basicConfig(filename='server.log', level=logging.INFO)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 8888
    server_socket.bind((host, port))
    logging.info("Server started. Listening on port " + str(port) + "...")

if __name__ == "__main__":
    start_server()
