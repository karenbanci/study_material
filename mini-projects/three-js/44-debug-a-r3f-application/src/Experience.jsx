import { OrbitControls } from "@react-three/drei";
import { folder, useControls, button } from "leva";
import { Perf } from "r3f-perf";
// import Cube from "./Cube.jsx";

export default function Experience() {
  const { perfVisible } = useControls("perf", {
    perfVisible: true,
  });

  const { position, color, visible, sphereScale } = useControls("sphere", {
    position: {
      value: {
        x: -2,
        y: 0,
      },
      // min: -4,
      // max: 4,
      step: 0.1,
      joystick: "invertY",
    },
    color: "#6b97a0",
    visible: true,
    myInterval: {
      value: [4, 5],
      min: 0,
      max: 10,
    },
    clickMe: button(() => console.log("clicked")),
    choice: { options: ["a", "b", "c"] },
  });

  const { cubeScale } = useControls("cube", {
    scale: {
      value: 1,
      min: 0.1,
      max: 2,
      step: 0.1,
      joystick: "invertY",
    },
  });

  return (
    <>
      {perfVisible ? <Perf position="top-left" /> : null}

      <OrbitControls makeDefault />

      <directionalLight position={[1, 2, 3]} intensity={4.5} />
      <ambientLight intensity={1.5} />

      <mesh position={[position.x, position.y, 0]}>
        <sphereGeometry />
        <meshStandardMaterial color={color} />
      </mesh>

      {/* <Cube scale={2} /> */}
      <mesh position-x={2} scale={cubeScale} visible={visible}>
        <boxGeometry />
        <meshStandardMaterial color="mediumpurple" />
      </mesh>

      <mesh position-y={-1} rotation-x={-Math.PI * 0.5} scale={10}>
        <planeGeometry />
        <meshStandardMaterial color="greenyellow" />
      </mesh>
    </>
  );
}
