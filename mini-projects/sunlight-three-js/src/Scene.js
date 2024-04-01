import Model from "./Model";
import * as THREE from "three";
// import SkyAndSun from "./SkyAndSun";
import { Sky, Plane } from "drei";
import { useHelper } from "drei/misc/useHelper";
import React, { Suspense, useRef } from "react";
import { Canvas } from "react-three-fiber";
import OrbitControls from "./OrbitControls";
import { DirectionalLightHelper } from "three/src/helpers/DirectionalLightHelper";

/*
reference to get the sunlight position:
https://www.suncalc.org
*/

function Scene() {
  function calcPosFromRadians(inclination, azimuth) {
    const array = [];
    // console inclination and azimuth
    console.log("calcPosFromRadians", inclination, azimuth);

    const radius = 100;

    array.push(radius * Math.cos(azimuth) * Math.cos(inclination));
    array.push(radius * Math.sin(inclination));
    array.push(radius * Math.sin(azimuth));

    console.log("calcPosFromAngles", array);

    return array;
  }

  function calcPosFromDegrees(inclination, azimuth) {
    return calcPosFromRadians(
      inclination * (Math.PI / 180),
      azimuth * (Math.PI / 180)
    );
  }

  // inclination and azimuth
  // const calc = calcPosFromDegrees(1.1, 88.35); // 7 am NY time
  // const calc = calcPosFromDegrees(42.3, 136.67); // 11 am NY time
  // const calc = calcPosFromDegrees(48.98, 202.38); // 2 pm NY time
  // const calc = calcPosFromDegrees(34.19, 237.83); // 4 pm NY time
  const calc = calcPosFromDegrees(13.01, 261.19); // 6 pm NY time

  // var csv = "";

  // for (var i = 0; i < 360; i += 10) {
  //   for (var j = 0; j < 180; j += 10) {
  //     csv += i + "," + j + ",";
  //     csv +=
  //       calcPosFromDegrees(j, i).x +
  //       "," +
  //       calcPosFromDegrees(j, i).y +
  //       "," +
  //       calcPosFromDegrees(j, i).z +
  //       "\n";
  //   }
  // }

  // console.log(csv);

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas shadowMap camera={{ position: [100, 50, 100], fov: 50 }}>
        <Sky distance={45000} sunPosition={calc} />

        <OrbitControls
          minAzimuthAngle={-Math.PI / 4}
          maxAzimuthAngle={Math.PI / 4}
          minPolarAngle={Math.PI / 6}
          maxPolarAngle={Math.PI - Math.PI / 6}
        />
        <Suspense fallback={null}>
          <ambientLight intensity={0.7} />
          <DirectionalLightWithHelper calc={calc} />
          <Model />
          {/* Plane just to see the shadow - I will remove it later */}
          <Plane
            receiveShadow // highlight-line
            rotation={[-Math.PI / 2, 0, 0]}
            position={[0, -0.1, 0]}
            args={[100, 100]}
          >
            <meshStandardMaterial attach="material" color="white" />
          </Plane>
        </Suspense>
      </Canvas>
    </div>
  );
}

function DirectionalLightWithHelper(calc) {
  console.log("DirectionalLightWithHelper", calc);
  // helpers
  const directionalLightRef = useRef();
  useHelper(directionalLightRef, DirectionalLightHelper, 1, "red");

  return (
    <directionalLight
      ref={directionalLightRef}
      intensity={0.5}
      castShadow // highlight-line
      shadow-mapSize-height={512}
      shadow-mapSize-width={512}
      position={calc}
    />
  );
}

export default Scene;
