import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import * as dat from 'lil-gui'
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader.js'
import { TextGeometry } from 'three/examples/jsm/geometries/TextGeometry.js'

/**
 * Base
 */
// Debug
const gui = new dat.GUI();

// Canvas
const canvas = document.querySelector('canvas.webgl');

// Scene
const scene = new THREE.Scene();

// Axes helper
// const axesHelper = new THREE.AxesHelper();
// scene.add(axesHelper);

// Bouding is a information associated with the geometry that tells what space is taken up by the geometry

/**
 * Textures
 */
const textureLoader = new THREE.TextureLoader();
const matcapTexture = textureLoader.load('/textures/matcaps/8.png');

/**
 * Fonts
 */
const fontLoader = new FontLoader();
fontLoader.load(
  '/fonts/helvetiker_regular.typeface.json',
  (font) => {
    const textGeometry = new TextGeometry('Karen Banci', {
      font: font,
      size: 0.5,
      height: 0.2,
      curveSegments: 6, // how many segments the text has
      bevelEnabled: true, // whether or not the text has a bevel
      bevelThickness: 0.03, // how thick the bevel is
      bevelSize: 0.02, // how deep the bevel is
      bevelOffset: 0,  // how far from the edge of the text the bevel is
      bevelSegments: 5, // how many bevel segments there are
    })

    // textGeometry.computeBoundingBox(); // compute the bounding box of the text
    // // console.log(textGeometry.boundingBox);
    // textGeometry.translate(
    //   // translate the text to the center of the screen
    //   -(textGeometry.boundingBox.max.x - 0.02) * 0.5,
    //   -(textGeometry.boundingBox.max.y - 0.02) * 0.5,
    //   -(textGeometry.boundingBox.max.z - 0.03) * 0.5
    // );

    textGeometry.center(); // center the text

    const material = new THREE.MeshMatcapMaterial({ matcap: matcapTexture });
    // textMaterial.wireframe = true;
    const text = new THREE.Mesh(textGeometry, material);
    scene.add(text);

    // console.time('donuts');
    // deixar essas constantes fora do loop para que o javascript não tenha que criar uma nova variável a cada iteração, isso melhora a performance. Deixa o código mais rápido
    const donutGeometry = new THREE.TorusGeometry(0.3, 0.2, 20, 45);
    const donutMaterial = new THREE.MeshMatcapMaterial({ matcap: matcapTexture });

    for(let i = 0; i < 200; i++){
      const donut = new THREE.Mesh(donutGeometry, donutMaterial);

      donut.position.x = (Math.random() - 0.5) * 10;
      donut.position.y = (Math.random() - 0.5) * 10;
      donut.position.z = (Math.random() - 0.5) * 10;

      donut.rotation.x = Math.random() * Math.PI;
      donut.rotation.y = Math.random() * Math.PI;

      const scale = Math.random();
      //               x,    y and    z
      donut.scale.set(scale, scale, scale);
      // donut.scale.x = scale;
      // donut.scale.y = scale;
      // donut.scale.z = scale;

      scene.add(donut);
    }
    // console.timeEnd('donuts');
  }
)


/**
 * Object
 */
const cube = new THREE.Mesh(
    new THREE.BoxGeometry(1, 1, 1),
    new THREE.MeshBasicMaterial()
)

// scene.add(cube)

/**
 * Sizes
 */
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}

window.addEventListener('resize', () =>
{
    // Update sizes
    sizes.width = window.innerWidth
    sizes.height = window.innerHeight

    // Update camera
    camera.aspect = sizes.width / sizes.height
    camera.updateProjectionMatrix()

    // Update renderer
    renderer.setSize(sizes.width, sizes.height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
})

/**
 * Camera
 */
// Base camera
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
camera.position.x = 1
camera.position.y = 1
camera.position.z = 2
scene.add(camera)

// Controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

/**
 * Animate
 */
const clock = new THREE.Clock()

const tick = () =>
{
    const elapsedTime = clock.getElapsedTime()

    // Update controls
    controls.update()

    // Render
    renderer.render(scene, camera)

    // Call tick again on the next frame
    window.requestAnimationFrame(tick)
}

tick()
