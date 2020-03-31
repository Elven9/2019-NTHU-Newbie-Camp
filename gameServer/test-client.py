import socketio

# Create Client
client = socketio.Client()

# On Connect To Server
@client.event
def connect():
    print("Connected to server...")

# Connect to server
client.connect("http://localhost:8080")
