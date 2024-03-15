import { useEffect } from "react";
import { useThree } from "react-three-fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader";

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

export default Model;
