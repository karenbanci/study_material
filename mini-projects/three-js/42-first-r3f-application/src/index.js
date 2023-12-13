import "./style.css";
import ReactDOM from "react-dom/client";
import { Canvas } from "@react-three/fiber";
import Experience from "./Experience.js";
import * as THREE from "three";

const root = ReactDOM.createRoot(document.querySelector("#root"));

const cameraSettings = {
  fov: 45,
  // zoom: 100,
  near: 0.1,
  far: 200,
  position: [3, 2, 6],
};

root.render(
  <Canvas
    // flat // flat makes colors like HDR - it is default color
    // dpr={[1, 2]} // dpr is device pixel ratio - good for performance
    gl={{
      antialias: true,
      toneMapping: THREE.ACESFilmicToneMapping,
      outputColorSpace: THREE.SRGBColorSpace,
    }}
    camera={cameraSettings}
    // orthographic
  >
    <Experience />
  </Canvas>
);
