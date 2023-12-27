import { OrbitControls } from "@react-three/drei";
import {
  EffectComposer,
  Vignette,
  ToneMapping,
  Glitch,
  Noise,
  Bloom,
  DepthOfField,
} from "@react-three/postprocessing";
import { Perf } from "r3f-perf";
import { BlendFunction, GlitchMode } from "postprocessing";
import Drunk from "./Drunk.jsx";
import { useRef } from "react";
import { useControls } from "leva";

// console.log(BlendFunction);
// console.log(GlitchMode);

export default function Experience() {
  const drunkRef = useRef();

  const drunkProps = useControls("Drunk Effect", {
    frequency: {
      value: 2,
      min: 1,
      max: 20,
    },
    amplitude: {
      value: 0.1,
      min: 0,
      max: 1,
    },
  });

  return (
    <>
      {/* add color to background because Vignette will be applied in the all screen*/}
      <color args={["#ffffff"]} attach="background" />

      <EffectComposer disableNormalPass>
        {/* <Vignette
          offset={0.3}
          darkness={0.9}
          blendFunction={BlendFunction.NORMAL}
        /> */}
        {/* <Glitch
          delay={[0.5, 1]}
          duration={[0.1, 0.3]}
          strength={[0.02, 0.04]}
          mode={GlitchMode.CONSTANT_WILD}
        /> */}
        {/* <Noise premultiply blendFunction={BlendFunction.SOFT_LIGHT} /> */}
        {/* <Bloom intensity={0.1} luminanceThreshold={0} mipmapBlur /> */}
        {/* <DepthOfField
          focusDistance={0.025}
          focalLength={0.025}
          bokehScale={6}
        /> */}
        {/* <ToneMapping /> */}
        <Drunk ref={drunkRef} {...drunkProps} />
      </EffectComposer>

      <Perf position="top-left" />

      <OrbitControls makeDefault />

      <directionalLight castShadow position={[1, 2, 3]} intensity={4.5} />
      <ambientLight intensity={1.5} />

      <mesh castShadow position-x={-2}>
        <sphereGeometry />
        <meshStandardMaterial color="orange" />
      </mesh>

      <mesh castShadow position-x={2} scale={1.5}>
        <boxGeometry />
        <meshStandardMaterial color="mediumpurple" />
      </mesh>

      <mesh
        receiveShadow
        position-y={-1}
        rotation-x={-Math.PI * 0.5}
        scale={10}
      >
        <planeGeometry />
        <meshStandardMaterial color="greenyellow" />
      </mesh>
    </>
  );
}

/*
Vignette - escurece as bordas da tela
  - offset - tamanho do escurecimento
  - darkness - quanto mais alto, mais escuro
  - blendFunction - tipo de blend

Glitch - efeito de glitch - tipo a tela bugando
  - delay - tempo de delay para o glitch
  - duration - tempo de duração do glitch
  - strength - força do glitch
  - mode - tipo de glitch

Noise - adiciona ruido na tela - tipo tv antiga
  - premultiply - se o ruido vai ser multiplicado pela cor do pixel
  - blendFunction - tipo de blend

Bloom - efeito de brilho
  - luminanceThreshold - quanto mais alto, mais brilho
  - mipmapBlur - quanto mais alto, mais borrado - efeito de jogo
  exemplo de cor: color={[1.5, 1, 4]}
  <MeshStandardMaterial
    color="white"
    emissive="blue"
    emissiveIntensity={1}
    toneMapped={false}/>

DepthOfField - efeito de desfoque - não é tão bom para performance
  - focusDistance - distancia do foco
  - focalLength - tamanho do foco
  - bokehScale - tamanho do desfoque
*/
