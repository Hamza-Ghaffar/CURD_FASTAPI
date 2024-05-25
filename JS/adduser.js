document.addEventListener("DOMContentLoaded", async () => {
  
  // Check if the user is already authenticated
  const token = localStorage.getItem("token");

  // Check if the current page is the login page
  const isLoginPage = window.location.pathname.includes("login.html");

  // If not authenticated and not on the login page, redirect to the login page
  if (!token && !isLoginPage) {
    window.location.href = "login.html";
    return;
  }
  const addUserForm = document.querySelector("#add-user-form");

  if (addUserForm) {
    addUserForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const formData = new FormData(addUserForm);
      const userData = {};
      formData.forEach((value, key) => {
        userData[key] = value;
      });

      try {
        const get_token_from_localstorge = localStorage.getItem("token");

        if (!get_token_from_localstorge) {
          throw new Error("JWT token not found");
        }

        const response = await fetch("http://127.0.0.1:8888/user/", {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${get_token_from_localstorge}`, // 
          },
          body: JSON.stringify(userData),
        });

        if (response.ok) {
          const data = await response.json();
          console.log("User added successfully:");
          alert("User added successfully!", data);
          window.location.href = "adduser.html";
        } else {
          const errorData = await response.json();
          console.error("Error adding user:", errorData.detail);
          alert("Error adding user: " + errorData.detail);

          // Check if the error is related to the user already existing
          if (
            response.status === 400 &&
            errorData.detail.includes("already exists")
          ) {
            alert("Error adding user: " + errorData.detail);
            // Stay on the same page for this specific error
          }
        }
      } catch (error) {
        console.error("Network error:", error);
        alert("A network error occurred Try Login Again");
      }
    });
  }


  // Create a logout button
  const logoutButton = document.createElement("button");
  logoutButton.textContent = "Logout";
  logoutButton.setAttribute("id", "logout");

  // Append the logout button to the addUserForm
  if (addUserForm) {
    addUserForm.appendChild(logoutButton);
  }

  // Add event listener to the logout button
  logoutButton.addEventListener("click", () => {
    // Remove the JWT token from local storage
    localStorage.removeItem("token");

    // Redirect to the login page
    window.location.href = "dashboard.html";
  });

  // Prevent users from navigating back to this page after logging out
  window.addEventListener("beforeunload", (event) => {
    const token = localStorage.getItem("token");
    if (!token) {
      event.preventDefault();
    }
  });

});
