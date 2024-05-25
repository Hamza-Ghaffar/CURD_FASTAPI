document.addEventListener("DOMContentLoaded", async () => {
  const loginForm = document.querySelector("#login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const email = document.querySelector("#email").value;
      const password = document.querySelector("#password").value;
      const loginData = new URLSearchParams();
      loginData.append("username", email);
      loginData.append("password", password);

      try {
        const response = await fetch("http://127.0.0.1:8888/login/", {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          body: loginData.toString(),
        });

        if (response.ok) {
          const data_in_response_json = await response.json();
          localStorage.setItem("token", data_in_response_json.access_token);
          window.location.href = "adduser.html";
          alert("Login successful!");
        } else {
          const errorData = await response.json();
          console.error("Login Failed:", errorData.detail);
          alert("Login failed: " + errorData.detail);
        }
      } catch (error) {
        console.error("Network Error:", error);
        alert("A network error occurred");
      }
    });
  }

  
});
