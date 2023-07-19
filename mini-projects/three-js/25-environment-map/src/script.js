import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import * as dat from "lil-gui";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { RGBELoader } from "three/addons/loaders/RGBELoader.js";
import { EXRLoader } from "three/addons/loaders/EXRLoader.js";
import { GroundProjectedSkybox } from "three/addons/objects/GroundProjectedSkybox.js";

/**
 * Loaders
 */
const gltfLoader = new GLTFLoader();
const cubeTextureLoader = new THREE.CubeTextureLoader();
const rgbeLoader = new RGBELoader();
const exrLoader = new EXRLoader();
const textureLoader = new THREE.TextureLoader();

/**
 * Base
 */
// Debug
const gui = new dat.GUI();
const global = {}

// Canvas
const canvas = document.querySelector("canvas.webgl");

// Scene
const scene = new THREE.Scene();

/**
 * Update all materials
 */
const updateAllMaterials = () =>
{
    scene.traverse((child) =>
    {
        if(child.isMesh && child.material.isMeshStandardMaterial)
        {
            child.material.envMapIntensity = global.envMapIntensity
        }
    })
}

/**
 * Environment map
 */
scene.backgroundBlurriness = 0; // essa linha deixa o background com blur (fosco)
scene.environmentIntensity = 1;

gui.add(scene, 'backgroundBlurriness').min(0).max(1).step(0.001).onChange(updateAllMaterials);
gui.add(scene, 'environmentIntensity').min(0).max(10).step(0.001).onChange(updateAllMaterials);

// Global intesity
global.envMapIntensity = 1;
gui.add(global, 'envMapIntensity').min(0).max(10).step(0.001).onChange(updateAllMaterials);

// LDR cube texture
// const environmentMap = cubeTextureLoader.load([
//   // 6 images
//   "/environmentMaps/0/px.png",
//   "/environmentMaps/0/nx.png",
//   "/environmentMaps/0/py.png",
//   "/environmentMaps/0/ny.png",
//   "/environmentMaps/0/pz.png",
//   "/environmentMaps/0/nz.png",
// ]);

// scene.environment = environmentMap; // essa linha adiciona o environmentMap na cena inteira
// scene.background = environmentMap;

// HDR (RGBE)
// rgbeLoader.load("/environmentMaps/blender-2k.hdr", (environmentMap) => {
//   environmentMap.mapping = THREE.EquirectangularReflectionMapping;

//   scene.background = environmentMap;
//   scene.environment = environmentMap;
// });

// // EXR (OpenEXR)
// exrLoader.load("/environmentMaps/nvidiaCanvas-4k.exr", (environmentMap) => {
//   environmentMap.mapping = THREE.EquirectangularReflectionMapping;

//   scene.background = environmentMap;
//   scene.environment = environmentMap;
// });

// LDR equirectangular
// const environmentMap = textureLoader.load('/environmentMaps/holographic_disneyworld_with_just_one_castle_tree.jpg');
// environmentMap.mapping = THREE.EquirectangularReflectionMapping;
// environmentMap.colorSpace = THREE.SRGBColorSpace;
// scene.background = environmentMap;
// scene.environment = environmentMap;


// Ground projected skybox - aqui vou tirar o objeto flutuando
// rgbeLoader.load("/environmentMaps/2/2k.hdr", (environmentMap) => {

//   environmentMap.mapping = THREE.EquirectangularReflectionMapping;
//   scene.environment = environmentMap;

//   // skybox
//   const skybox = new GroundProjectedSkybox(environmentMap, 32);
//   skybox.radius = 120;
//   skybox.height = 11;
//   skybox.scale.setScalar(50);
//   scene.add(skybox);

//   gui.add(skybox, 'radius', 1, 200, 0.1).name('skybox radius');
//   gui.add(skybox, "height", 1, 200, 0.1).name("skybox height");
// })

/**
 * Real time environment map
 */
const environmentMap = textureLoader.load(
  "/environmentMaps/blockadesLabsSkybox/interior_views_cozy_wood_cabin_with_cauldron_and_p.jpg"
);
environmentMap.mapping = THREE.EquirectangularReflectionMapping;
environmentMap.colorSpace = THREE.SRGBColorSpace;

scene.background = environmentMap;

// Holy donut
const holyDonut = new THREE.Mesh(
  new THREE.TorusGeometry(8, 0.5),
  new THREE.MeshBasicMaterial({
    color: new THREE.Color(10, 4, 2), // deixa a luz no tom mais quente
  })
);
holyDonut.layers.enable(1); // aqui nos vemos o reflexo do donuts na cena
holyDonut.position.y = 4;
scene.add(holyDonut);

// Cube render target
const cubeRenderTarget = new THREE.WebGLCubeRenderTarget(256, {

  // type: THREE.FloatType, // realistic lighting - float use 32 bits
  type: THREE.HalfFloatType, // realistic lighting - halffloat use 16 bits
});

scene.environment = cubeRenderTarget.texture;

// cube camera
const cubeCamera = new THREE.CubeCamera(0.1, 100, cubeRenderTarget);
cubeCamera.layers.set(1); // nao podemos ver o reflexo do cubo na cena, entao colocamos ele em uma layer diferente

/**
 * To change the layers of an object or a camera, we can use 3 methods
 *
 * object.layers.enable(1) // enable layer 1 - add layer to the object
 * object.layers.disable(1) // disable layer 1 - remove layer from the object
 * object.layers.set(1) // set layer 1 - remove all layers and add only layer 1
 */


/**
 * Torus Knot
 */
const torusKnot = new THREE.Mesh(
  new THREE.TorusKnotGeometry(1, 0.4, 100, 16),
  new THREE.MeshStandardMaterial({
    roughness: 0,
    metalness: 1,
    color: 0xaaaaaa,
  })
);

// torusKnot.material.envMap = environmentMap;
torusKnot.position.y = 4;
torusKnot.position.x = -4;
scene.add(torusKnot);



/**
 * Models
 */
gltfLoader.load("/models/FlightHelmet/glTF/FlightHelmet.gltf", (gltf) => {
  gltf.scene.scale.set(10, 10, 10);
  scene.add(gltf.scene);

  updateAllMaterials() // essa linha atualiza todos os materiais do modelo
});

/**
 * Sizes
 */
const sizes = {
  width: window.innerWidth,
  height: window.innerHeight,
};

window.addEventListener("resize", () => {
  // Update sizes
  sizes.width = window.innerWidth;
  sizes.height = window.innerHeight;

  // Update camera
  camera.aspect = sizes.width / sizes.height;
  camera.updateProjectionMatrix();

  // Update renderer
  renderer.setSize(sizes.width, sizes.height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
});

/**
 * Camera
 */
// Base camera
const camera = new THREE.PerspectiveCamera(
  75,
  sizes.width / sizes.height,
  0.1,
  100
);
camera.position.set(4, 5, 4);
scene.add(camera);

// Controls
const controls = new OrbitControls(camera, canvas);
controls.target.y = 3.5;
controls.enableDamping = true;

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
});
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

/**
 * Animate
 */
const clock = new THREE.Clock();
const tick = () => {
  // Time
  const elapsedTime = clock.getElapsedTime();

  // real time environment map
  if (holyDonut){
    holyDonut.rotation.x = Math.sin(elapsedTime) * 2;

    cubeCamera.update(renderer, scene); // update each frame
  }

  // Update controls
  controls.update();

  // Render
  renderer.render(scene, camera);

  // Call tick again on the next frame
  window.requestAnimationFrame(tick);
};

tick();

