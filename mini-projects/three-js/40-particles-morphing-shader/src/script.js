import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import GUI from "lil-gui";
import gsap from "gsap";
import particlesVertexShader from "./shaders/particles/vertex.glsl";
import particlesFragmentShader from "./shaders/particles/fragment.glsl";

/**
 * Base
 */
// Debug
const gui = new GUI({ width: 340 });
const debugObject = {};

// Canvas
const canvas = document.querySelector("canvas.webgl");

// Scene
const scene = new THREE.Scene();

// Loaders
const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath("./draco/");
const gltfLoader = new GLTFLoader();
gltfLoader.setDRACOLoader(dracoLoader);

/**
 * Sizes
 */
const sizes = {
  width: window.innerWidth,
  height: window.innerHeight,
  pixelRatio: Math.min(window.devicePixelRatio, 2),
};

window.addEventListener("resize", () => {
  // Update sizes
  sizes.width = window.innerWidth;
  sizes.height = window.innerHeight;
  sizes.pixelRatio = Math.min(window.devicePixelRatio, 2);

  // Materials
  if (particles)
    particles.material.uniforms.uResolution.value.set(
      sizes.width * sizes.pixelRatio,
      sizes.height * sizes.pixelRatio
    );

  // Update camera
  camera.aspect = sizes.width / sizes.height;
  camera.updateProjectionMatrix();

  // Update renderer
  renderer.setSize(sizes.width, sizes.height);
  renderer.setPixelRatio(sizes.pixelRatio);
});

/**
 * Camera
 */
// Base camera
const camera = new THREE.PerspectiveCamera(
  35,
  sizes.width / sizes.height,
  0.1,
  100
);
camera.position.set(0, 0, 8 * 2);
scene.add(camera);

// Controls
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
  antialias: true,
});

renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(sizes.pixelRatio);

debugObject.clearColor = "#160920";
gui.addColor(debugObject, "clearColor").onChange(() => {
  renderer.setClearColor(debugObject.clearColor);
});
renderer.setClearColor(debugObject.clearColor);

/**
 * Particles
 */
// Load Models
// essa linha de código é necessária para que quando mudamos o tamanho da tela, o objeto mude de tamanho
let particles = null;

gltfLoader.load("./models.glb", (gltf) => {
  particles = {};
  particles.index = 0;

  // Positions
  const positions = gltf.scene.children.map(
    (child) => child.geometry.attributes.position
  );
  // console.log(positions); // retorna uma  array

  particles.maxCount = 0;

  for (const position of positions) {
    if (position.count > particles.maxCount) {
      particles.maxCount = position.count;
    }
  }
  // console.log(particles.maxCount);

  // Positions
  particles.positions = [];
  for (const position of positions) {
    const originalArray = position.array;
    const newArray = new Float32Array(particles.maxCount * 3);

    for (let i = 0; i < particles.maxCount; i++) {
      const i3 = i * 3;

      if (i3 < originalArray.length) {
        newArray[i3 + 0] = originalArray[i3 + 0];
        newArray[i3 + 1] = originalArray[i3 + 1];
        newArray[i3 + 2] = originalArray[i3 + 2];
      } else {
        const randomIndex = Math.floor(position.count * Math.random()) * 3;
        // console.log(randomIndex);
        newArray[i3 + 0] = originalArray[randomIndex + 0];
        newArray[i3 + 1] = originalArray[randomIndex + 1];
        newArray[i3 + 2] = originalArray[randomIndex + 2];
      }
    }
    particles.positions.push(new THREE.Float32BufferAttribute(newArray, 3));
  }

  // console.log(particles.positions);

  // Geometry
  const sizesArray = new Float32Array(particles.maxCount);

  for (let i = 0; i < particles.maxCount; i++) {
    sizesArray[i] = Math.random();
  }

  particles.geometry = new THREE.BufferGeometry();
  particles.geometry.setAttribute(
    "position",
    particles.positions[particles.index]
  );
  particles.geometry.setAttribute("aPositionTarget", particles.positions[3]);
  particles.geometry.setAttribute(
    "aSize",
    new THREE.BufferAttribute(sizesArray, 1)
  );

  // particles.geometry.setIndex(null);

  // Material
  particles.colorA = "#ff7300";
  particles.colorB = "#0091ff";

  particles.material = new THREE.ShaderMaterial({
    vertexShader: particlesVertexShader,
    fragmentShader: particlesFragmentShader,
    uniforms: {
      uSize: new THREE.Uniform(0.4),
      uResolution: new THREE.Uniform(
        new THREE.Vector2(
          sizes.width * sizes.pixelRatio,
          sizes.height * sizes.pixelRatio
        )
      ),
      uProgress: new THREE.Uniform(0),
      uColorA: new THREE.Uniform(new THREE.Color(particles.colorA)),
      uColorB: new THREE.Uniform(new THREE.Color(particles.colorB)),
    },
    blending: THREE.AdditiveBlending, // deixar a particula brilhando
    depthWrite: false, // nao escrever no buffer de profundidade
  });

  // Points
  particles.points = new THREE.Points(particles.geometry, particles.material);
  // frustumCulled: false, para que a particula não seja cortada pela camera
  particles.points.frustumCulled = false;
  scene.add(particles.points);

  // Methods
  particles.morph = (index) => {
    // update atributes
    particles.geometry.attributes.position =
      particles.positions[particles.index];
    particles.geometry.attributes.aPositionTarget = particles.positions[index];

    // Animate uProgress
    gsap.fromTo(
      particles.material.uniforms.uProgress,
      { value: 0 }, // from
      { value: 1, duration: 3, ease: "linear" } // to
    );

    // save index
    particles.index = index;
  };

  particles.morph0 = () => {
    particles.morph(0);
  };
  particles.morph1 = () => {
    particles.morph(1);
  };
  particles.morph2 = () => {
    particles.morph(2);
  };
  particles.morph3 = () => {
    particles.morph(3);
  };

  // mudar o modelo a cada 5 segundos
  setInterval(() => {
    const newIndex = Math.floor(Math.random() * 4);
    particles.morph(newIndex);
  }, 5000);

  //Tweaks
  gui.addColor(particles, "colorA").onChange(() => {
    particles.material.uniforms.uColorA.value.set(particles.colorA);
  });
  gui.addColor(particles, "colorB").onChange(() => {
    particles.material.uniforms.uColorB.value.set(particles.colorB);
  });

  gui
    .add(particles.material.uniforms.uProgress, "value")
    .min(0)
    .max(1)
    .step(0.001)
    .name("uProgress")
    .listen();

  gui.add(particles, "morph0").name("Morph 0");
  gui.add(particles, "morph1").name("Morph 1");
  gui.add(particles, "morph2").name("Morph 2");
  gui.add(particles, "morph3").name("Morph 3");
});

/**
 * Animate
 */
const tick = () => {
  // Update controls
  controls.update();

  // Render normal scene
  renderer.render(scene, camera);

  // Call tick again on the next frame
  window.requestAnimationFrame(tick);
};

tick();
