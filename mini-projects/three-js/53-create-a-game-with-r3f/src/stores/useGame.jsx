import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

// it will be like a react hook
export default create(
  // we need subscribeWithSelector to be able to replace the state
  subscribeWithSelector((set) => {
    return {
      blocksCount: 5,
      blocksSeed: 0, // random levels

      startTime: 0,
      endTime: 0,

      // Phases
      phase: "ready",

      start: () => {
        // we want to replace the phase property
        set((state) => {
          if (state.phase === "ready") {
            // start time will be saved when the phase changes to playing
            return { phase: "playing", starttime: Date.now() };
          }
          return {};
        });
      },

      restart: () => {
        // we want to replace the phase property
        set((state) => {
          if (state.phase === "playing" || state.phase === "ended") {
            return { phase: "ready", blocksSeed: Math.random() };
          }
          return {};
        });
      },

      end: () => {
        // we want to replace the phase property
        set((state) => {
          if (state.phase === "playing") {
            // end time will be saved when the phase changes to ended
            return { phase: "ended", endTime: Date.now() };
          }
          return {};
        });
      },
    };
  })
);
