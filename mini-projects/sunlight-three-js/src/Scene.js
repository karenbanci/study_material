import Model from "./Model";
import * as THREE from "three";
import SkyAndSun from "./SkyAndSun";
import React, { Suspense } from "react";
import { Canvas } from "react-three-fiber";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
// import OrbitControls from "./OrbitControls";

// import CalcSunPosition from "./CalcSunPosition";

// console.log("Model", Model);

function Scene() {
  // Example sun position calculation (customize as needed)
  // const sunPosition = new THREE.Vector3(100, 100, 100);
  // const sunPosition = CalcSunPosition();

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas
        camera={{ position: [0, 100, 2000], fov: 60 }}
        onCreated={({ gl }) => {
          gl.toneMapping = THREE.ACESFilmicToneMapping;
          gl.toneMappingExposure = 0.5;
        }}
      >
        <SkyAndSun
          turbidity={10}
          rayleigh={2}
          mieCoefficient={0.005}
          mieDirectionalG={0.7}
          // sunPosition={sunPosition}
        />
        <ambientLight intensity={0.1} />
        <Suspense fallback={null}>
          {/* <pointLight position={[10, 10, 10]} /> */}
          <Model />
        </Suspense>
        <OrbitControls
          minAzimuthAngle={-Math.PI / 4}
          maxAzimuthAngle={Math.PI / 4}
          minPolarAngle={Math.PI / 6}
          maxPolarAngle={Math.PI - Math.PI / 6}
        />
      </Canvas>
    </div>
  );
}

export default Scene;
