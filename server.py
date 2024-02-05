import logging
import socket

def calculate_metric(string):
    """
    This function returns the weight metric of a string.

    :param string: String to calculate its metric.
    :return: The value obtained from the metric calculation.
    :rtype: float
    """      
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


def process_string(cadena):
    """
    This function processes a string under established rules.

    :param string: String to parse.  
    :return: The value obtained from the metric calculation.
    :rtype: float
    """

    """ Converts all characters in the string to lowercase, thus simplifying
      the analysis of any of these variants (aa, AA, aA, Aa) """
    if 'aa' in cadena.lower():
        # If the rule is detected, the metric value of the string will be 1000
        logging.warning(f"Double 'a' rule detected >> '{cadena}'")
        return 1000
    else:
        # Otherwise, the chain metric is calculated
        return calculate_metric(cadena)


def manage_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        string = data.decode().strip()
        weight = process_string(string)
        client_socket.send(str(weight).encode())
    client_socket.close()


def start_server():
    """
    This function starts a basic TCP server that listens on a preconfigured
    port and manages client connections using the manage_client() function.
    It also logs events using the logging module and stores them in a
    file called "server.log"

    """
    logging.basicConfig(filename='server.log', level=logging.INFO)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 8888
    server_socket.bind((host, port))
    server_socket.listen(5)
    logging.info("Server started. Listening on port " + str(port) + "...")
    while True:
        client_socket, _ = server_socket.accept()
        logging.info("Client connected.")
        manage_client(client_socket)


if __name__ == "__main__":
    start_server()
