// import * as THREE from "three";
import { useEffect, useState } from "react";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader";
import React from "react";

function Model() {
  // const { scene } = useThree(); // Use the useThree hook to access the three.js scene

  const [scene, setScene] = useState(null);
  const model = "/portal.glb";

  const createScene = (gltfScene) => {
    // Config Scale
    gltfScene.scale.set(1.5, 1.5, 1.5);
    gltfScene.scale.multiplyScalar(10);

    return gltfScene;
  };

  useEffect(() => {
    if (model) {
      const loader = new GLTFLoader();
      const dracoLoader = new DRACOLoader();
      dracoLoader.setDecoderPath("./draco/");
      loader.setDRACOLoader(dracoLoader);

      loader.load(
        model,
        (gltf) => {
          // setModel(gltf.scene);

          setScene(createScene(gltf.scene));
        },
        undefined,
        (error) => {
          console.error(error);
        }
      );
    }
  }, [model]);

  if (!scene) return null;
  return <primitive object={scene} />;
}

export default Model;
