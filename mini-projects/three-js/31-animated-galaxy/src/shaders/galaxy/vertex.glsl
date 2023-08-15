uniform float uSize;
uniform float uTime;
attribute float aScale;
attribute vec3 aRandomness;

varying vec3 vColor;


void main() {

            // Position
  vec4 modelPosition = modelMatrix * vec4(position, 1.0);

  // Spin
  float angle = atan(modelPosition.x, modelPosition.z); // calcular o angulo
  float distanceToCenter = length(modelPosition.xz); // calcular a distancia do centro
  float angleOffset = (1.0 / distanceToCenter) * uTime * 0.2; // calcular o offset angle
  angle += angleOffset; // adicionar o offset ao angulo
  modelPosition.x = cos(angle) * distanceToCenter; // calcular a nova posicao x
  modelPosition.z = sin(angle) * distanceToCenter; // calcular a nova posicao z

  // Randomness
  modelPosition.xyz += aRandomness;
  // modelPosition += aRandomness;
  // modelPosition.x += aRandomness.x;
  // modelPosition.y += aRandomness.y;
  // modelPosition.z += aRandomness.z;

  vec4 viewPosition = viewMatrix * modelPosition;
  vec4 projectedPosition = projectionMatrix * viewPosition;
  gl_Position = projectedPosition;

            //Size
  gl_PointSize = uSize * aScale;
  // copiei essa linha do points.glsl.js no node_modules do three.js
  // para deixar as particulas com o mesmo tamanho independente da distancia
  gl_PointSize *= (1.0 / - viewPosition.z);

  // Co\lor
  vColor = color;
}
