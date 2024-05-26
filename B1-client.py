import socket
import json
def mainrequest(SocketC, request):
    SocketC.send(request.encode('utf-8'))
    response_length_str = SocketC.recv(10).decode('utf-8').strip()
    print(f"Received response length string: '{response_length_str}'")
    response_length = int(response_length_str)
    print(f"Received response length: {response_length}")
    response_data = b""
    while len(response_data) < response_length:
        part = SocketC.recv(response_length - len(response_data))
        response_data += part

    return json.loads(response_data.decode('utf-8'))

def search_headlines_menu(SocketC):
    while True:
        print("Search headlines menu:")
        print("1. Search for keywords")
        print("2. Search by category")
        print("3. Search by country")
        print("4. List all new headlines")
        print("5. Back to the main menu")
        option = input("Select an option: ")

        if option == '1':
            keyword = input("Enter keyword: ")
            params = {'q': keyword}
            news_data = mainrequest(SocketC, f'get_news|everything|{json.dumps(params)}')
            display_items(news_data)
        elif option == '2':