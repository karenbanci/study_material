import { Effect, BlendFunction } from "postprocessing";
import { Uniform } from "three";

const fragmentShader = /* glsl */ `

    uniform float frequency;
    uniform float amplitude;
    uniform float offset;

    // vai criar ondas na tela
    void mainUv(inout vec2 uv)
    {
      uv.y += sin(uv.x * frequency + offset) * amplitude;
    }

    //vai aplicar um filtro na tela - neste caso, verde
    void mainImage(const in vec4 inputColor, const in vec2 uv, out vec4 outputColor)
    {
      outputColor = vec4(0.8, 1.0, 0.5, inputColor.a);
    }
`;

export default class DrunkEffect extends Effect {
  constructor({ frequency, amplitude, blendFunction = BlendFunction.DARKEN }) {
    super("DrunkEffect", fragmentShader, {
      blendFunction: blendFunction,
      uniforms: new Map([
        // name of property, value
        ["frequency", new Uniform(frequency)],
        ["amplitude", new Uniform(amplitude)],
        ["offset", new Uniform(0)], // animation
      ]),
    });
  }

  update(renderer, inputBuffer, deltaTime) {
    // console.log("update");
    // deltaTime is the time between the last frame and the current one - performance
    this.uniforms.get("offset").value += deltaTime;
  }
}

/**
We are using the WebGL 2 syntax where we can specify more information associated with each parameter:

- const means that the parameter is not writable.
- in means that it’s a copy of the actual variable and changing it won’t affect the initial variable sent when calling the function.
- out means that changing this value will change the variable sent when calling the function.

It prevents us from making mistakes but also gives us a hint about what variables we need to change:

- inputColor contains the current color for that pixel which is defined by the previous effects.
- uv contains the render coordinates (from 0,0 at the bottom left corner to 1,1 in the top right corner).
- outputColor is what we need to change in order to apply the effect.
 */
