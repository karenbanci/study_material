/**
 *
 * Example input:

Lobby 0 Enter -
Hallway1 10 Enter
Room1 30 Enter
Room1 40 Exit // back in hall way1 now
Room1 50 Enter
Room1 60 Exit
Hallway1 90 Exit // back in Lobby
Hallway2 100 Enter
Hallway2 150 Exit
Lobby 160 Exit

Output:
map(Lobby = 30, Hallway1 = 60, Room1 = 20, Hallway2 = 50)

---------

Different Unique Simpler example:
Lobby 0 Enter
Hallway1 10 Enter
Hallway1 20 exit // back in Lobby
Room1 30 Enter
Room1 45 Exit
Lobby 50 exit

Input: log = [
  0:{room: Lobby, time: 0, action:enter},    - rooms_entered=[0]
  1:{room: Hallway1, time: 10, action:enter},- rooms_entered=[0,1] time_per_room = {Lobby:10}
  2:{room: Hallway1, time: 20, action:exit}, - rooms_entered=[0] time_per_room = {Lobby:10,Hallway1:10}
  3:{room: Room1, time: 30, action:enter}, - rooms_entered=[0,3] time_per_room = {Lobby:20,Hallway1:10}
  4:{room: Room1, time: 45, action:exit}, - rooms_entered=[0] time_per_room = {Lobby:20,Hallway1:10, Room1:15}
  5:{room: Lobby, time: 50, action:exit}, - rooms_entered=[] time_per_room = {Lobby:25,Hallway1:10, Room1:15}
]

Output:
map(Lobby = 25, Hallway1 = 10, Room1 = 15)

*/

function timer(log) {
  const time_per_room = {};
  const rooms_entered = [];

  for (let i = 0; i < log.length; i++) {
    const log_entry = log[i];
    const peek = rooms_entered[rooms_entered.length - 1];

    if (rooms_entered.length) {
      const diff_time = log_entry.time - log[i - 1].time;
      const peek_room =log[peek].room

      time_per_room[peek_room] = time_per_room[peek_room] || 0;
      time_per_room[peek_room] += diff_time;
    }

    if (log_entry.action === "enter") {
      rooms_entered.push(i);
    } else {
      // exit
      rooms_entered.pop();
    }
  }

  // magica

  return time_per_room;
}

console.log("Esperado: map(Lobby = 25, Hallway1 = 10, Room1 = 15)");
console.log(
  timer([
    { room: "Lobby", time: 0, action: "enter" },
    { room: "Hallway1", time: 10, action: "enter" },
    { room: "Hallway1", time: 20, action: "exit" },
    { room: "Room1", time: 30, action: "enter" },
    { room: "Room1", time: 45, action: "exit" },
    { room: "Lobby", time: 50, action: "exit" },
  ])
);
console.log("--------");

console.log(
  "Esperado: map(Lobby = 30, Hallway1 = 60, Room1 = 20, Hallway2 = 50)"
);
console.log(
  timer([
    { room: "Lobby", time: 0, action: "enter" },
    { room: "Hallway1", time: 10, action: "enter" },
    { room: "Room1", time: 30, action: "enter" },
    { room: "Room1", time: 40, action: "exit" },
    { room: "Room1", time: 50, action: "enter" },
    { room: "Room1", time: 60, action: "exit" },
    { room: "Hallway1", time: 90, action: "exit" },
    { room: "Hallway2", time: 100, action: "enter" },
    { room: "Hallway2", time: 150, action: "exit" },
    { room: "Lobby", time: 160, action: "exit" },
  ])
);

// Lobby 0 Enter -
// Hallway1 10 Enter
// Room1 30 Enter
// Room1 40 Exit // back in hall way1 now
// Room1 50 Enter
// Room1 60 Exit
// Hallway1 90 Exit // back in Lobby
// Hallway2 100 Enter
// Hallway2 150 Exit
// Lobby 160 Exit

// function timer2(rooms, times, actions) { }

// console.log(timer2(["Lobby", "Hallway1", "Room1", "Room"],[0,10,20,30,45,50], ["enter", "enter", "exit"])
