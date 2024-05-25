document.addEventListener("DOMContentLoaded", async () => {
  
  
  

    try {
    
    const getuserupdateform = document.querySelector("#add-user-form");
    if (getuserupdateform) {
      getuserupdateform.addEventListener("submit", async (event) => {
        event.preventDefault();

        const userupdateformdata = new FormData(getuserupdateform);

        // Extract specific fields for editing
        const userupdatedatadict = {
          username: userupdateformdata.get("username"),
          email: userupdateformdata.get("email"),
          password: userupdateformdata.get("password"),
          mobile_number: userupdateformdata.get("mobile_number"),
          full_name: userupdateformdata.get("full_name"),
          is_active: userupdateformdata.get("is_active") === "true",
          is_superuser: userupdateformdata.get("is_superuser") === "true",
        };

        // Get the user ID from the FormData object
        const userId = userupdateformdata.get("id");

        try {
          const access_token =
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlJvY2siLCJleHAiOjE3MTY1NTAxOTZ9.2yJjbbtECUymmF0z66CNLzMXgKziWa7Mc0C2qQMcSmM";

          localStorage.setItem("token", access_token);
          const savetoken = localStorage.getItem("token");
          
          const response = await fetch(`http://127.0.0.1:8888/user/${userId}`, {
            method: "PUT",
            mode: "cors",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${savetoken}`,
            },
            body: JSON.stringify(userupdatedatadict),
          });

          // Check if the response is ok (status code 200-299)

          if (!response.ok) {
            throw error(error)
          }
          // Log success message
          else console.log("Request successful");
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
