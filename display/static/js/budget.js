
const ctx = document.getElementById('doughnutChart').getContext('2d');

const income = 10000;  // Example income value
const expenses = 6000;  // Example expenses value
const profit = income - expenses;

const data = {
    labels: ['Income', 'Profit'],
    datasets: [{
        data: [income, profit],
        backgroundColor: ['#36a2eb', '#4caf50'],
        hoverBackgroundColor: ['#36a2eb', '#4caf50']
    }]
};

const options = {
    responsive: true,
    maintainAspectRatio: false,
    cutoutPercentage: 50,
    plugins: {
        legend: {
            display: false,
            position: 'bottom'
        }
    }
};

new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: options
});

document.querySelectorAll('.action').forEach(object => {
    object.style.width = "1%";
    object.style.border = "none";
    object.style.background = "transparent";
    object.style.cursor = "pointer";
});


document.querySelectorAll(".budget_nav button").forEach(object => {
    object.addEventListener("click", function () {
        document.querySelectorAll(".budget_nav button").forEach(object2 => {
            object2.classList.remove("chosen-nav");
        });
        object.classList.add("chosen-nav");
        if (object.textContent == "Overlook") {
            document.querySelector(".budget-overlook").classList.remove("not-budget");
            document.querySelector(".budget-income").classList.add("not-budget");
            document.querySelector(".budget-expenses").classList.add("not-budget");
        }
        else if (object.textContent == "Income") {
            document.querySelector(".budget-overlook").classList.add("not-budget");
            document.querySelector(".budget-income").classList.remove("not-budget");
            document.querySelector(".budget-expenses").classList.add("not-budget");
        }
        else if (object.textContent == "Expenses") {
            document.querySelector(".budget-overlook").classList.add("not-budget");
            document.querySelector(".budget-income").classList.add("not-budget");
            document.querySelector(".budget-expenses").classList.remove("not-budget");
        }
        else if (object.textContent == "All together") {
            document.querySelector(".budget-overlook").classList.remove("not-budget");
            document.querySelector(".budget-income").classList.remove("not-budget");
            document.querySelector(".budget-expenses").classList.remove("not-budget");
        }
    });
});
