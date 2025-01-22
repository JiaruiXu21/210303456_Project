// script.js

// Ensure the DOM is fully loaded before attaching event listeners
document.addEventListener("DOMContentLoaded", () => {

    // Add event listener to form submission for validation
    const form = document.querySelector("form");
    form.addEventListener("submit", (event) => {
        if (!validateForm()) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    // Function to validate the form inputs
    function validateForm() {
        let isValid = true;
        const selects = document.querySelectorAll("form select");
        const textInputs = document.querySelectorAll("form input[type='text']");

        // Check if all dropdowns are selected
        selects.forEach((select) => {
            if (!select.value) {
                isValid = false;
                highlightError(select);
            } else {
                clearError(select);
            }
        });

        // Check if all text inputs are filled
        textInputs.forEach((input) => {
            if (!input.value.trim()) {
                isValid = false;
                highlightError(input);
            } else {
                clearError(input);
            }
        });

        if (!isValid) {
            alert("Please fill out all fields before submitting.");
        }
        return isValid;
    }

    // Highlight error for invalid inputs
    function highlightError(element) {
        element.style.border = "2px solid red";
    }

    // Clear error styling for valid inputs
    function clearError(element) {
        element.style.border = "";
    }

    // Optional: Add live preview of recommendations based on current selections
    const previewArea = document.getElementById("preview");
    if (previewArea) {
        form.addEventListener("change", updatePreview);
    }

    function updatePreview() {
        const lifestyle = document.querySelector("select[name='lifestyle']").value;
        const material = document.querySelector("select[name='material']").value;
        const priceRange = document.querySelector("select[name='price_range']").value;

        previewArea.innerHTML = `
            <strong>Current Selections:</strong><br>
            Lifestyle: ${lifestyle || "Not Selected"}<br>
            Material: ${material || "Not Selected"}<br>
            Price Range: ${priceRange || "Not Selected"}
        `;
    }
});
