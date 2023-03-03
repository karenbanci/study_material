import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'

/**
 * Base
 */
// Canvas
const canvas = document.querySelector('canvas.webgl')

// Scene
const scene = new THREE.Scene()

// Object
// const geometry = new THREE.BoxGeometry(1, 1, 1, 2, 2, 2)
const geometry = new THREE.BufferGeometry();

const count = 50;
// Float32Array é um array de 32 bits
const positionsArray = new Float32Array(count * 3 * 3);

// iterando sobre o array,
for(let i = 0; i < count * 3 * 3; i++) {
  positionsArray[i] = Math.random();
}
const positionsAttribute = new THREE.BufferAttribute(positionsArray, 3);
geometry.setAttribute('position', positionsAttribute);

const material = new THREE.MeshBasicMaterial({
  color: 0xff0000,
  // wireframe posso ver os a linha dos triangulos
  wireframe: true,
});

const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);


/*
//  Floar32Array é um array de 32 bits
//  usei o Float32Array para criar um array de 9 posições
const positionsArray = new Float32Array([
  // x, y, z
  0,0,0,
  0,1,0,
  1,0,0
])

// BufferGeometry é uma geometria que não é renderizada diretamente
// 3 é o numero de elementos que cada vertice tem
const positionsAttribute = new THREE.BufferAttribute(positionsArray, 3)

const geometry = new THREE.BufferGeometry()
//  string porque é um atributo do bufferGeometry
geometry.setAttribute('position', positionsAttribute)
*/

// Sizes
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

// Camera
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
camera.position.z = 3
scene.add(camera)

// Controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true

// Renderer
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

// Animate
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
