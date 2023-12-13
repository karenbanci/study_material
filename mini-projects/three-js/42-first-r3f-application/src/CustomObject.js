import * as THREE from "three";
import { useMemo, useEffect, useRef } from "react";

export default function CustomObject() {
  // create ref
  const geometryRef = useRef();

  // useEffect because the geometryRef is not ready yet (it's undefined)
  // in the first render
  useEffect(() => {
    geometryRef.current.computeVertexNormals(); // it would be called once
  }, []);

  // criating triangles
  const verticesCount = 10 * 3;

  // create a cache of positions
  const positions = useMemo(() => {
    const positions = new Float32Array(verticesCount * 3);

    for (let i = 0; i < verticesCount; i++) {
      positions[i] = (Math.random() - 0.5) * 3;
    }

    return positions;
  }, []);

  return (
    <mesh>
      <bufferGeometry ref={geometryRef}>
        <bufferAttribute
          attach="attributes-position"
          count={verticesCount}
          itemSize={3}
          array={positions}
        />
      </bufferGeometry>
      <meshStandardMaterial color="red" side={THREE.DoubleSide} />
    </mesh>
  );
}
