import "./App.css";
import * as THREE from "three";
import React from "react";
// import { Canvas } from "react-three-fiber";
import Scene from "./Scene.js";
import styled from "styled-components";

console.log("Scene", Scene);

function App() {
  const SceneConainer = styled.div`
    width: 100%;
    height: 100vh;
    /* background-color: black; */
  `;

  return (
    <SceneConainer>
      <Scene />
    </SceneConainer>
  );
}

export default App;
