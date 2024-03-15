import { create, all } from "mathjs";

// import { useEffect, useRef } from "react";
// import { useThree, useFrame } from "react-three-fiber";
// import { Sky } from "three/examples/jsm/objects/Sky.js";
// import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

const CalcSunPosition = () => {
  const math = create(all, {});

  const SunCalc = require("suncalc");
  console.log("Calculo do SOL", SunCalc);

  // get today's sunlight times for London
  const times = SunCalc.getTimes(new Date(), 51.5, -0.1);

  // get position of the sun (azimuth and altitude) at today's sunrise
  const sunrisePos = SunCalc.getPosition(times.sunrise, 51.5, -0.1);
  console.log("Sunrise ------------ ", sunrisePos);

  // get sunrise azimuth in degrees
  const sunriseAzimuth = (sunrisePos.azimuth * 180) / Math.PI;
  console.log("Sunrise Azimuth", sunriseAzimuth);

  const altitude = sunrisePos.altitude;
  console.log("Altitude", altitude);

  const azimuth = sunrisePos.azimuth;
  console.log("Azimuth", azimuth);

  // azimuth = -1.528729280365006;
  // altitude = -0.012671868724339556;

  const x = math.cos(altitude) * math.cos(azimuth);
  const y = math.cos(altitude) * math.sin(azimuth);
  const z = math.sin(altitude);

  console.log("X", x);
  console.log("Y", y);
  console.log("Z", z);

  return [x, y, z];

  // return (
  //   <group>
  //     <ambientLight intensity={0.1} />
  //     <directionalLight
  //       position={[x, y, z]}
  //       intensity={0.5}
  //       castShadow
  //       // shadow-mapSize-width={1024}
  //       // shadow-mapSize-height={1024}
  //       // shadow-camera-far={50}
  //       // shadow-camera-left={-10}
  //       // shadow-camera-right={10}
  //       // shadow-camera-top={10}
  //       // shadow-camera-bottom={-10}
  //     />
  //   </group>
  // );
};

export default CalcSunPosition;
