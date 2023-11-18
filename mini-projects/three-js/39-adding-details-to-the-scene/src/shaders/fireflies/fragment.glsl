void main() {
  float distanceToCenter = distance(gl_PointCoord, vec2(0.5));
  // tira a borda das estrelas
  float strength = 0.05 / distanceToCenter - 0.1;

  gl_FragColor = vec4(1.0, 1.0, 1.0, strength);
}
