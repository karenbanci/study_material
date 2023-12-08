import { useRef, useState, useEffect } from "react";

export default function Clicker({ increment, keyName, color }) {
  // this is the same as the above, but with a default value from local storage
  const [count, setCount] = useState(
    parseInt(localStorage.getItem(keyName) ?? 0)
  );

  const buttonRef = useRef();
  // console.log(buttonRef);

  // o codigo abaixo vai fazer exatamente a mesma coisa que o codigo acima
  // useEffect(() => {
  //   // get item from local storage
  //   const savedCount = parseInt(localStorage.getItem("count") ?? 0);
  //   // keep the count in sync with the local storage if you uppdate the page
  //   setCount(savedCount);
  //   // empty array means that this effect will only run once
  // }, []);

  // irá salvar a contagem no localStorage
  useEffect(() => {
    // localStorage saves data locally in the browser
    localStorage.setItem(keyName, count);
    // this effect will run every time the count changes
  }, [count]);

  // irá destruir a contagem do localStorage - first render
  useEffect(() => {
    // console.log("buttonRef");
    buttonRef.current.style.backgroundColor = color;
    buttonRef.current.style.color = "black";

    return () => {
      localStorage.removeItem(keyName);
    };
  }, []);

  const buttonClick = () => {
    setCount(count + 1);
    increment(); // this is a prop function
  };

  return (
    <div>
      <div style={{ color }}>Clicks count: {count} </div>
      <button ref={buttonRef} onClick={buttonClick}>
        Click me!
      </button>
    </div>
  );
}
