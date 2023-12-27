import DrunkEffect from "./DrunkEffect";
import { forwardRef } from "react";

export default forwardRef(function Drunk(props, ref) {
  // console.log(props);

  // instantiate the effect
  const effect = new DrunkEffect(props);

  return <primitive ref={ref} object={effect} />;
});

/**
forwardRef is a function that takes a component and returns a new component that forwards the ref to the inner component.
 */
