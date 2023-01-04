import { API_ENDPOINT } from ".";

export const getBooks = async () => {
  const response = await fetch(`${API_ENDPOINT}/books`);
  const books = await response.json();

  return books;
};

export const addNewBook = async (newTitle, newStart, newEnd) => {
  const response = await fetch(`${API_ENDPOINT}/books`, {
    method: "POST",
    body: JSON.stringify({
      title: newTitle,
      start: newStart,
      end: newEnd
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const newBook = await response.json();

  return newBook;
};

export const deleteBook = async (id) => {
  const response = await fetch(`${API_ENDPOINT}/books/${id}`, {
    method: "DELETE",
  });

  return response.status;
};

export const updateBook = async (id, newTitle, newStart, newEnd) => {
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
