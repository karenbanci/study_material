// manipulação de objeto
/* const objeto = {x:1};
objeto.x = 5;
objeto.y = 3;
console.log("objeto" + JSON.stringify(objeto)); */


// Inheritance
let o = {};
o.x=1;
let p = Object.create(o);
p.y=2;
let q = Object.create(p);
p.z=3;
let f = q.toString();
console.log(q.x + q.y)
