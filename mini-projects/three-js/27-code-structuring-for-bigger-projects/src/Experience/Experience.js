import * as THREE from "three"
import Sizes from "./Utils/Sizes"
import Time from "./Utils/Time"
import Camera from "./Camera"
import Renderer from "./Renderer"
import World from "./World/World"

let instance = null

export default class Experience {
  constructor(canvas) {

    if(instance){
      // console.log('b')
      return instance
    }

    // to conver this class to a singleton
    instance = this


    // Global access
    window.experience = this

    // Options
    this.canvas = canvas

    // Setup
    this.sizes = new Sizes()
    this.time = new Time()
    this.scene = new THREE.Scene()
    this.camera = new Camera()
    this.renderer = new Renderer()
    this.world = new World()


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

  // resize - to the children
  resize(){
    this.camera.resize()
    this.renderer.resize();


  }

  // udpate world, animation, etc
  update(){
    this.camera.update()
    this.renderer.update()
    // console.log('update')
  }
}
