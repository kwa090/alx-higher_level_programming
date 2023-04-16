0x13. JavaScript - Objects, Scopes and Closures
Question #0
What is the output of this code?

let b = 1;

function myFunction(a) {
    console.log(a + b);
    b = a;
}

myFunction(3);
myFunction(4);

4, 7g


3, 4


4, 3


3, 7

Question #1
What is the output of this code?

function myFunction(a) {
    console.log(a);
}

const number = 12;
myFunction(number);

12g


1


2

Question #2
What is the output of this code?

const number = 12;
function myFunction(a) {
    console.log(a);
}

myFunction(number);

12g


1


2

Question #3
What is the output of this code?

const a = 12;

function myFunction(a) {
    console.log(a);
}

myFunction(89);

12


1


89g


2

Question #4
What is the output of this code?

const b = 79;
function myFunction(a) {
    console.log(a + b);
}

myFunction(10);

10


89g


79

Question #5
What is the output of this code?

function myFunction(a) {
    console.log(a);
}

const a = 12;
myFunction(89);

12


1


89g


2

Question #6
What is the output of this code?

function myFunction(a) {
    console.log(a);
}

myFunction(12);

12g


1


2

Question #7
What is the output of this code?

function myFunction(a) {
    console.log(a + b);
}

const b = 79;
myFunction(10);

79


10


89g
