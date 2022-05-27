const axios = require("axios");

export async function getData() {
  const response = await axios.get("http://localhost:8000/");
  return response.data;
}
