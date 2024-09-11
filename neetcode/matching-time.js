/**

input
Start   | End  | Name
10      | 100  | Abby
50      | 70   | Ben
60      | 120  | Carla
150     | 300  | David


Output:
10  | 50  | Abby
50  | 60  | Abby, Ben
60  | 70  | Abby, Ben, Carla
70  | 100 | Abby, Carla
100 | 120 | Carla
150 | 300 | David


10 - 50 - +Abby
50 - 60 - Abby +Ben
60 - 70 - Abby, Ben  +Carla
70 - 100 - Abby, -Ben Carla
100 - 120 - -Abby, Carla
150 - 300 - David


10 ------------------ 100
            Abby
      50 -------- 70
              Ben
          60 ------------------120
             Carla
                                    150 -------- 300
                                          David


1. A partir dos dados de entrada contruir a tabela de unidades de tempo

2. Percorrer cada unidade de tempo
2.1. Entrou alguém?

 */

// Input Data
const intervals = [
  { start: 10, end: 100, name: "Abby" },
  { start: 50, end: 70, name: "Ben" },
  { start: 60, end: 120, name: "Carla" },
  { start: 150, end: 300, name: "David" },
];

// Step 1: Extract all unique points (start or end points) and sort them
let points = [];
intervals.forEach(({ start, end }) => {
  points.push(start, end);
});

points = [...new Set(points)].sort((a, b) => a - b); // Remove duplicates and sort

// Step 2: Create the output intervals by processing each point
let result = [];
for (let i = 0; i < points.length - 1; i++) {
  let start = points[i];
  let end = points[i + 1];

  // Find active names in this range
  let activeNames = intervals
    .filter((interval) => interval.start <= start && interval.end >= end)
    .map((interval) => interval.name);

  result.push({ start, end, names: activeNames });
}

// Step 3: Output the result
result.forEach(({ start, end, names }) => {
  console.log(`${start} | ${end} | ${names.join(", ")}`);
});
