# Behind Discord: Building a Real-Time Chat Server with WebSockets

## Why I Built This

Whenever we send a message on Discord, Slack, WhatsApp Web, or any real-time application, the message appears instantly for everyone connected.

For a long time, I used these applications without understanding what was happening behind the scenes.

This week, I decided to explore:

* How real-time communication actually works
* Why WebSockets exist
* How multiple users stay connected simultaneously
* How Python handles asynchronous networking

This project is the result of that exploration.

---

## What I Learned

### WebSockets

Unlike traditional HTTP requests, WebSockets create a persistent connection between a client and a server.

Instead of repeatedly asking:

> "Do you have new messages?"

the connection remains open and the server can instantly send updates whenever something changes.

This is one of the key technologies behind:

* Discord
* Slack
* WhatsApp Web
* Online multiplayer games
* Live dashboards
* Stock market applications

---

### Async Programming

While building this project, I worked with:

* `async`
* `await`
* asynchronous event loops
* concurrent message handling

This helped me understand how a single server can manage multiple connected users without blocking execution.

---

### Data Structures Still Matter

One interesting realization was that even in networking applications, basic data structures remain important.

For example:

* Lists were used to maintain active client connections.
* Iteration was used to broadcast messages to every connected client.
* State management depended on organizing connected users efficiently.

Sometimes the most important concepts are still the fundamentals.

---

## Features

* Real-time communication using WebSockets
* Multiple client support
* Message broadcasting
* Connection management
* Async client-server architecture
* Terminal-based chat interface

---

## Tech Stack

* Python
* Asyncio
* WebSockets

---

## Project Structure

```text
server.py
main.py
```

### Server

Responsible for:

* Managing active connections
* Receiving messages
* Broadcasting messages
* Handling client disconnects

### Client

Responsible for:

* Sending messages
* Receiving messages concurrently
* Maintaining a live connection with the server

---

## Future Improvements

* Usernames
* Chat rooms
* Private messaging
* SQLite message persistence
* Authentication
* Web interface

---

## Key Takeaway

This project was less about building a chat application and more about understanding the foundations of real-time systems.

The next time I use Discord or Slack, I'll have a much better appreciation for what is happening underneath the UI.
