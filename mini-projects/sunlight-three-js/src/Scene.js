import Model from "./Model";
import * as THREE from "three";
// import SkyAndSun from "./SkyAndSun";
import { Sky, Plane } from "drei";
import React, { Suspense } from "react";
import { Canvas } from "react-three-fiber";
import OrbitControls from "./OrbitControls";

function Scene() {
  function calcPosFromRadians(
    inclination,
    azimuth,
    vector = new THREE.Vector3()
  ) {
    // console inclination and azimuth
    console.log("calcPosFromRadians", inclination, azimuth);
    // const theta = Math.PI * (inclination - 0.5);
    // const phi = 2 * Math.PI * (azimuth - 0.5);

    // vector.x = Math.cos(phi) * 1;
    // vector.y = Math.sin(theta) * 1;
    // vector.z = Math.sin(phi) * 1;

    const radius = 1;
    vector.x = radius * Math.cos(azimuth) * Math.cos(inclination);
    vector.y = radius * Math.cos(azimuth) * Math.sin(inclination);
    vector.z = radius * Math.sin(azimuth);

    console.log("calcPosFromAngles", vector);

    return vector;
  }

  function calcPosFromDegrees(inclination, azimuth) {
    return calcPosFromRadians(
      inclination * (Math.PI / 180),
      azimuth * (Math.PI / 180)
    );
  }

  // TODO: TEMOS QUE ARRUMAR A POSIÇAO, NAO ESTÁ FUNCIONANDO CORRETAMENTE OS VALORES
  // altitud and azimuth
  const calc = calcPosFromDegrees(0, 270);
  // 0
  // Vector3 {x: 0.62968172529648, y: 0, z: 0.7768532196159377}
  // 0 (-0.5)
  // calcPosFromAngles Vector3 {x: -0.6296817252964799, y: -1, z: -0.7768532196159378}

  // 10
  // Vector3 {x: 0.62968172529648, y: 0.5212468736421765, z: 0.7768532196159377}

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas shadowMap camera={{ position: [100, 50, 100], fov: 50 }}>
        <Sky distance={45000} sunPosition={[calc.x, calc.y, calc.z]} />

        <OrbitControls
          minAzimuthAngle={-Math.PI / 4}
          maxAzimuthAngle={Math.PI / 4}
          minPolarAngle={Math.PI / 6}
          maxPolarAngle={Math.PI - Math.PI / 6}
        />
        <Suspense fallback={null}>
          <ambientLight intensity={0.7} />
          <directionalLight
            intensity={0.5}
            castShadow // highlight-line
            shadow-mapSize-height={512}
            shadow-mapSize-width={512}
            position={[calc.x, calc.y, calc.z]}
          />
          <Model />
          {/* <Plane
            receiveShadow // highlight-line
            rotation={[-Math.PI / 2, 0, 0]}
            position={[0, -10, 0]}
            args={[100, 100]}
          >
            <meshStandardMaterial attach="material" color="white" />
          </Plane> */}
        </Suspense>
      </Canvas>
    </div>
  );
}

export default Scene;
