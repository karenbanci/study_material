import * as THREE from "three";
import {GLTFLoader} from "three/examples/jsm/loaders/GLTFLoader";
import EventEmitter from "./EventEmitter";

export default class Resources extends EventEmitter {
  constructor(sources) {
    super();

    // console.log(sources, "sources")

    // Options
    this.sources = sources;

    // Setup
    this.items = {};
    this.toload = this.sources.length;
    this.loaded = 0;

    this.setLoaders()
    this.startLoading()
  }

  setLoaders() {
    this.loaders = {};
    this.loaders.gltfLoader = new GLTFLoader();
    this.loaders.textureLoader = new THREE.TextureLoader();
    this.loaders.cubeTextureLoader = new THREE.CubeTextureLoader();
  }

  // method and loop throught the sources array to load them by using corresponding loader
  startLoading(){
    for(const source of this.sources){
      // console.log("source", source)

      if (source.type === "gltfModel") {
        this.loaders.gltfLoader.load(source.path, (file) => {
          this.sourceLoaded(source, file);
        });

      } else if (source.type === "texture") {
        this.loaders.textureLoader.load(source.path, (file) => {
          this.sourceLoaded(source, file);
        });

      } else if (source.type === "cubeTexture") {
        this.loaders.cubeTextureLoader.load(source.path, (file) => {
          this.sourceLoaded(source, file);
        });
      }
    }

  }

  sourceLoaded(source, file){
    this.items[source.name] = file;

    // increment loaded
    this.loaded++;

    if(this.loaded === this.toload){

      // console.log('finished loading')
      this.trigger('ready')
    }

  }
}
