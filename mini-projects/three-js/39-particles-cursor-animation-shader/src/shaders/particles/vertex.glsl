uniform vec2 uResolution;
uniform sampler2D uPictureTexture;
uniform sampler2D uColorGradientTexture;
uniform sampler2D uDisplacementTexture;

attribute float aIntensity;
attribute float aAngle;

varying vec3 vColor;

void main() {

  // Displacement
  vec3 newPosition = position;
  float displacementIntensity = texture(uDisplacementTexture, uv).r;
  // the particles come back to their original position
  displacementIntensity = smoothstep(0.1, 0.3, displacementIntensity);

  vec3 displacement = vec3(cos(aAngle) * 0.2, sin(aAngle) * 0.2, 1.0);
  displacement = normalize(displacement);
  displacement *= displacementIntensity;
  displacement *= 3.0;
  displacement *= aIntensity;

  newPosition += displacement;

    // Final position
  vec4 modelPosition = modelMatrix * vec4(newPosition, 1.0);
  vec4 viewPosition = viewMatrix * modelPosition;
  vec4 projectedPosition = projectionMatrix * viewPosition;
  gl_Position = projectedPosition;

    // Picture
    // texture function pick the color from uPictureTexture at the uv coordinates and swizzle the r channel
  float pictureIntensity = texture(uPictureTexture, uv).r;

    // Point size
  gl_PointSize = 0.15 * pictureIntensity * uResolution.y;
  gl_PointSize *= (1.0 / -viewPosition.z);

  // Varyings
  vColor = vec3(pow(pictureIntensity, 2.0));

  vec3 colorGradient = texture(uColorGradientTexture, uv).rgb;
  vColor = vec3(colorGradient);

}
