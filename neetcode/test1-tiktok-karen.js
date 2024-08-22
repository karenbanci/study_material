/*
    * Complete the 'GetOptimalContentStorage' function below.
//  *
//  * The function is expected to return an INTEGER.
//  * The function accepts INTEGER_ARRAY tiktokStorage as parameter.

// first case
// index    0.  1. 2  3  4.      0  1  2. 3. 4
//          [1, 0, 1, 0, 1]  -> [0, 0, 1, 1, 1] - 1 operation
// swap arr[0] and arr[3]

// second case
//index     0   1  2  3  4. 5  6. 7. 8       0. 1. 2. 3. 4. 5. 6. 7. 8
//          [1, 0, 0, 1, 1, 0, 0, 0, 1]    [1, 1, 0, 1, 1, 0, 0, 0, 0]
// fist operation   arr[1]  and arr[8]

//.   0. 1. 2. 3. 4. 5. 6. 7. 8      0. 1. 2. 3. 4. 5. 6. 7. 8
//   [1, 1, 0, 1, 1, 0, 0, 0, 0] -> [1, 1, 1, 1, 0, 0, 0, 0, 0]
// second operation   arr[2]  and arr[4]
*/
