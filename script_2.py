# JavaScript File
js_content = '''// NutriFlow Premium Diet Scheduler App

// Sample data
const sampleData = {
    sampleMealPlans: {
        monday: {
            breakfast: {name: "Greek Yogurt Bowl", calories: 320, protein: 20, carbs: 25, fat: 12},
            lunch: {name: "Quinoa Salad", calories: 450, protein: 15, carbs: 60, fat: 16},
            dinner: {name: "Grilled Salmon", calories: 380, protein: 35, carbs: 15, fat: 22},
            snack: {name: "Apple & Almonds", calories: 180, protein: 6, carbs: 20, fat: 10}
        },
        tuesday: {
            breakfast: {name: "Oatmeal with Berries", calories: 280, protein: 12, carbs: 45, fat: 8},
            lunch: {name: "Turkey Wrap", calories: 420, protein: 25, carbs: 35, fat: 18},
            dinner: {name: "Chicken Stir-fry", calories: 400, protein: 30, carbs: 25, fat: 20},
            snack: {name: "Protein Smoothie", calories: 200, protein: 15, carbs: 18, fat: 8}
        },
        wednesday: {
            breakfast: {name: "Avocado Toast", calories: 300, protein: 12, carbs: 30, fat: 18},
            lunch: {name: "Lentil Soup", calories: 350, protein: 18, carbs: 50, fat: 8},
            dinner: {name: "Beef & Vegetables", calories: 450, protein: 35, carbs: 20, fat: 25},
            snack: {name: "Greek Yogurt", calories: 120, protein: 12, carbs: 8, fat: 5}
        },
        thursday: {
            breakfast: {name: "Smoothie Bowl", calories: 290, protein: 15, carbs: 35, fat: 12},
            lunch: {name: "Chicken Caesar Salad", calories: 380, protein: 30, carbs: 15, fat: 22},
            dinner: {name: "Pasta Primavera", calories: 420, protein: 18, carbs: 55, fat: 16},
            snack: {name: "Mixed Nuts", calories: 160, protein: 6, carbs: 8, fat: 14}
        },
        friday: {
            breakfast: {name: "Egg Benedict", calories: 350, protein: 18, carbs: 25, fat: 20},
            lunch: {name: "Sushi Bowl", calories: 400, protein: 25, carbs: 45, fat: 12},
            dinner: {name: "Grilled Chicken", calories: 370, protein: 35, carbs: 12, fat: 18},
            snack: {name: "Fruit Salad", calories: 150, protein: 3, carbs: 35, fat: 2}
        },
        saturday: {
            breakfast: {name: "Pancakes", calories: 380, protein: 12, carbs: 50, fat: 15},
            lunch: {name: "Buddha Bowl", calories: 420, protein: 20, carbs: 45, fat: 18},
            dinner: {name: "Fish Tacos", calories: 400, protein: 28, carbs: 35, fat: 20},
            snack: {name: "Dark Chocolate", calories: 140, protein: 3, carbs: 15, fat: 9}
        },
        sunday: {
            breakfast: {name: "French Toast", calories: 340, protein: 14, carbs: 40, fat: 16},
            lunch: {name: "Mediterranean Bowl", calories: 430, protein: 22, carbs: 38, fat: 22},
            dinner: {name: "Roast Chicken", calories: 390, protein: 38, carbs: 8, fat: 24},
            snack: {name: "Hummus & Veggies", calories: 170, protein: 8, carbs: 18, fat: 9}
        }
    },
    motivationalMessages: [
        "Great job staying consistent! 🌟",
        "You're building healthy habits one meal at a time! 💪",
        "Your dedication is inspiring! Keep it up! 🎉",
        "Every healthy choice counts - you're doing amazing! ✨",
        "Consistency is key, and you've got it! 🔥",
        "You're crushing your goals today! 🚀",
        "Small steps lead to big changes! 🌱",
        "Your future self will thank you! 💚"
    ],
    groceryCategories: {
        proteins: ["Salmon", "Chicken breast", "Greek yogurt", "Turkey", "Almonds", "Eggs", "Beef", "Tofu"],
        vegetables: ["Spinach", "Bell peppers", "Broccoli", "Carrots", "Tomatoes", "Avocado", "Mixed greens"],
        fruits: ["Apples", "Berries", "Bananas", "Oranges", "Lemons", "Mixed fruit"],
        grains: ["Quinoa", "Oats", "Brown rice", "Whole wheat wraps", "Pasta", "Bread"],
        dairy: ["Greek yogurt", "Almond milk", "Cheese", "Butter"],
        pantry: ["Olive oil", "Nuts", "Dark chocolate", "Hummus", "Spices"]
    },
    nutritionGoals: {
        calories: 1800,
        protein: 120,
        carbs: 200,
        fat: 70,
        fiber: 25,
        water: 8
    },
    achievements: [
        {id: 1, name: "First Week", icon: "🏆", description: "Completed your first week", unlocked: true},
        {id: 2, name: "Streak Master", icon: "🔥", description: "7-day logging streak", unlocked: true},
        {id: 3, name: "Nutrition Expert", icon: "📊", description: "Hit all macro targets", unlocked: false},
        {id: 4, name: "Meal Prep Pro", icon: "👨‍🍳", description: "Generated 10 meal plans", unlocked: true},
        {id: 5, name: "Hydration Hero", icon: "💧", description: "Drank 8 glasses of water", unlocked: false},
        {id: 6, name: "Consistency King", icon: "👑", description: "30-day streak", unlocked: false}
    ]
};

// App state
let currentUser = {
    age: 28,
    weight: 150,
    goal: 'maintain',
    preferences: ['vegetarian'],
    streak: 7,
    totalCalories: 1234
};

let currentDay = 'monday';
let currentSection = 'landing';

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    setupEventListeners();
});

function initializeApp() {
    showSection('landing');
    updateDashboard();
    updateMealDisplay();
    updateGroceryList();
    updateProgress();
    rotateMotivationalMessage();
    
    // Rotate motivational messages every 5 seconds
    setInterval(rotateMotivationalMessage, 5000);
}

function setupEventListeners() {
    // Navigation
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const section = this.dataset.section;
            showSection(section);
            updateActiveNavBtn(this);
        });
    });

    // Day selector
    document.querySelectorAll('.day-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            currentDay = this.dataset.day;
            updateActiveDayBtn(this);
            updateMealDisplay();
        });
    });

    // Profile form changes
    const profileInputs = document.querySelectorAll('#profile input, #profile select');
    profileInputs.forEach(input => {
        input.addEventListener('change', updateUserProfile);
    });
}

function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Show selected section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
        currentSection = sectionId;
        
        // Update charts when showing progress section
        if (sectionId === 'progress') {
            setTimeout(updateCharts, 100);
        }
        
        // Update dashboard when showing dashboard
        if (sectionId === 'dashboard') {
            updateDashboard();
        }
    }
}

function updateActiveNavBtn(activeBtn) {
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    activeBtn.classList.add('active');
}

function updateActiveDayBtn(activeBtn) {
    document.querySelectorAll('.day-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    activeBtn.classList.add('active');
}

function startApp() {
    showSection('dashboard');
    updateActiveNavBtn(document.querySelector('[data-section="dashboard"]'));
    showNotification("Welcome to NutriFlow! Let's start your healthy journey! 🚀");
}

function updateDashboard() {
    // Update calories
    const caloriesEaten = document.getElementById('caloriesEaten');
    if (caloriesEaten) {
        caloriesEaten.textContent = currentUser.totalCalories.toLocaleString();
    }

    // Update today's meals
    updateTodaysMeals();
    
    // Update achievements
    updateAchievements();
    
    // Update progress chart
    updateProgressChart();
}

function updateTodaysMeals() {
    const todayMealsContainer = document.getElementById('todayMeals');
    if (!todayMealsContainer) return;

    const meals = sampleData.sampleMealPlans[currentDay];
    todayMealsContainer.innerHTML = '';

    Object.keys(meals).forEach(mealType => {
        const meal = meals[mealType];
        const mealItem = document.createElement('div');
        mealItem.className = 'meal-item';
        mealItem.innerHTML = `
            <span class="meal-name">${meal.name}</span>
            <span class="meal-calories">${meal.calories} cal</span>
        `;
        todayMealsContainer.appendChild(mealItem);
    });
}

function updateAchievements() {
    const achievementsContainer = document.getElementById('achievements');
    if (!achievementsContainer) return;

    achievementsContainer.innerHTML = '';
    
    sampleData.achievements.slice(0, 4).forEach(achievement => {
        const achievementEl = document.createElement('div');
        achievementEl.className = `achievement ${achievement.unlocked ? 'unlocked' : ''}`;
        achievementEl.innerHTML = `
            <div class="achievement-icon">${achievement.icon}</div>
            <div class="achievement-name">${achievement.name}</div>
        `;
        achievementsContainer.appendChild(achievementEl);
    });
}

function updateMealDisplay() {
    const mealsContainer = document.getElementById('mealsContainer');
    if (!mealsContainer) return;

    const meals = sampleData.sampleMealPlans[currentDay];
    mealsContainer.innerHTML = '';

    Object.keys(meals).forEach(mealType => {
        const meal = meals[mealType];
        const mealCard = document.createElement('div');
        mealCard.className = 'meal-card';
        mealCard.innerHTML = `
            <div class="meal-type">${mealType}</div>
            <div class="meal-name">${meal.name}</div>
            <div class="meal-macros">
                <span>🔥 ${meal.calories}</span>
                <span>💪 ${meal.protein}g</span>
                <span>🌾 ${meal.carbs}g</span>
                <span>🥑 ${meal.fat}g</span>
            </div>
        `;
        mealsContainer.appendChild(mealCard);
    });
}

function updateGroceryList() {
    const groceryContainer = document.getElementById('groceryList');
    if (!groceryContainer) return;

    groceryContainer.innerHTML = '';

    Object.keys(sampleData.groceryCategories).forEach(category => {
        const items = sampleData.groceryCategories[category];
        const categoryEl = document.createElement('div');
        categoryEl.className = 'grocery-category';
        
        const itemsList = items.map(item => `<li>${item}</li>`).join('');
        
        categoryEl.innerHTML = `
            <div class="category-title">${category}</div>
            <ul class="grocery-items">${itemsList}</ul>
        `;
        groceryContainer.appendChild(categoryEl);
    });
}

function updateProgress() {
    // Update goal metrics
    const proteinFill = document.querySelector('.metric:nth-child(1) .metric-fill');
    const carbFill = document.querySelector('.metric:nth-child(2) .metric-fill');
    const fatFill = document.querySelector('.metric:nth-child(3) .metric-fill');

    if (proteinFill) proteinFill.style.width = '85%';
    if (carbFill) carbFill.style.width = '72%';
    if (fatFill) fatFill.style.width = '90%';
}

function updateCharts() {
    updateProgressChart();
    updateNutritionChart();
    updateWeeklyChart();
}

function updateProgressChart() {
    const canvas = document.getElementById('progressChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    
    // Clear previous chart
    Chart.getChart(canvas)?.destroy();
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [68, 32],
                backgroundColor: ['#4CAF50', '#e0e0e0'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            cutout: '70%',
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function updateNutritionChart() {
    const canvas = document.getElementById('nutritionChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    
    // Clear previous chart
    Chart.getChart(canvas)?.destroy();
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Protein', 'Carbs', 'Fat', 'Fiber'],
            datasets: [{
                label: 'Grams',
                data: [102, 144, 63, 22],
                backgroundColor: [
                    '#FF6B35',
                    '#4CAF50',
                    '#667eea',
                    '#764ba2'
                ],
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function updateWeeklyChart() {
    const canvas = document.getElementById('weeklyChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    
    // Clear previous chart
    Chart.getChart(canvas)?.destroy();
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Calories',
                data: [1750, 1820, 1680, 1890, 1760, 1950, 1700],
                borderColor: '#4CAF50',
                backgroundColor: 'rgba(76, 175, 80, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    min: 1500,
                    max: 2000
                }
            }
        }
    });
}

function regenerateMealPlan() {
    showNotification("🤖 AI is generating your new meal plan...");
    
    // Simulate AI processing
    setTimeout(() => {
        // Shuffle meals for demo
        shuffleMealPlan();
        updateMealDisplay();
        updateGroceryList();
        showNotification("✨ New meal plan generated! Optimized for your goals!");
    }, 2000);
}

function shuffleMealPlan() {
    // Simple meal shuffling for demo purposes
    const mealOptions = {
        breakfast: [
            {name: "Greek Yogurt Bowl", calories: 320, protein: 20, carbs: 25, fat: 12},
            {name: "Oatmeal with Berries", calories: 280, protein: 12, carbs: 45, fat: 8},
            {name: "Avocado Toast", calories: 300, protein: 12, carbs: 30, fat: 18},
            {name: "Smoothie Bowl", calories: 290, protein: 15, carbs: 35, fat: 12}
        ],
        lunch: [
            {name: "Quinoa Salad", calories: 450, protein: 15, carbs: 60, fat: 16},
            {name: "Turkey Wrap", calories: 420, protein: 25, carbs: 35, fat: 18},
            {name: "Buddha Bowl", calories: 420, protein: 20, carbs: 45, fat: 18},
            {name: "Chicken Caesar Salad", calories: 380, protein: 30, carbs: 15, fat: 22}
        ],
        dinner: [
            {name: "Grilled Salmon", calories: 380, protein: 35, carbs: 15, fat: 22},
            {name: "Chicken Stir-fry", calories: 400, protein: 30, carbs: 25, fat: 20},
            {name: "Beef & Vegetables", calories: 450, protein: 35, carbs: 20, fat: 25},
            {name: "Grilled Chicken", calories: 370, protein: 35, carbs: 12, fat: 18}
        ],
        snack: [
            {name: "Apple & Almonds", calories: 180, protein: 6, carbs: 20, fat: 10},
            {name: "Protein Smoothie", calories: 200, protein: 15, carbs: 18, fat: 8},
            {name: "Greek Yogurt", calories: 120, protein: 12, carbs: 8, fat: 5},
            {name: "Mixed Nuts", calories: 160, protein: 6, carbs: 8, fat: 14}
        ]
    };

    // Update current day with random selections
    Object.keys(mealOptions).forEach(mealType => {
        const options = mealOptions[mealType];
        const randomMeal = options[Math.floor(Math.random() * options.length)];
        sampleData.sampleMealPlans[currentDay][mealType] = randomMeal;
    });
}

function rotateMotivationalMessage() {
    const motivationEl = document.getElementById('motivationMsg');
    if (!motivationEl) return;

    const messages = sampleData.motivationalMessages;
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    
    motivationEl.style.opacity = '0';
    setTimeout(() => {
        motivationEl.textContent = `"${randomMessage}"`;
        motivationEl.style.opacity = '1';
    }, 300);
}

function updateUserProfile() {
    const age = document.getElementById('age')?.value;
    const weight = document.getElementById('weight')?.value;
    const goal = document.getElementById('goal')?.value;

    if (age) currentUser.age = parseInt(age);
    if (weight) currentUser.weight = parseInt(weight);
    if (goal) currentUser.goal = goal;

    showNotification("Profile updated! Your meal plans will be adjusted accordingly. 📝");
}

function showNotification(message) {
    const notification = document.getElementById('notification');
    if (!notification) return;

    notification.textContent = message;
    notification.classList.add('show');

    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// Export functionality (placeholder)
function exportGroceryList() {
    showNotification("📄 Grocery list exported! Check your downloads folder.");
}

// Add click event for export button
document.addEventListener('DOMContentLoaded', function() {
    const exportBtn = document.querySelector('.export-btn');
    if (exportBtn) {
        exportBtn.addEventListener('click', exportGroceryList);
    }
});

// Simulate real-time updates
setInterval(() => {
    if (currentSection === 'dashboard') {
        // Simulate small changes in calories
        currentUser.totalCalories += Math.floor(Math.random() * 50) - 25;
        if (currentUser.totalCalories < 1000) currentUser.totalCalories = 1000;
        if (currentUser.totalCalories > 2000) currentUser.totalCalories = 2000;
        
        const caloriesEl = document.getElementById('caloriesEaten');
        if (caloriesEl) {
            caloriesEl.textContent = currentUser.totalCalories.toLocaleString();
        }
    }
}, 10000); // Update every 10 seconds

// Add some interactive animations
document.addEventListener('DOMContentLoaded', function() {
    // Add hover effects to cards
    document.querySelectorAll('.card, .feature-card, .meal-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});'''

# Save JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("JavaScript file created successfully!")
print("File size:", len(js_content), "characters")
print("\\nAll files created:")
print("1. index.html")
print("2. style.css") 
print("3. app.js")
print("\\nYour Premium Diet Scheduler MVP is ready for presentation!")