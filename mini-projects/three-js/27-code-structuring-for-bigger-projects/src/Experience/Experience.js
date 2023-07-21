import * as THREE from "three"
import Sizes from "./Utils/Sizes"
import Time from "./Utils/Time"
import Camera from "./Camera"

export default class Experience {
  constructor(canvas) {
    // Global access
    window.experience = this

    // Options
    this.canvas = canvas

    // Setup
    this.sizes = new Sizes()
    this.time = new Time()
    this.scene = new THREE.Scene()
    this.camera = new Camera(this)

    // Sizes resize event
    this.sizes.on("resize", () => {
      this.resize()
    })

    // Time tick event
    this.time.on("tick", () => {
      this.update()
    }
    )
  }

  // resize world, animation, etc
  resize(){

  }

  // udpate world, animation, etc
  update(){
    // console.log('update')
  }
}
