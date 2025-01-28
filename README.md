# DuoPlay Server

## Description
DuoPlay Server connects a server with two clients, allowing them to play a simple multiplayer game. The server handles communication and synchronizes game states between the clients, demonstrating basic client-server interaction in a gaming context.

## Project Overview
This project illustrates how socket programming works by creating a multiplayer game where two players can connect to the same server over a local Wi-Fi network. The game ends if the boxes controlled by the players overlap during gameplay. The project demonstrates how a server manages connections, synchronizes game states, and facilitates real-time communication between clients.

## Features
- Two-player multiplayer gameplay.
- Server-client architecture using socket programming.
- Real-time synchronization of game states between clients.
- Game ends when player-controlled boxes overlap.
- Works over the same Wi-Fi network for local multiplayer sessions.

## Technologies Used
- **Programming Language:** Python
- **Networking:** Socket programming

## How It Works
1. **Server Setup:**
   - A server is created to listen for incoming connections from clients.
   - It manages communication between the two clients and synchronizes their game states.

2. **Client Connection:**
   - Two clients connect to the server using the same Wi-Fi network.
   - Once connected, they can start playing the game.

3. **Game Mechanics:**
   - Players control boxes in the game environment.
   - The server monitors the game state and checks for overlap between the boxes.
   - If the boxes overlap, the server notifies the clients, and the game ends.

## Prerequisites
- Python installed on the server and client machines.
- All devices connected to the same Wi-Fi network.

## Use Cases
- **Educational:** Demonstrates the fundamentals of socket programming and client-server architecture.
- **Gaming:** Provides a basic example of multiplayer game mechanics.
- **Networking:** Illustrates real-time communication and data exchange between multiple clients.

## Future Enhancements
- Add more complex game mechanics.
- Enable cross-network connections.
- Improve graphical user interface (GUI) for better gameplay experience.
- Implement a scoring system and leaderboard.

## Conclusion
DuoPlay Server is a simple yet effective example of socket programming and client-server interaction. It provides a foundation for understanding how multiplayer games can be developed and how real-time communication is managed in a networked environment.

