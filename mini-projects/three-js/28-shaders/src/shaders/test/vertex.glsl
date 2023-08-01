// transform the coordinates into the clip space
// uniform mat4 projectionMatrix;
// apply transformations relative to the camera (position, rotation, field of view, near, far)
// uniform mat4 viewMatrix;
// apply transformations relative to the Mesh (position, rotation, scale)
// uniform mat4 modelViewMatrix;
// use it for the wavez frequency
uniform vec2 uFrequency;
// use it for the wavez speed
uniform float uTime;

// attribute vec3 position;
// attribute vec2 uv;

varying vec2 vUv;
varying float vElevation;

// attribute float aRandom;
// varying float vRandom;

void main()
{
    vec4 modelPosition = modelViewMatrix * vec4(position, 1.0);

    // add elevation to the model to being realistic
    float elevation = sin(modelPosition.x * uFrequency.x - uTime) * 0.1;
    elevation += sin(modelPosition.y * uFrequency.y - uTime) * 0.1;

    modelPosition.z += elevation;

    modelPosition.z += sin(modelPosition.x * uFrequency.x - uTime) * 0.1;
    modelPosition.z += sin(modelPosition.y * uFrequency.y - uTime) * 0.1;

    // modelPosition.y += uTime;

    // modelPosition.z += aRandom * 0.1;

    vec4 viewPosition = viewMatrix * modelPosition;
    vec4 projectedPosition = projectionMatrix * viewPosition;

    gl_Position = projectedPosition;

    vUv = uv;
    vElevation = elevation;

    // vRandom = aRandom;
}

// this function above  is called automatically

// float fooBar = 0.4; sintax example

// int foo = 5; sintax example -  we can't mix float with integer (you need convert just one float or int)

// bool foo = true; sintax example

// vec2 foo = vec2(1.0, 2.0); x and y values

// vec3 foo = vec3(0.0);

// vec3 purpleColor = vec3(0.0); - I can use with RGB values
// purpleColor.r = 0.5:
// purpleColor.b = 1.0:

// vec4 we can use letter w : vec4(w,x,y,z)

// float loremIpum(float a, float b) {  -- we also can use void instead float
//  return a + b;
// }
// float result = loremIpum(1.0,);
