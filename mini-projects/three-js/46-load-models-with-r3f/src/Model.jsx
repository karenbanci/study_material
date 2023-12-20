import { useGLTF, Clone } from "@react-three/drei";

export default function Model() {
  const model = useGLTF("./hamburger-draco.glb");
  // console.log(model);

  return (
    <>
      <Clone object={model.scene} scale={0.35} position-x={-4} />;
      <Clone object={model.scene} scale={0.35} position-x={0} />
      <Clone object={model.scene} scale={0.35} position-x={4} />
    </>
  );
}

// it will load the model and cache it for future use.
useGLTF.preload("./hamburger-draco.glb");

/**
 alternativa para carregar imagem

import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader";

 const model = useLoader(GLTFLoader, "./hamburger-draco.glb", (loader) => {
    const dracoLoader = new DRACOLoader();
    dracoLoader.setDecoderPath("./draco/");
    loader.setDRACOLoader(dracoLoader);
  });

  Clone is a helper component that clones a given object and all its children.
 */
