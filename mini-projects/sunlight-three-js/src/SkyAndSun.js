import { useEffect, useMemo } from "react";
import * as THREE from "three";
import { useThree } from "react-three-fiber";
import { Sky } from "three/examples/jsm/objects/Sky.js";
import CalcSunPosition from "./CalcSunPosition";
// import OrbitControls from "./OrbitControls";

// import { useControls } from "leva";

console.log("CalcSunPosition linha 10 SkyANDSun", CalcSunPosition());

function SkyAndSun() {
  const { scene } = useThree(); // Access the Three.js scene object
  // const sky = useRef();

  const sunProperties = {
    turbidity: 10,
    rayleigh: 3,
    mieCoefficient: 0.005,
    mieDirectionalG: 0.7,
    elevation: 2,
    azimuth: 180,
    // exposure: renderer.toneMappingExposure,
  };
  // const sky = new Sky();
  const sky = useMemo(() => new Sky(), []);
  // const sky = new Sky();

  useEffect(() => {
    // Ensure the sky object is only added once
    if (!sky.current) {
      sky.current = new Sky();
      console.log("Sky", sky.current);
      sky.current.scale.setScalar(450000);
      scene.add(sky.current);
    }

    const sunPosition = CalcSunPosition();
    // const sun = new THREE.Vector3();
    let sun = new THREE.Vector3(sunPosition[0], sunPosition[1], sunPosition[2]);
    console.log("linha 40 Sun Position", sun);

    const renderer = new THREE.WebGLRenderer();

    // const camera = new THREE.PerspectiveCamera(
    //   60,
    //   window.innerWidth / window.innerHeight,
    //   100,
    //   2000000
    // );
    // camera.position.set(0, 100, 2000);

    const effectController = {
      turbidity: 10,
      rayleigh: 3,
      mieCoefficient: 0.005,
      mieDirectionalG: 0.7,
      elevation: 2,
      azimuth: 180,
      exposure: renderer.toneMappingExposure,
    };

    const uniforms = sky.material.uniforms;
    uniforms["turbidity"].value = effectController.turbidity;
    uniforms["rayleigh"].value = effectController.rayleigh;
    uniforms["mieCoefficient"].value = effectController.mieCoefficient;
    uniforms["mieDirectionalG"].value = effectController.mieDirectionalG;
    uniforms["sunPosition"].value.copy(sun);

    const phi = THREE.MathUtils.degToRad(90 - effectController.elevation);
    console.log("phi", phi);
    const theta = THREE.MathUtils.degToRad(effectController.azimuth);
    console.log("theta", theta);

    console.log("linha 64", sun.setFromSphericalCoords(1, phi, theta));

    renderer.toneMappingExposure = effectController.exposure;
    // renderer.render(scene);
    // renderer.render(scene, camera);

    // Clean up: Remove the sky from the scene when the component unmounts
    return () => {
      if (sky.current) scene.remove(sky.current);
    };
  }, [sky, scene]);

  return null;
}

export default SkyAndSun;
