const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';

class Field {
  constructor(field){
    this.field = field;
  }

  get field(){
    return this.field;
  }

  const myField = new Field([
    ['*', '░', 'O'],
    ['░', 'O', '░'],
    ['░', '^', '░'],
  ]);

  print(){
    console.log(myField.join(''))
  }


}
