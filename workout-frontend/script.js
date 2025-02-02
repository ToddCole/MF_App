const API_URL = "http://127.0.0.1:5000/workout?category=";
const NUTRITION_API_URL = "http://127.0.0.1:5000/nutrition";

async function fetchWorkouts() {
    const category = document.getElementById("category").value;
    document.getElementById("loading").classList.remove("hidden"); // Show loading text
    try {
        const response = await fetch(API_URL + category);
        if (!response.ok) throw new Error("Network response was not OK");

        const data = await response.json();
        document.getElementById("loading").classList.add("hidden"); // Hide loading text

        const resultsDiv = document.getElementById("workout-results");
        resultsDiv.innerHTML = ""; // Clear previous results

        if (data.exercises.length === 0) {
            resultsDiv.innerHTML = "<p>No workouts found.</p>";
            return;
        }

        data.exercises.forEach(exercise => {
            const exerciseCard = document.createElement("div");
            exerciseCard.classList.add("exercise-card");
            exerciseCard.innerHTML = `
                <h2>${exercise.name}</h2>
                <p>${exercise.description}</p>
                <strong>Equipment: ${exercise.equipment.length > 0 ? exercise.equipment.join(", ") : "None"}</strong>
            `;
            resultsDiv.appendChild(exerciseCard);
        });

    } catch (error) {
        console.error("Error fetching workouts:", error);
        document.getElementById("workout-results").innerHTML = `<p style="color: red;">Failed to fetch workouts. Try again later.</p>`;
    }
}

// Fetch Nutrition Data
async function fetchNutrition() {
    try {
        const response = await fetch(NUTRITION_API_URL);
        if (!response.ok) throw new Error("Network response was not OK");

        const data = await response.json();
        const resultsDiv = document.getElementById("nutrition-results");
        resultsDiv.innerHTML = ""; // Clear previous results

        if (!data.results || data.results.length === 0) {
            resultsDiv.innerHTML = "<p>No nutrition data available.</p>";
            return;
        }

        data.results.forEach(ingredient => {
            const nutritionCard = document.createElement("div");
            nutritionCard.classList.add("nutrition-card");
            nutritionCard.innerHTML = `
                <h2>${ingredient.name}</h2>
                <p>ID: ${ingredient.id}</p>
            `;
            resultsDiv.appendChild(nutritionCard);
        });

    } catch (error) {
        console.error("Error fetching nutrition data:", error);
        document.getElementById("nutrition-results").innerHTML = `<p style="color: red;">Failed to fetch nutrition data.</p>`;
    }
}
