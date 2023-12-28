import { OrbitControls } from "@react-three/drei";
import { Perf } from "r3f-perf";
import {
  Physics,
  RigidBody,
  CuboidCollider,
  BallCollider,
} from "@react-three/rapier";
import { useRef } from "react";

// console.log("Physics", Physics, "RigidBody", RigidBody);

export default function Experience() {
  const cube = useRef();

  const cubeJump = () => {
    cube.current.applyImpulse({ x: 0, y: 5, z: 0 });
    cube.current.applyTorqueImpulse({
      x: Math.random() - 0.5,
      y: Math.random() - 0.5,
      z: Math.random() - 0.5,
    });
  };

  return (
    <>
      <Perf position="top-left" />

      <OrbitControls makeDefault />

      <directionalLight castShadow position={[1, 2, 3]} intensity={4.5} />
      <ambientLight intensity={1.5} />

      <Physics debug gravity={[0, -9.08, 0]}>
        {/* --------- Bola --------- */}
        <RigidBody colliders="ball">
          <mesh castShadow position={[-1.5, 2, 0]}>
            <sphereGeometry />
            <meshStandardMaterial color="orange" />
          </mesh>
        </RigidBody>

        {/*  --------- Cubo  --------- */}
        <RigidBody ref={cube} position={[1.5, 2, 0]} gravityScale={1}>
          <mesh castShadow onClick={cubeJump}>
            <boxGeometry />
            <meshStandardMaterial color="mediumpurple" />
          </mesh>
        </RigidBody>

        {/*  --------- Piso  --------- */}
        <RigidBody type="fixed">
          <mesh receiveShadow position-y={-1.25}>
            <boxGeometry args={[10, 0.5, 10]} />
            <meshStandardMaterial color="greenyellow" />
          </mesh>
        </RigidBody>
      </Physics>
    </>
  );
}

/**
<RigidBody colliders="trimesh"> -- é para deixar o collider na forma do torus
  <mesh
    castShadow
    position={[0, 1, -0.25]}
    rotation={[Math.PI * 0.5, 0, 0]}
  >
    <torusGeometry args={[1, 0.5, 16, 32]} />
    <meshStandardMaterial color="mediumpurple" />
  </mesh>
</RigidBody>

  -- pesquisar mais sobre o colliders
BallCollider https://rapier.rs/javascript3d/classes/Ball.html
CuboidCollider https://rapier.rs/javascript3d/classes/Cuboid.html
RoundCuboidCollider https://rapier.rs/javascript3d/classes/RoundCuboid.html
CapsuleCollider https://rapier.rs/javascript3d/classes/Capsule.html
ConeCollider https://rapier.rs/javascript3d/classes/Cone.html
CylinderCollider https://rapier.rs/javascript3d/classes/Cylinder.html
ConvexHullCollider https://rapier.rs/javascript3d/classes/ConvexPolyhedron.html
TrimeshCollider https://rapier.rs/javascript3d/classes/TriMesh.html
HeightfieldCollider https://rapier.rs/javascript3d/classes/Heightfield.html

------- Torus Geometry -------
<CuboidCollider args={[1.5, 1.5, 0.5]} />
  <CuboidCollider
    args={[0.25, 1, 0.25]}
    position={[0, 0, 1]}
    rotation={[-Math.PI * 0.35, 0, 0]}

Donuts
        <RigidBody
          colliders={false}
          position={[0, 1, -0.25]}
          rotation={[Math.PI * 0.5, 0, 0]}
        >
          <BallCollider args={[1.5]} />
          <mesh castShadow>
            <torusGeometry args={[1, 0.5, 16, 32]} />
            <meshStandardMaterial color="mediumpurple" />
          </mesh>
        </RigidBody>
/>

------------- LINKS -------------
https://rapier.rs/javascript3d/classes/RoundCuboid.html
https://rapier.rs/javascript3d/classes/RigidBody.html
*/
