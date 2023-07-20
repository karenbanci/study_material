import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import * as dat from "lil-gui";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { RGBELoader } from "three/examples/jsm/loaders/RGBELoader.js";
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader.js";

/**
 * Loaders
 */
const gltfLoader = new GLTFLoader();
const rgbeLoader = new RGBELoader();
const textureLoader = new THREE.TextureLoader();

/**
 * Base
 */
// Debug
const gui = new dat.GUI();
const global = {};

// Canvas
const canvas = document.querySelector("canvas.webgl");

// Scene
const scene = new THREE.Scene();

/**
 * Update all materials
 */
const updateAllMaterials = () => {
  scene.traverse((child) => {
    if (child.isMesh && child.material.isMeshStandardMaterial) {
      child.material.envMapIntensity = global.envMapIntensity;

      child.castShadow = true; // o objeto vai projetar sombra
      child.receiveShadow = true; // o objeto vai receber sombra
    }
  });
};

/**
 * Environment map
 */
// Global intensity
global.envMapIntensity = 1;
gui
  .add(global, "envMapIntensity")
  .min(0)
  .max(10)
  .step(0.001)
  .onChange(updateAllMaterials);

// HDR (RGBE) equirectangular
rgbeLoader.load("/environmentMaps/0/2k.hdr", (environmentMap) => {
  environmentMap.mapping = THREE.EquirectangularReflectionMapping;

  scene.background = environmentMap;
  scene.environment = environmentMap;
});

/**
 * Directional light
 */
const directionalLight = new THREE.DirectionalLight("#ffffff", 2);
directionalLight.position.set(-1, 6.5, 2.5);
scene.add(directionalLight);

gui
  .add(directionalLight, "intensity")
  .min(0)
  .max(10)
  .step(0.001)
  .name("lightIntensity");
gui
  .add(directionalLight.position, "x")
  .min(-10)
  .max(10)
  .step(0.001)
  .name("lightX");
gui
  .add(directionalLight.position, "y")
  .min(-10)
  .max(10)
  .step(0.001)
  .name("lightY");
gui
  .add(directionalLight.position, "z")
  .min(-10)
  .max(10)
  .step(0.001)
  .name("lightZ");

// shadows
directionalLight.castShadow = true;
directionalLight.shadow.normalBias = 0.036; // vai deixar a sombra mais suave
directionalLight.shadow.bias = - 0.015; // vai deixar a sombra mais suave
directionalLight.shadow.camera.far = 15; // quanto maior o valor, mais longe a sombra vai aparecer
directionalLight.shadow.mapSize.set(256, 256); // quanto maior o valor, mais detalhado fica a sombra e quanto menor, mais pixelado fica a sombra e melhor o desempenho
gui.add(directionalLight, "castShadow").name("castShadow");
gui
  .add(directionalLight.shadow, "normalBias")
  .min(-0.05)
  .max(0.05)
  .step(0.001)
  .name("normalBias");
gui
  .add(directionalLight.shadow, "bias")
  .min(-0.05)
  .max(0.05)
  .step(0.001)
  .name("normalBias");

// // Helper
// const directionalLightCameraHelper = new THREE.CameraHelper(
//   directionalLight.shadow.camera
// );
// scene.add(directionalLightCameraHelper); // podemos ver a camera como ela está posicionada

// Target
directionalLight.target.position.set(0, 4, 0); // posição do objeto que a luz está apontando
directionalLight.target.updateMatrixWorld(); // atualiza a posição do objeto

/**
 * Models
 */
// Helmet
// gltfLoader.load("/models/FlightHelmet/glTF/FlightHelmet.gltf", (gltf) => {
//   gltf.scene.scale.set(10, 10, 10);
//   scene.add(gltf.scene);

//   updateAllMaterials();
// });

const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath("/draco/");

gltfLoader.setDRACOLoader(dracoLoader);

// Hambuger
gltfLoader.load("/models/hambuguer.glb", (gltf) => {
  gltf.scene.scale.set(3, 3, 3);
  gltf.scene.position.set(0, 2.5, 0);
  scene.add(gltf.scene);

  updateAllMaterials();
});

/**
 * Floor
 */
const floorColorTexture = textureLoader.load(
  "/textures/wood_cabinet_worn_long/wood_cabinet_worn_long_diff_1k.jpg"
);
const floorNormalTexture = textureLoader.load(
  "/textures/wood_cabinet_worn_long/wood_cabinet_worn_long_diff_1k"
);
const floorAORoughnessMetalnessTexture = textureLoader.load(
  "/textures/wood_cabinet_worn_long/wood_cabinet_worn_long_arm_1k.jpg"
);

floorColorTexture.colorSpace = THREE.SRGBColorSpace; // deixa a cor mais realista

const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(8, 8),
  new THREE.MeshStandardMaterial({
    map: floorColorTexture,
    normalMap: floorNormalTexture,
    aoMap: floorAORoughnessMetalnessTexture,
    roughnessMap: floorAORoughnessMetalnessTexture,
    metalnessMap: floorAORoughnessMetalnessTexture,
  })
);
floor.rotation.x = -Math.PI * 0.5; // rotaciona o objeto em 90 graus
scene.add(floor);

/**
 * Wall
 */
const wallColorTexture = textureLoader.load(
  "/textures/castle_brick_broken_06/castle_brick_broken_06_diff_1k.jpg"
);
const wallNormalTexture = textureLoader.load(
  "/textures/castle_brick_broken_06/castle_brick_broken_06_diff_1k"
);
const wallAORoughnessMetalnessTexture = textureLoader.load(
  "/textures/castle_brick_broken_06/castle_brick_broken_06_arm_1k.jpg"
);

wallColorTexture.colorSpace = THREE.SRGBColorSpace; // deixa a cor mais realista

const wall = new THREE.Mesh(
  new THREE.PlaneGeometry(8, 8),
  new THREE.MeshStandardMaterial({
    map: wallColorTexture,
    normalMap: wallNormalTexture,
    aoMap: wallAORoughnessMetalnessTexture,
    roughnessMap: wallAORoughnessMetalnessTexture,
    metalnessMap: wallAORoughnessMetalnessTexture,
  })
);
wall.position.y = 4;
wall.position.z = -4;
scene.add(wall);

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
  antialias: true, // suaviza as bordas
});
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// Tone mapping
renderer.toneMapping = THREE.ReinhardToneMapping;
renderer.toneMappingExposure = 3; // quanto maior o valor, mais claro fica a imagem

gui.add(renderer, "toneMapping", {
  No: THREE.NoToneMapping, // no quer dizer que não vai aplicar nenhum tone mapping
  Linear: THREE.LinearToneMapping, // parece mais claro
  Reinhard: THREE.ReinhardToneMapping, // parece mais realista
  Cineon: THREE.CineonToneMapping, // parece mais escuro
  ACESFilmic: THREE.ACESFilmicToneMapping,
});

gui.add(renderer, "toneMappingExposure").min(0).max(10).step(0.001);

// Phiysically accurate lights
renderer.useLegacyLights = false; // Sempre começar o projeto com false
gui.add(renderer, "useLegacyLights").name("useLegacyLights");

// shadows
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // suaviza as sombras

/**
 * Animate
 */
const tick = () => {
  // Update controls
  controls.update();

  // Render
  renderer.render(scene, camera);

  // Call tick again on the next frame
  window.requestAnimationFrame(tick);
};

tick();
