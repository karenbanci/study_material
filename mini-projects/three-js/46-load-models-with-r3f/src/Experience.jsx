import { OrbitControls } from "@react-three/drei";
import { Perf } from "r3f-perf";
import { Suspense } from "react";
import Placeholder from "./Placeholder";
import Hamburger from "./Hamburger";
import Model from "./Model";
import Fox from "./Fox";

export default function Experience() {
  return (
    <>
      <Perf position="top-left" />

      <OrbitControls makeDefault />

      <directionalLight
        castShadow
        position={[1, 2, 3]}
        intensity={4.5}
        shadow-normalBias={0.04} // remover as fissuras da imagem
      />
      <ambientLight intensity={1.5} />

      <mesh
        receiveShadow
        position-y={-1}
        rotation-x={-Math.PI * 0.5}
        scale={10}
      >
        <planeGeometry />
        <meshStandardMaterial color="greenyellow" />
      </mesh>
      <Suspense fallback={<Placeholder position-y={0.5} scale={[2, 3, 2]} />}>
        <Hamburger scale={0.35} />
      </Suspense>

      <Fox />
    </>
  );
}

/* Suspense permite que a página seja carregada e depois carrega a imagem,
para o usuário não ficar esperando a imagem carregar e ficar olhando para
tela branca.

Suspense uses fallback, is what the user will see if the component is not ready.
You can put the spinner there, or a placeholder image, or whatever you want. (loading...)

criar o Placeholder.jsx para colocar o objeto que vai aparecer enquanto a imagem não carrega.
*/
