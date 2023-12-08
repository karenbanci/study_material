import { useMemo, useState } from "react";
import Clicker from "./Clicker";
import People from "./People";

export default function App({ clickersCount, children }) {
  // we will destroy the clicker after a while
  const [hasClicker, setHasClicker] = useState(true);
  const [count, setCount] = useState(0);

  const toggleClicker = () => {
    setHasClicker(!hasClicker);
  };

  const increment = () => {
    // total count
    setCount(count + 1);
  };

  // it works like a cache
  const colors = useMemo(() => {
    const colors = [];

    for (let i = 0; i < clickersCount; i++) {
      colors.push(`hsl(${Math.random() * 360}deg, 100%, 70%)`);
    }

    return colors;
    // if classClickerCount changes, this function will run again
  }, [hasClicker]);

  // console.log(colors);

  return (
    <>
      {children}

      <div>Total Count: {count}</div>

      <button onClick={toggleClicker}>
        {/* text is changing */}
        {hasClicker ? "Hide" : "Show"} Clicker
      </button>
      {/* esconde o botao de clicker */}
      {hasClicker && (
        <>
          {[...Array(clickersCount)].map((value, index) => {
            return (
              <Clicker
                key={index}
                increment={increment}
                keyName={`count${index}`}
                color={colors[index]}
              />
            );
          })}
        </>
      )}
      <People />
    </>
  );
}
