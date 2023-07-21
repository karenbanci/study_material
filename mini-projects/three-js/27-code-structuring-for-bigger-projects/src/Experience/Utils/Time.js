import EventEmitter from "./EventEmitter";

export default class Time extends EventEmitter {
  constructor() {
    super();

    // console.log('Time')

    // Setup
    this.start = Date.now();
    this.current = this.start;
    this.elapsed = 0;
    this.delta = 16; // default screen 16 fps

    window.requestAnimationFrame(() => {
      this.tick();
    });
  }

  tick() {
    // console.log('tick')

    const currentTime = Date.now();
    this.delta = currentTime - this.current;
    this.current = currentTime;
    this.elapsed = this.current - this.start;

    this.trigger("tick");


    window.requestAnimationFrame(() => {
      this.tick();
    });
  }
}
