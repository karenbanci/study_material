import * as THREE from "three"
import Sizes from "./Utils/Sizes"
import Time from "./Utils/Time"
import Camera from "./Camera"
import Resources from "./Utils/Resources"
import Renderer from "./Renderer"
import World from "./World/World"
// import Floor from "./World/Floor"
import sources from "./sources"
import Debug from "./Utils/Debug"

// console.log(sources)

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
    this.debug = new Debug()
    this.sizes = new Sizes()
    this.time = new Time()
    this.scene = new THREE.Scene()
    this.camera = new Camera()
    this.renderer = new Renderer()
    this.resources = new Resources(sources)
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
    this.world.update()
    this.renderer.update()
    // console.log('update')
  }

  destroy(){
    this.sizes.off("resize")  // remove the event listener
    this.time.off("tick") // remove the event listener

    // Traverse the scene and dispose of all objects
    this.scene.traverse((child) => {
      console.log(child)

      if(child instanceof THREE.Mesh){

        child.geometry.dispose()

        // Loop through the material properties
        for (const key in child.material){

          const value = child.material[key]
          // console.log(value)

          // test if ther is a dispose function
          if(value && typeof value.dispose === 'function'){
            value.dispose()
          }
        }


      }
    })

    this.camera.controls.dispose()
    this.renderer.instance.dispose()

    if(this.debug.active){
      this.debug.gui.destroy()
    }
  }

}
