const axios = require("axios");

document.getElementById("request").onclick = () => {
  axios
    .get("http://localhost:8000/")
    .then((response) => {
      const messageJumbotron = document.getElementById("message");
      messageJumbotron.innerText = response.data;
      messageJumbotron.style.display = "block";
    })
    .catch((error) => {
      if (error) throw new Error(error);
    });
};
