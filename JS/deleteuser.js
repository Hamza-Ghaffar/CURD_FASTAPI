document.addEventListener("DOMContentLoaded", async () => {
  
  
  

    try {
    
    const getuserdeleteform = document.querySelector("#delete-user-form");
    if (getuserdeleteform) {
        getuserdeleteform.addEventListener("submit", async (event) => {
        event.preventDefault();

        const userdeleteformdata = new FormData(getuserdeleteform);

        // Extract specific fields for editing
       

        // Get the user ID from the FormData object
        const userId = userdeleteformdata.get("id");

        try {
          const access_token =
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRoZVJvY2siLCJleHAiOjE3MTY1NTc0ODN9.spxvqg3W5imGsBSlr2jsR0e02NYaojaWlX7mb1DVCxA";

          localStorage.setItem("token", access_token);
          const savetoken = localStorage.getItem("token");
          
          const response = await fetch(`http://127.0.0.1:8888/user/${userId}`, {
            method: "delete",
            mode: "cors",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${savetoken}`,
            },
            //body: JSON.stringify(userId),
          });

          // Check if the response is ok (status code 200-299)

          if (!response.ok) {
            throw error(error)
          }
          // Log success message
          else console.log("Request successful");
          alert(`User ${userId} Deleted Successfully `);

        } catch (error) {
          // Log any errors that occur during fetch request
          console.error("Error:", error);
          if (
            error instanceof TypeError &&
            error.message === "Failed to fetch"
          ) {
            alert("Network error. Please check your internet connection.");
          } else {
            alert("Something went wrong with the request.");
          }
        }
      });
    }
  } catch (error) {
    // Log any errors that occur in the main try block
    console.log("Error:", error);
  }
});
