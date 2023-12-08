import React, { useEffect, useState } from "react";

export default function People() {
  const [people, setPeople] = useState([]);

  // this function will get the data from the server in async way
  // the fetch is loading the data from the internet
  // resques a response from the server
  // return a promise because it will take some time to parse the data
  // when parse is done, it will return all the data from the server (result is the data from the server)
  const getPeople = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const result = await response.json();

    setPeople(result);

    // console.log(result);

    // fetch("https://jsonplaceholder.typicode.com/users")
    //  .then((response) => response.json())
    //  .then((result) => console.log(result));
  };

  useEffect(() => {
    getPeople();
  }, []);

  return (
    <div>
      <h2>People</h2>
      <ul>
        {people.map((person, id) => (
          <li key={id}>
            {person.name}, <br />
            {person.email} <br />
            <br />
          </li>
        ))}
      </ul>
    </div>
  );
}
