import { useKeyboardControls } from "@react-three/drei";
import useGame from "./stores/useGame.jsx";
import { useRef, useEffect } from "react";
import { addEffect } from "@react-three/fiber";

export default function Interface() {
  const time = useRef();

  const restart = useGame((state) => state.restart);
  const phase = useGame((state) => state.phase);

  // re-render the component when the time changes

  // access the controls state
  const forward = useKeyboardControls((state) => state.forward);
  const leftward = useKeyboardControls((state) => state.leftward);
  const backward = useKeyboardControls((state) => state.backward);
  const rightward = useKeyboardControls((state) => state.rightward);
  const jump = useKeyboardControls((state) => state.jump);

  useEffect(() => {
    const unsubscribeEffect = addEffect(() => {
      const state = useGame.getState();
      // console.log(state);

      let elapsedTime = 0;

      // se o jogo estiver rodando
      if (state.phase === "playing") {
        elapsedTime = Date.now() - state.startTime;
        // se o jogo estiver finalizado, mostra o tempo total
      } else if (state.phase === "ended") {
        elapsedTime = state.endTime - state.startTime;
      }

      // convert to seconds
      elapsedTime /= 1000;
      // console.log(elapsedTime);
      elapsedTime = elapsedTime.toFixed(2);
      if (time.current) time.current.textContent = elapsedTime;

      // console.log(elapsedTime);
    });

    return () => {
      unsubscribeEffect();
    };
  }, []);

  return (
    <div className="interface">
      {/* Time */}
      <div ref={time} className="time">
        0.00
      </div>

      {/*  Interface */}
      {phase === "ended" && (
        <div className="restart" onClick={restart}>
          Restart
        </div>
      )}

      {/* Controls */}
      <div className="controls">
        <div className="raw">
          <div className={`key ${forward ? "active" : ""}`}></div>
        </div>
        <div className="raw">
          <div className={`key ${leftward ? "active" : ""}`}></div>
          <div className={`key ${backward ? "active" : ""}`}></div>
          <div className={`key ${rightward ? "active" : ""}`}></div>
        </div>
        <div className="raw">
          <div className={`key large ${jump ? "active" : ""}`}></div>
        </div>
      </div>
    </div>
  );
}
