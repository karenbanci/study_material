import "./App.css";
import React, { Suspense, useRef, useEffect } from "react";
import { Canvas, useThree, extend } from "react-three-fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader";
import { OrbitControls as ThreeOrbitControls } from "three/examples/jsm/controls/OrbitControls";
import styled from "styled-components";

extend({ ThreeOrbitControls });

function OrbitControls() {
  const {
    camera,
    gl: { domElement },
  } = useThree();

  const controls = useRef();

  useEffect(() => {
    if (controls.current) {
      controls.current.update();
    }
  });

  return <threeOrbitControls ref={controls} args={[camera, domElement]} />;
}

function Model() {
  const { scene } = useThree(); // Use the useThree hook to access the three.js scene

  useEffect(() => {
    const loader = new GLTFLoader();
    const dracoLoader = new DRACOLoader();
    dracoLoader.setDecoderPath("./draco/"); // Adjust path to Draco decoder
    loader.setDRACOLoader(dracoLoader);

    loader.load(
      "/model3d.glb", // Adjust the path as necessary
      (gltf) => {
        scene.add(gltf.scene); // Directly add the loaded scene to the existing scene
      },
      undefined,
      (error) => {
        console.error("An error happened", error);
      }
    );

    // Optionally, return a cleanup function if you want to remove the model when the component unmounts
    return () => {
      /* Perform any cleanup if necessary */
    };
  }, [scene]); // Empty dependency array means this effect runs once on mount

  // No need to return anything since we're directly manipulating the scene
  return null;
}

function App() {
  const SceneConainer = styled.div`
    width: 100%;
    height: 100vh;
    background-color: black;
  `;

  return (
    <SceneConainer>
      <Canvas>
        <Suspense fallback={null}>
          <ambientLight />
          <pointLight position={[10, 10, 10]} />
          <Model />
          <OrbitControls />
        </Suspense>
      </Canvas>
    </SceneConainer>
  );
}

export default App;
