import "./style.css";
import ReactDOM from "react-dom/client";
import { Canvas } from "@react-three/fiber";
import Experience from "./Experience.jsx";
// import * as THREE from "three";

const root = ReactDOM.createRoot(document.querySelector("#root"));

// const created = ({ gl, scene }) => {
//   // console.log(gl);
//   // gl.setClearColor("#ff0000", 1);
//   // console.log(scene);
//   scene.background = new THREE.Color("#ff0000");
// };

root.render(
  <Canvas
    shadows={false}
    camera={{
      fov: 45,
      near: 0.1,
      far: 200,
      position: [-4, 3, 6],
    }}
    // onCreated={created}
  >
    {/* create a color inside the canvas */}
    {/* <color args={["#ff0000"]} attach="background" /> */}
    <Experience />
  </Canvas>
);
