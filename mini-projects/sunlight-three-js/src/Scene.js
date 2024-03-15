import React, { Suspense } from "react";
import { Canvas } from "react-three-fiber";
import * as THREE from "three";
import Model from "./Model";
import OrbitControls from "./OrbitControls";
import SkyAndSun from "./SkyAndSun";
import CalcSunPosition from "./CalcSunPosition";

function Scene() {
  // Example sun position calculation (customize as needed)
  // const sunPosition = new THREE.Vector3(100, 100, 100);
  const sunPosition = CalcSunPosition();

  return (
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
        sunPosition={sunPosition}
      />
      <ambientLight intensity={0.1} />
      <Suspense fallback={null}>
        {/* <pointLight position={[10, 10, 10]} /> */}
        <Model />
      </Suspense>
      <OrbitControls />
    </Canvas>
  );
}

export default Scene;
