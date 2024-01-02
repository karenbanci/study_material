import { useRef } from "react";
import { useFrame } from "@react-three/fiber";

export default function Lights() {
  const light = useRef();

  // state argument to access to the camera
  useFrame((state) => {
    // -4 to move the light in front of the camera
    light.current.position.z = state.camera.position.z + 1 - 4;
    // to update the target position
    light.current.target.position.z = state.camera.position.z - 4;

    // update the matrix world to update the position camera and lights
    light.current.target.updateMatrixWorld();
  });

  return (
    <>
      <directionalLight
        ref={light}
        castShadow
        position={[4, 4, 1]}
        intensity={4.5}
        shadow-mapSize={[1024, 1024]}
        shadow-camera-near={1}
        shadow-camera-far={10}
        shadow-camera-top={10}
        shadow-camera-right={10}
        shadow-camera-bottom={-10}
        shadow-camera-left={-10}
      />
      <ambientLight intensity={1.5} />
    </>
  );
}
