import { useEffect, useRef } from "react";
import { useThree } from "react-three-fiber";
import { Sky } from "three/examples/jsm/objects/Sky.js";
import CalcSunPosition from "./CalcSunPosition";

console.log("CalcSunPosition", CalcSunPosition());

function SkyAndSun({
  turbidity,
  rayleigh,
  mieCoefficient,
  mieDirectionalG,
  sunPosition,
}) {
  const { scene } = useThree(); // Access the Three.js scene object
  const sky = useRef();

  // Assuming CalcSunPosition returns an array [x, y, z] for the sun's position
  // const sunPosition = CalcSunPosition();
  // console.log("Sun Position", sunPosition);

  useEffect(() => {
    // Ensure the sky object is only added once
    if (!sky.current) {
      sky.current = new Sky();
      sky.current.scale.setScalar(450000);
      scene.add(sky.current);
    }

    const uniforms = sky.current.material.uniforms;
    uniforms["turbidity"].value = turbidity;
    uniforms["rayleigh"].value = rayleigh;
    uniforms["mieCoefficient"].value = mieCoefficient;
    uniforms["mieDirectionalG"].value = mieDirectionalG;
    uniforms["sunPosition"].value.set(...sunPosition);

    // Clean up: Remove the sky from the scene when the component unmounts
    return () => {
      if (sky.current) scene.remove(sky.current);
    };
  }, [
    scene,
    turbidity,
    rayleigh,
    mieCoefficient,
    mieDirectionalG,
    sunPosition,
  ]); // Add sunPosition to dependency array

  //mrdoob/three.js/examples/webgl_shaders_sky.html

  // No need to return anything since the sky is being added directly to the scene
  return null;
}

export default SkyAndSun;
