import * as THREE from "three";
import * as dat from "lil-gui";
import gsap from "gsap";

THREE.ColorManagement.enabled = false;

/**
 * Debug
 */
const gui = new dat.GUI();

const parameters = {
  materialColor: "#ffeded",
};

gui.addColor(parameters, "materialColor").onChange(() => {
  // on change, update the material color
  material.color.set(parameters.materialColor);
  particlesMaterial.color.set(parameters.materialColor);
});

/**
 * Base
 */
// Canvas
const canvas = document.querySelector("canvas.webgl");

// Scene
const scene = new THREE.Scene();

/**
 * Objects
 */
// texture
const textureLoader = new THREE.TextureLoader();
const particleTexture = textureLoader.load("/textures/particles/9.png");
const gradientTexture = textureLoader.load("/textures/gradients/3.jpg"); // 3.jpg is the gradient image
gradientTexture.magFilter = THREE.NearestFilter; // to avoid blurring

// material
const material = new THREE.MeshToonMaterial({
  color: parameters.materialColor,
  gradientMap: gradientTexture,
});

// meshes
const objectsDistance = 4;

const mesh1 = new THREE.Mesh(new THREE.TorusGeometry(1, 0.4, 16, 60), material);
const mesh2 = new THREE.Mesh(new THREE.ConeGeometry(1, 2, 32), material);
const mesh3 = new THREE.Mesh(
  new THREE.TorusKnotGeometry(0.8, 0.35, 100, 16),
  material
);

scene.add(mesh1, mesh2, mesh3);

mesh1.position.y = -objectsDistance * 0;
mesh2.position.y = -objectsDistance * 1;
mesh3.position.y = -objectsDistance * 2;

mesh1.position.x = 2;
mesh2.position.x = -2;
mesh3.position.x = 2;

const sectionMeshes = [mesh1, mesh2, mesh3]; // to loop through them

/**
 * Particles
 */
// Geometry
const particlesCount = 1000;
const positions = new Float32Array(particlesCount * 3); // 3 because we have x, y, z

for (let i = 0; i < particlesCount * 3; i++) {
  positions[i * 3 + 0] = (Math.random() - 0.5) * 10; // x position
  positions[i * 3 + 1] = objectsDistance * 0.5 - Math.random() *  objectsDistance * sectionMeshes.length; // y position
  positions[i * 3 + 2] = (Math.random() - 0.5) * 10; // z position
}

const particlesGeometry = new THREE.BufferGeometry();

particlesGeometry.setAttribute(
  "position",
  new THREE.BufferAttribute(positions, 3)
);

// Material
const particlesMaterial = new THREE.PointsMaterial({
  color: parameters.materialColor,
  sizeAttenuation: true,
  size: 0.2,
  transparent: true, // to see the alpha map
  alphaMap: particleTexture,
});

// Points
const particles = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particles);


/**
 * Lights
 */
const directionalLight = new THREE.DirectionalLight("#ffffff", 1);
directionalLight.position.set(1, 1, 0);
scene.add(directionalLight);
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
// group - the camera will move inside the group
const cameraGroup = new THREE.Group();
scene.add(cameraGroup);

// Base camera
const camera = new THREE.PerspectiveCamera(
  35,
  sizes.width / sizes.height,
  0.1,
  100
);
camera.position.z = 6;
cameraGroup.add(camera);

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
  alpha: true, // by default, the clear alpha value is 0
});
// renderer.setClearColor(1)
renderer.outputColorSpace = THREE.LinearSRGBColorSpace;
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

/**
 * Scroll
 */
let scrollY = window.scrollY;
let currentSection = 0;

window.addEventListener("scroll", () => {
  scrollY = window.scrollY;
  // console.log(scrollY);

  const newSection = Math.round(scrollY / sizes.height);
  // console.log(newSection);

  if(newSection != currentSection){

    currentSection = newSection;
    // console.log('New section: ', currentSection)

    // console.log(sectionMeshes[currentSection].rotation)

    gsap.to(
      sectionMeshes[currentSection].rotation,
      {
        duration: 1.5,
        ease: "power2.inOut",
        x: '+=6',
        y: '+=3',
        z: '+=1.5'
      }
      );
  }
});

/**
 * Cursor
 */
const cursor = {}
cursor.x = 0
cursor.y = 0

window.addEventListener('mousemove', (event) =>{
  cursor.x = event.clientX / sizes.width - 0.5
  cursor.y = event.clientY / sizes.height - 0.5

  // console.log(cursor)
})

/**
 * Animate
 */
const clock = new THREE.Clock();
let previousTime = 0;

const tick = () => {
  const elapsedTime = clock.getElapsedTime();
  const deltaTime = elapsedTime - previousTime; // to get the time between each frame
  previousTime = elapsedTime;

  // console.log(deltaTime);

  // animate the camera
  camera.position.y = (-scrollY / sizes.height) * objectsDistance; // to move the camera up and down

  // change the camera position based on the cursor position
  const parallaxX = cursor.x * 0.5;
  const parallaxY = - cursor.y * 0.5 // to invert the movement
  cameraGroup.position.x += (parallaxX - cameraGroup.position.x) * 5 * deltaTime
  cameraGroup.position.y += (parallaxY - cameraGroup.position.y) * 5 * deltaTime

  // animate the meshes
  for (const mesh of sectionMeshes) {
    // to rotate the meshes mais rapido quando chegar na sessao do objeto
    mesh.rotation.x += deltaTime * 0.1;
    mesh.rotation.y += deltaTime * 0.12;
  }

  // animate the particles
  // particles.rotation.y = - elapsedTime * 0.02;
  // particles.rotation.z = - elapsedTime * 0.02;

  // Render
  renderer.render(scene, camera);

  // Call tick again on the next frame
  window.requestAnimationFrame(tick);
};

tick();
