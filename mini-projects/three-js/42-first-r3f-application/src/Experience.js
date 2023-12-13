import { extend, useFrame, useThree } from "@react-three/fiber";
import { useRef } from "react";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import CustomObject from "./CustomObject";

extend({ OrbitControls });

export default function Experience() {
  const { camera, gl } = useThree();

  // create a reference to the mesh - it will allow us to access the mesh properties
  const cubeRef = useRef();
  const groupRef = useRef();

  // it call each frame to render - animate frame works well here
  useFrame((state, delta) => {
    // state.camera.position.x += delta; // => it will move the camera

    // => it will return the time in seconds since the clock started
    // const angle = state.clock.getElapsedTime();
    // state.camera.position.x = Math.sin(angle) * 8;
    // state.camera.position.z = Math.cos(angle) * 8;
    // => it will make the camera look at the center of the scene
    // state.camera.lookAt(0, 0, 0);

    cubeRef.current.rotation.y += 0.01;
    // groupRef.current.rotation.y += delta;
  });

  return (
    <>
      {/* rotate camera */}
      <orbitControls args={[camera, gl.domElement]} />

      <directionalLight position={[1, 2, 3]} intensity={4.5} />
      <ambientLight intensity={1.5} />

      <group ref={groupRef}>
        <mesh position-x={-2}>
          <sphereGeometry args={[1.5, 32, 32]} />
          <meshStandardMaterial color="orange" />
        </mesh>

        <mesh
          ref={cubeRef}
          rotation-y={Math.PI * 0.25}
          position-x={2}
          scale={1.5}
        >
          <boxGeometry scale={1.5} />
          <meshStandardMaterial color="mediumpurple" />
        </mesh>
      </group>

      <mesh position-y={-1} rotation-x={-Math.PI * 0.5} scale={10}>
        <planeGeometry />
        <meshStandardMaterial color="greenyellow" />
      </mesh>

      <CustomObject />
    </>
  );
}

/**
     Notes:
   UseFrame Hook
   state: contains information about 3JS environment like camera, scene, etc.
   delta: time in seconds since the last frame
   */
