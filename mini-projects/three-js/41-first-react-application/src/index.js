import "./style.css";
import { createRoot } from "react-dom/client";
import App from "./App.js";

const root = createRoot(document.querySelector("#root"));

root.render(
  <div>
    <App
      clickersCount={3}
      children={
        <>
          <h1>Primeiro</h1>
        </>
      }
    />
    {/* <App
      clickersCount={3}
      children={
        <>
          <h1>Segundo</h1>
        </>
      }
    />
    <App
      clickersCount={3}
      children={
        <>
          <h1>Terceiro</h1>
        </>
      }
    /> */}
  </div>
);
