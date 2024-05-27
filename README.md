## Project Title
*News Aggregator and Distribution Server*

### Project Description
This project involves the development of a multi-threaded server application that aggregates news from various sources using the News API and distributes the fetched news data to connected clients upon request. The server listens for incoming client connections on a specified host and port, managing each client connection in a separate thread to handle multiple clients simultaneously

### Semester
2nd

### users name
ITNE352-B1 : is Nouf Bureshaid
Amna Hesham : is Amna Hesham

### Group 
Group B1
ITNE352
Section 2
Nouf Bureshaid - 202109273
Amna Hesham - 202107285

### Table of Contents

### Requirements
1. User need to install python
2. Local envioronment is required to run this application steps to which are provided in How to section

### How to

1. Create a virtual environment if not available - `python -m venv venv`
2. Activate the virtual environment - `.\venv\Scripts\activate`
3. Install all dependencies - `pip install requests`
4. Now run your server - `python server.py`
5. Now open another terminal and run - `python client.py`
   
All Set! app is running now

### The scripts
#### A. `client.py` - this script have the code for all the functionalities at client side
The client script is designed to interact with a news service server. The main functionalities of the client include searching for news headlines and listing news sources based on various criteria. The script utilizes the 'socket' and 'json' packages to communicate with the server and handle JSON data,respectively.
Main Functionalities
1-Connecting to the Server:
The client connects to a server using a TCP socket.
It sends the client's name to the server upon connection.
2-Main Menu:
The script presents a main menu with options to search headlines, list sources, or quit the application.
3-Search Headlines Menu:
Allows the user to search for news by keywords, category, or country.
Provides an option to list all new headlines.
4-Receive Sources Menu:
Allows the user to list news sources by category, country, or language.
Provides an option to list all available sources.
5-Request and Response Handling:
The 'mainrequest' function sends a request to the server and receives a response.
The response length is received first, followed by the actual data.
6-Display Functions:
'display_items' shows the list of news articles and their details upon selection.
'receive_and_print' lists the news sources based on the criteria selected. 7-Main Execution Block: will manages the main application flow by Prompts the user to enter their name and sends it to the server/ Displays the main menu Based on user input, it calls search_headlines_menu or receive_sources/ or exits the application.

#### B. `server.py` - this file represents the server configuration and settings
socket: For creating network connections.
threading: For handling multiple client connections simultaneously.
requests: For making HTTP requests to the NewsAPI.
json: For parsing JSON data.
os: For interacting with the operating system                                                                                                                                                                          NEWS_API_KEY: The API key for accessing NewsAPI.
BASE_URL: The base URL for the NewsAPI.
HOST: The IP address where the server will listen for connections.
PORT: The port number on which the server will listen.                                                                                                                                                           get_allnews: This function fetches news data from the NewsAPI by :
Adds the API key to the parameters.
Makes a GET request to the specified endpoint with the given parameters.
Returns the JSON response if successful or an error message if not.                                                                                                                                     Save_userlog: This function saves user activity logs to a JSON file by 
Creates a filename based on the group ID, client name, and the requested option.
Writes the data to this file in JSON format.
Chandel: This function handles client connections by:
Receives the client's name.
Processes requests in a loop until the client disconnects.
Handles get_news requests by calling get_allnews and sending the response back to the client.
Logs the request and response.                                                                                                                                                                                                main:  This is the entry point of the server:
Creates a socket and binds it to the specified host and port.
Listens for incoming connections.
Accepts connections and spawns a new thread for each client using Chandel to handle the client's requests.  
Handles invalid requests by sending an error response.
Closes the connection when done.
### Acknowledgments
We want to thank our professor Dr. Mohammed Almeer for his continuing support during this project and available documentations online regarding this project

### Conclusion
In conclusion, these codes establish a basic client-server news retrieval system. Users can request news based on keywords, categories, or countries, and the server responds with the relevant information. Although the current setup functions adequately, there's room for improvement. Enhancements like error handling and user authentication would strengthen the system's reliability and security. Moreover, introducing features such as personalized recommendations could enhance the user experience, making the system more appealing and user-friendly. Overall, while these codes lay a solid foundation, they could be further refined to create a more robust and feature-rich news retrieval system.
