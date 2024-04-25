varying vec3 vColor;
// uniform sampler2D uColorGradientTexture;

void main() {

  vec2 uv = gl_PointCoord;
  float distanceToCenter = length(uv - vec2(0.5));

  //remove the edges
  if(distanceToCenter > 0.5) {
    discard;
  };

  // vec3 colorGradient = texture2D(uColorGradientTexture, uv).rgb;
  // gl_FragColor = vec4(colorGradient, 1.0);

  // gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0)
  gl_FragColor = vec4(vColor, 1.0);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>

}
