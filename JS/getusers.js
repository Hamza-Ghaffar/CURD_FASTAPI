document.addEventListener("DOMContentLoaded", () => {
    
    const userListContainer = document.getElementById("user-list");
    const fetchUsersButton = document.getElementById("fetch-users-button");

    const fetchUsers = async () => {
        const access_token = localStorage.getItem("token");

        if (!access_token) {
            alert("JWT token not found");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8888/user", {
                method: "GET",
                mode: "cors",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${access_token}`,
                }
            });

            if (!response.ok) {
                throw new Error("Request failed");
            }

            const users = await response.json();
            console.log("Fetched users:", users);

            userListContainer.innerHTML = ""; // Clear existing users
            users.forEach(user => {
                const userCard = document.createElement("div");
                userCard.classList.add("user-card");

                const userName = document.createElement("h2");
                userName.textContent = user.username;
                userCard.appendChild(userName);

                const userEmail = document.createElement("p");
                userEmail.textContent = `Email: ${user.email}`;
                userCard.appendChild(userEmail);

                userListContainer.appendChild(userCard);
            });
        } catch (error) {
            console.error("Error:", error);
            if (error instanceof TypeError && error.message === "Failed to fetch") {
                console.error("Network error. Please check your internet connection.");
                alert("Network error. Please check your internet connection.");
            } else {
                console.error("Something went wrong with the request.");
                alert("Something went wrong with the request.");
            }
        }
    };

    fetchUsersButton.addEventListener("click", fetchUsers);
});
