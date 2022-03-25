const button = document.querySelector("#check");
const text = document.querySelector("#email");

button.addEventListener("click", () => {
  let email = text.value;
  // console.log(email);
  fetch("/check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.querySelector("#result").innerHTML = "";
      if (data.is_spam) {
        document.querySelector("#result").innerHTML = spam_message;
      } else {
        document.querySelector("#result").innerHTML = ham_message;
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

spam_message = `<h2 id="result">Ohh No! It's a spam!</h2>`;
ham_message = `<h2 id="result">Don't Worry! It's not a spam.</h2>`;
