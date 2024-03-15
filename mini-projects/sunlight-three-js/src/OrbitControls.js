import { OrbitControls as ThreeOrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { useThree, extend } from "react-three-fiber";
import React, { useRef, useEffect } from "react";

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

export default OrbitControls;
