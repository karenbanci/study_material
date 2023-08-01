// precision mediump float;

uniform vec3 uColor;
uniform sampler2D uTexture; // type of textures

varying vec2 vUv;
varying float vElevation;

// varying float vRandom;

// put color each fragment (pixel)
void main()
{
  vec4 textureColor = texture2D(uTexture, vUv);
  textureColor.rgb *= vElevation * 2.0 + 0.6;
  gl_FragColor = textureColor;

  // gl_FragColor = vec4(vUv, 1.0, 1.0);
}
