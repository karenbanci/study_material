import { useEffect, useMemo } from "react";
import * as THREE from "three";
import { useThree } from "react-three-fiber";
import { Sky } from "three/examples/jsm/objects/Sky.js";
import CalcSunPosition from "./CalcSunPosition";
// import OrbitControls from "./OrbitControls";

// import { useControls } from "leva";

console.log("CalcSunPosition", CalcSunPosition());

function SkyAndSun({ turbidity, rayleigh, mieCoefficient, mieDirectionalG }) {
  const { scene } = useThree(); // Access the Three.js scene object
  // const sky = useRef();

  // const sky = new Sky();
  const sky = useMemo(() => new Sky(), []);

  useEffect(() => {
    // Ensure the sky object is only added once
    if (!sky.current) {
      sky.current = new Sky();
      sky.current.scale.setScalar(450000);
      scene.add(sky.current);
    }

    const sunPosition = CalcSunPosition();
    const sun = new THREE.Vector3(...sunPosition);
    console.log("Sun Position", sun);

    const uniforms = sky.current.material.uniforms;
    uniforms["turbidity"].value = turbidity;
    uniforms["rayleigh"].value = rayleigh;
    uniforms["mieCoefficient"].value = mieCoefficient;
    uniforms["mieDirectionalG"].value = mieDirectionalG;
    uniforms["sunPosition"].value = sun;

    // Clean up: Remove the sky from the scene when the component unmounts
    return () => {
      if (sky.current) scene.remove(sky.current);
    };
  }, [sky, scene, turbidity, rayleigh, mieCoefficient, mieDirectionalG]);

  return null;
}

export default SkyAndSun;
