
//  Scene
const scene = new THREE.Scene();

//  Red cube
const geometry = new THREE.BoxGeometry(1, 1, 1);
// posso escrever o nome da cor dentro da string se eu não souber o hexadecimal
const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);


//  Sizes
const sizes = {
  width: 800,
  height: 600
}

// Camera
/*
PerspectiveCamera( fov : Number, aspect : Number, near : Number, far : Number )
fov — Camera frustum vertical field of view.
aspect — Camera frustum aspect ratio.
near — Camera frustum near plane.
far — Camera frustum far plane.
*/
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height);
camera.position.z = 3; // ajusta a posição da camera
scene.add(camera);

// Renderer
const canvas = document.querySelector(".webgl");
console.log(canvas)
const renderer = new THREE.WebGLRenderer({
  canvas: canvas
});
renderer.setSize(sizes.width, sizes.height);

renderer.render(scene, camera);
