import { OrbitControls, useGLTF } from "@react-three/drei";
import { Perf } from "r3f-perf";
import {
  Physics,
  RigidBody,
  CuboidCollider,
  CylinderCollider,
  InstancedRigidBodies,
  BallCollider,
} from "@react-three/rapier";
import { useRef, useState, useEffect, useMemo } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

// console.log("Physics", Physics, "RigidBody", RigidBody);

export default function Experience() {
  const [hitSound] = useState(() => new Audio("./hit.mp3"));

  const cube = useRef();
  const twister = useRef();
  const cubes = useRef();

  const cubeJump = () => {
    const mass = cube.current.mass();
    cube.current.applyImpulse({ x: 0, y: 5 * mass, z: 0 });
    cube.current.applyTorqueImpulse({
      x: Math.random() - 0.5,
      y: Math.random() - 0.5,
      z: Math.random() - 0.5,
    });
  };

  // to do to the paralelepipedo rotate
  useFrame((state) => {
    const time = state.clock.getElapsedTime();

    // deixar a rotação mais rapida, multiplica o tempo por qualquer valor
    const eulerRotation = new THREE.Euler(0, time * 3, 0);
    const quaternionRotation = new THREE.Quaternion();
    quaternionRotation.setFromEuler(eulerRotation);
    twister.current.setNextKinematicRotation(quaternionRotation);

    // para girar em torno do eixo central
    // we need an angle and we are going to use the time multiplied by 0.5
    const angle = time * 0.5;
    const x = Math.cos(angle) * 2;
    const z = Math.sin(angle) * 2;
    twister.current.setNextKinematicTranslation({ x: x, y: -0.8, z: z });
  });

  const collisionEnter = () => {
    // console.log("collisionEnter");
    // hitSound.currentTime = 0;
    // hitSound.volume = Math.random();
    // hitSound.play();
  };

  const hamburger = useGLTF("./hamburger.glb");

  const cubesCount = 100;

  // useEffect(() => {
  //   for (let i = 0; i < cubesCount; i++) {
  //     const matrix = new THREE.Matrix4();
  //     // compose tem 3 parametros: posição, rotação e escala
  //     // ótimo para performance
  //     matrix.compose(
  //       new THREE.Vector3(i * 2, 0, 0),
  //       new THREE.Quaternion(),
  //       new THREE.Vector3(1, 1, 1)
  //     );
  //     cubes.current.setMatrixAt(i, matrix);
  //   }
  // }, []);
  // isso é a mesma coisa do código acima <InstancedRigidBodies>

  // useMemo é para memorizar o valor
  const cubeInstances = useMemo(() => {
    const instances = [];

    for (let i = 0; i < cubesCount; i++) {
      instances.push({
        key: "instance_" + i, // key é para o react saber que é um novo objeto
        position: [
          (Math.random() - 0.5) * 8,
          6 + i * 0.2,
          (Math.random() - 0.5) * 8,
        ],
        rotation: [Math.random(), Math.random(), Math.random()],
      });
    }
    return instances;
  }, []);

  return (
    <>
      <Perf position="top-left" />

      <OrbitControls makeDefault />

      <directionalLight castShadow position={[1, 2, 3]} intensity={4.5} />
      <ambientLight intensity={1.5} />

      <Physics debug={false} gravity={[0, -9.08, 0]}>
        {/* --------- Bola --------- */}
        <RigidBody colliders="ball" restitution={0.5}>
          <mesh castShadow position={[-1.5, 2, 0]}>
            <sphereGeometry />
            <meshStandardMaterial color="orange" />
          </mesh>
        </RigidBody>
        {/*  --------- Cubo  --------- */}
        <RigidBody
          ref={cube}
          position={[1.5, 2, 0]}
          gravityScale={1}
          restitution={0} // a peça quica algumas vezes (efeito natural)
          friction={0.7}
          colliders={false}
          // onCollisionEnter={collisionEnter} // quando colidir com algo
          // onCollisionExit={() => console.log("collisionExit")}
          // rapier considera o objeto parado depois de um tempo
          // onSleep={() => console.log("sleep")}
          // onWake={() => console.log("wake")}
        >
          <mesh castShadow onClick={cubeJump}>
            <boxGeometry />
            <meshStandardMaterial color="mediumpurple" />
          </mesh>
          <CuboidCollider mass={2} args={[0.5, 0.5, 0.5]} />
        </RigidBody>

        {/*  --------- Piso  --------- */}
        <RigidBody type="fixed" friction={0.7}>
          <mesh receiveShadow position-y={-1.25}>
            <boxGeometry args={[10, 0.5, 10]} />
            <meshStandardMaterial color="greenyellow" />
          </mesh>
        </RigidBody>

        {/*  --------- Paralelepipedo  --------- */}
        <RigidBody
          ref={twister}
          position={[0, -0.8, 0]}
          friction={0}
          type="kinematicPosition"
        >
          <mesh castShadow scale={[0.4, 0.4, 3]}>
            <boxGeometry />
            <meshStandardMaterial color="red" />
          </mesh>
        </RigidBody>

        {/*  --------- Hamburger  --------- */}
        <RigidBody position={[0, 4, 0]} colliders={false}>
          <primitive object={hamburger.scene} scale={0.25} />
          <CylinderCollider args={[0.5, 1.25]} />
        </RigidBody>

        {/*  --------- Paredes  --------- */}
        <RigidBody type="fixed">
          <CuboidCollider args={[5, 2, 0.5]} position={[0, 1, 5.25]} />
          <CuboidCollider args={[5, 2, 0.5]} position={[0, 1, -5.25]} />
          <CuboidCollider args={[0.5, 2, 5]} position={[5.25, 1, 0]} />
          <CuboidCollider args={[0.5, 2, 5]} position={[-5.25, 1, 0]} />
        </RigidBody>

        {/* quando estamos criando a geometria e declarar o material, tem que setar o arg como null */}
        <InstancedRigidBodies instances={cubeInstances}>
          <instancedMesh ref={cubes} castShadow args={[null, null, cubesCount]}>
            <boxGeometry />
            <meshStandardMaterial color="tomato" />
          </instancedMesh>
        </InstancedRigidBodies>
      </Physics>
    </>
  );
}

/**
 colliders="trimesh" e colliders="hull" não são bons para performance

<RigidBody colliders="trimesh"> -- é para deixar o collider na forma do objeto
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
