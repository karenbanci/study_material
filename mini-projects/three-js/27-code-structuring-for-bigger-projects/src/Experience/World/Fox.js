import * as THREE from "three";
import Experience from "../Experience";

export default class Fox {

  constructor() {
    this.experience = new Experience();
    this.scene = this.experience.scene;
    this.resources = this.experience.resources;
    this.time = this.experience.time;
    this.debug = this.experience.debug;

    // console.log(this.debug)
    //Debug
    if(this.debug){
      this.debugFolder = this.debug.ui.addFolder("fox");
      this.debugFolder.open();
    }

    // console.log('fox teste')

    // Setup
    this.resource = this.resources.items.foxModel;
    // console.log(this.resource)

    this.setModel()
    this.setAnimation();


  }
  setModel(){
    this.model = this.resource.scene;
    this.model.scale.set(0.02, 0.02, 0.02);
    this.scene.add(this.model);

    // add shadow
    this.model.traverse((child) => {
      // console.log(child)
      if(child instanceof THREE.Mesh){
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
  }

  // add animation
  setAnimation(){
    this.animation = {};
    this.animation.mixer = new THREE.AnimationMixer(this.model);

    this.animation.actions = {};

    // creating the actions
    this.animation.actions.idle = this.animation.mixer.clipAction(this.resource.animations[0]);
    this.animation.actions.walking = this.animation.mixer.clipAction(this.resource.animations[1]);
    this.animation.actions.running = this.animation.mixer.clipAction(this.resource.animations[2]);

    // console.log(this.animation.actions)
    this.animation.actions.current = this.animation.actions.idle;
    this.animation.actions.current.play();

    this.animation.play = (name) => {

      const newAction = this.animation.actions[name];
      const oldAction = this.animation.actions.current;

      newAction.reset()
      newAction.play()
      newAction.crossFadeFrom(oldAction, 1)

      this.animation.actions.current = newAction;
    }
    // for testing, you can type this comand in the console
    // window.experience.world.fox.animation.play('running')

    // Debug
    if(this.debug.active){

      const debugObject = {
        playIdle: () => {this.animation.play('idle')},
        playWalking: () => {this.animation.play('walking')},
        playRunning: () => {this.animation.play('running')}
      };
      this.debugFolder.add(debugObject, 'playIdle');
      this.debugFolder.add(debugObject, 'playWalking');
      this.debugFolder.add(debugObject, 'playRunning');

    }
  }

  update(){
    // console.log('update')
    this.animation.mixer.update(this.time.delta * 0.001);
  }


}
