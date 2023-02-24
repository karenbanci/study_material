import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'


/**
 * Cursor
 */
const cursor = {
  x: 0,
  y: 0
}
window.addEventListener('mousemove', (event) => {
  cursor.x = event.clientX / sizes.width - 0.5
  cursor.y = - (event.clientY / sizes.height - 0.5)
})

/**
 * Base
 */
// Canvas
const canvas = document.querySelector('canvas.webgl')

// Sizes
const sizes = {
    width: 800,
    height: 600
}

// Scene
const scene = new THREE.Scene()

// Object
const mesh = new THREE.Mesh(
    new THREE.BoxGeometry(1, 1, 1, 5, 5, 5),
    new THREE.MeshBasicMaterial({ color: 0xff0000 })
)
scene.add(mesh)

// Camera
//                                    fiel of view, aspect ratio, near, far
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
// optional
// aspect ratio is the ratio between the width and the height of the camera
// const aspectRatio = sizes.width / sizes.height
// console.log(aspectRatio)
// // OrthographicCamera(left, right, top, bottom, near, far)
// const camera = new THREE.OrthographicCamera(
//   -1 * aspectRatio,
//   1 * aspectRatio,
//   1,
//   -1,
//   0.1,
//   100
// );
// camera.position.x = 2
// camera.position.y = 2
camera.position.z = 3
camera.lookAt(mesh.position)
scene.add(camera)

// Controls
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;
// controls.target.y = 2;
// controls.update();

// near and far, correspond to how close and how far the camera can see
// objects outside of this range will not be rendered


// Renderer
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)

// Animate
const clock = new THREE.Clock()

const tick = () =>
{
    // const elapsedTime = clock.getElapsedTime()

    // // Update objects  - animation
    // mesh.rotation.y = elapsedTime;

    // Update Camera - toda vez que eu passar o mouse, a camera vai se mover
    // camera.position.x = Math.sin(cursor.x * Math.PI * 2) * 3;
    // camera.position.z = Math.cos(cursor.x * Math.PI * 2) * 3;
    // camera.position.y = cursor.y * 5;
    // camera.lookAt(mesh.position)

    // Update controls
    controls.update();


    // Render
    renderer.render(scene, camera)

    // Call tick again on the next frame
    window.requestAnimationFrame(tick)
}

tick()
