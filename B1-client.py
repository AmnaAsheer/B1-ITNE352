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
            category = input("Enter category (e.g., business, entertainment, general, health, science, sports, technology): ")
            params = {'category': category}
            news_data = mainrequest(SocketC, f'get_news|top-headlines|{json.dumps(params)}')
            display_items(news_data)
        elif option == '3':
            country = input("Enter country code (e.g., us, in): ")
            params = {'country': country}
            news_data = mainrequest(SocketC, f'get_news|top-headlines|{json.dumps(params)}')
            display_items(news_data)
        elif option == '4':
            news_data = mainrequest(SocketC, 'get_news|top-headlines|{}')
            display_items(news_data)
        elif option == '5':
            break
        else:
            print("Invalid input. Please enter again.")
            
def receive_sources(SocketC):
    while True:
        print("List of sources menu:")
        print("1. Search by category")
        print("2. Search by country")
        print("3. Search by language")
        print("4. List all")
        print("5. Back to the main menu")
        option = input("Select an option: ")

        if option == '1':
            category = input("Enter category (e.g., business, entertainment, general, health, science, sports, technology): ")
            params = {'category': category}
            sources_data = mainrequest(SocketC, f'get_news|sources|{json.dumps(params)}')
            receive_and_print(sources_data)
        elif option == '2':
            country = input("Enter country code (e.g., au, nz, ca, ae, sa, gb, us, eg, ma): ")
            params = {'country': country}
            sources_data = mainrequest(SocketC, f'get_news|sources|{json.dumps(params)}')
            receive_and_print(sources_data)