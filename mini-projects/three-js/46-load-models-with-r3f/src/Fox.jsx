import { useGLTF, useAnimations } from "@react-three/drei";
import { useEffect } from "react";
import { useControls } from "leva";

export default function Fox() {
  const fox = useGLTF("./Fox/glTF/Fox.gltf");

  const animations = useAnimations(fox.animations, fox.scene);

  const { animationName } = useControls({
    animationName: {
      options: animations.names,
    },
  });

  useEffect(() => {
    const action = animations.actions[animationName];
    action.fadeIn(0.5).play();

    return () => {
      action.reset().fadeOut(0.5).play();
    };
  }, [animationName]);

  return (
    <primitive
      object={fox.scene}
      scale={0.02}
      position={[-2.5, 0, 2.5]}
      rotation-y={0.3}
    />
  );
}

/**
outra opção:
assim que carrega a página, a raposa começa a correr, 2s depois ela começa a andar

  useEffect(() => {
    const action = animations.actions.Run;
    action.play();

    // start the walk animation after 2 seconds
    window.setTimeout(() => {
      animations.actions.Walk.play();
      // crossFadeFrom: animação que vai ser substituida, tempo de transição
      animations.actions.Walk.crossFadeFrom(animations.actions.Run, 1);
    }, 2000);
  }, []);

 */
