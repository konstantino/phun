This is definitely not the most efficient solution to the n-queens problem. In case you are still reading there is a slightly interesting aspect to this python implementation.

The different arrangements of the n-queens on a chess board are mapped to a number in a numeric system of base n. Using this arrangement, by simply incrementing from one number to the next a new arrangement is made.

For example, say that we are solving 4-queens - the arrangements are 0000, 0001, 0002, 0003, 0010, 0011, 0012, 0013, 0020 and so on.

In this fashion, 0000 would mean that in the first arrangement all queens are in the first row, while for 0001 all queens are in the first row with the exception of the last queen which is in the second row.