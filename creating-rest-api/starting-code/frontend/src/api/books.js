// TODO: Import API_ENDPOINT
import { API_ENDPOINT } from "./index.js";

// TODO: Create the addNewBook function that takes in newTitle, newStart, and newEnd as arguments. Inside the function, create a POST request for the new book. Store the response as a JSON in a variable called newBook and return it at the end of the function.

export const addNewBook = async (newTitle, newStart, newEnd) => {
  // create a const variable called response that will be used to store the response of our POST request for a new book called newTitle for the book club to read between newStart date to newEnd date.
  const response = await fetch(`${API_ENDPOINT}/books`, {
    method: "POST",
    body: JSON.stringify({
      title: newTitle,
      start: newStart,
      end: newEnd,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const newBook = await response.json();
  return newBook;
};

// TODO: Create the getBooks function that retrieves all of the books that have been saved to the back-end API
export const getBooks = async () => {
  const response = await fetch(`${API_ENDPOINT}/books`);
  const books = await response.json();

  return books;
};


// TODO: Create the updateBook function that takes the arguments id, newTitle, newStart, newEnd. Inside of the function, create a PUT request for the specified book to be updated. Return the status of the response at the end of the function.
export const updateBook = async (id, newTitle, newStart, newEnd) => {
  // create a const variable called response that will be used to wait for the response of our PUT request for updating the specified book’s meta and scheduling information
  const response = await fetch(`${API_ENDPOINT}/books/${id}`, {
    method: "PUT",
    body: JSON.stringify({
      newTitle,
      newStart,
      newEnd
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  return response.status;
};

// TODO: Create the deleteBook function that takes the id of the book to be deleted as an argument. Inside of the function, create a DELETE request for the specified book to be deleted. Return the status of the response at the end of the function.
export const deleteBook = async (id) => {
  const response = await fetch(`${API_ENDPOINT}/books/${id}`, {
    method: "DELETE",
  });

  return response.status;
};
