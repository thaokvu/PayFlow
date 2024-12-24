// script.js - JavaScript for interactivity
// PURPOSE - Provides interactivity and enhance user experience on the paycheck page

// Event listener for the "Download Paycheck" button  
document.addEventListener("DOMContentLoaded", function () {  
    // Select the "Download Paycheck" button by its class  
    const downloadButton = document.querySelector(".btn-download");  

    // Ensure the button exists before adding functionality  
    if (downloadButton) {  
        // Add a click event listener to the button  
        downloadButton.addEventListener("click", function (event) {  
            // Prevent default action if necessary (e.g., avoid form submission issues)  
            event.preventDefault();  

            // Show a confirmation dialog when the user clicks the button  
            const userConfirmed = confirm("Do you want to download your paycheck?");  
            
            if (userConfirmed) {  
                // Proceed with downloading the paycheck  
                window.location.href = downloadButton.getAttribute("href");  
                showNotification("Your paycheck is being downloaded.", "success");  
            } else {  
                // Notify the user if they cancel the action  
                showNotification("Paycheck download canceled.", "warning");  
            }  
        });  
    }  
});  

// Function to show a notification message  
function showNotification(message, type = "info") {  
    // Create a notification div element  
    const notification = document.createElement("div");
    // Add appropriate classes for styling  
    notification.className = `notification ${type}`;   
    // Set the text content of the notification
    notification.innerText = message;   

    // Append the notification to the body or a specific container  
    document.body.appendChild(notification);  

    // Automatically remove the notification after 3 seconds  
    setTimeout(() => {  
        notification.remove();  
    }, 3000);  
}  

// Add functionality for additional interactive elements  
// Alerting users about updates or warnings dynamically  
function alertUserUpdate(message) {  
    // Alert the user with a standard alert box
    alert(message);   
    // Show a notification for the update  
    showNotification(message, "info"); 
}  