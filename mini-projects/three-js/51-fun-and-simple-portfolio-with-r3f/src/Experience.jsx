import {
  useGLTF,
  Environment,
  Float,
  PresentationControls,
  ContactShadows,
  Html,
  Text,
} from "@react-three/drei";

export default function Experience() {
  const computer = useGLTF(
    "https://threejs-journey.com/resources/models/macbook_model.gltf"
  );

  return (
    <>
      <color args={["#192634"]} attach={"background"} />

      <Environment preset="city" />

      <PresentationControls
        global
        rotation={[0.13, 0.1, 0]}
        polar={[-0.4, 0.2]}
        azimuth={[-1, 0.75]}
        config={{ mass: 2, tension: 400 }}
        snap={{ mass: 4, tension: 400 }}
      >
        <Float rotationIntensity={0.4}>
          {/* Lights */}
          <rectAreaLight
            width={2.5}
            height={1.65}
            intensity={65}
            color="#70757b"
            rotation={[-0.1, Math.PI, 0]}
            position={[0, 0.55, -1.15]}
          />

          {/* Laptop */}
          <primitive object={computer.scene} position-y={-1.2}>
            <Html
              transform
              wrapperClass="htmlScreen"
              distanceFactor={1.17}
              position={[0, 1.56, -1.4]}
              rotation-x={-0.256}
            >
              <iframe src="https://karenhb.com/" />
            </Html>
          </primitive>

          {/* Title */}
          <Text
            font={"./Lobster/Lobster-Regular.ttf"}
            fontSize={0.7}
            position={[2, 0.75, 0.75]}
            rotation-y={-1.25}
            maxWidth={2}
            textAlign="center"
            color={"#ffffff"}
          >
            Karen Honorio
          </Text>
          <Text
            font={"./Lobster/Lobster-Regular.ttf"}
            fontSize={0.3}
            position={[2, -0.3, 0.75]}
            rotation-y={-1.25}
            maxWidth={2}
            textAlign="center"
            color={"#56d5e0"}
            onClick={() =>
              (window.location.href = "https://karenbanci.github.io/")
            }
          >
            Portifolio
          </Text>
        </Float>
      </PresentationControls>

      <ContactShadows position-y={-1.4} opacity={0.4} scale={5} blur={2} />
    </>
  );
}

/**
 * Environment será responsável por adicionar um ambiente ao nosso projeto.
 */
