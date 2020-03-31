// Main Entry Point of Node Server

// Server Setting
const FPS40 = Number(1000 / 40);
const FPS20 = Number(1000 / 20);
const FPS10 = Number(1000 / 10);

const MAXCONNECTION = 30

// Controller
class Controller {
  constructor(io) {
    // Register Socket io object
    this.io = io;

    // Connected Client
    this.clientList = new ClientList(MAXCONNECTION)
  }

  // Main Loop For Logic Processing
  main() {
    
  }

  // Add Client
  addClient(socket) {
    let isSuccess = this.clientList.add(socket);

    if(isSuccess) console.log(`Socket ${socket.id} has join the room!!`);
    else console.log(`Socket Join Failed.`)
  }

  // Remove Client
  removeClient(socket) {
    this.clientList.remove(socket)

    console.log(`Socket ${socket.id} has removed from client list.`)
  }
}

// Client
class Client {
  constructor(idx) {
    // Default Value
    this.socketId = null;
    this.idx = idx;
    this.isOccupied = false
  }

  occupy(socket) {
    this.socketId = socket.id;
    this.isOccupied = true;
  }

  release() {
    this.socketId = null;
    this.isOccupied = false;
  }
}

// Client List
class ClientList {
  constructor(maxConnection) {
    // Setting
    this.maxConnection = maxConnection;
    this.pool = [];
    this.firstNotOccupied = 0;

    // Init Pool
    for(let i = 0; i < this.maxConnection; i++) this.pool.push(new Client(i))
  }

  add(socket) {
    // Check if the list have ability to adapte new user
    if (this.firstNotOccupied >= this.maxConnection) {
      return false;
    }

    // Add new user to list
    this.pool[this.firstNotOccupied].occupy(socket);

    // Update next empty space
    for(let i = this.firstNotOccupied + 1; i < this.maxConnection; i++) {
      if (!this.pool[i].isOccupied) {
        this.firstNotOccupied = i;
        return true;
      }
    }
  }

  remove(socket) {
    for(let i = 0; i < this.maxConnection; i++) {
      if(this.pool[i].socketId === socket.id) {
        // Release usage
        this.pool[i].release()

        // update first empty space if its index is smaller than previous one.
        if(i < this.firstNotOccupied) this.firstNotOccupied = i;
      }
    }
  }
}

// Socket IO Object
var io = require("socket.io")(8080);

console.log("Listnening to http://localhost:8080");

// Init Controller
var controller = new Controller(io);

// On Connection
io.on("connection", (socket) => {
  controller.addClient(socket)

  socket.on("disconnect", (_) => {
    controller.removeClient(socket)
  })
})

