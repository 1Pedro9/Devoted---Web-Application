function update() {
    let stockData = null;

    let list = null;
    document.querySelectorAll(".main-left>div").forEach(object => {
        if (!object.classList.contains("not-budget")) {
            list = object.querySelector(".stock-list");
        }
        object.querySelector(".stock-list").innerHTML = "";
    });
    if (list.parentElement.classList.contains("stocks")) {
        stockData = [
            { symbol: 'JSE: REM', targetDistance: '20% to target', price: 'ZAC 14,400.20', performance: [14400, 14420, 14380, 14400, 14410, 14450, 14430, 14400] },
            { symbol: 'NASDAQ: AAPL', targetDistance: '10% to target', price: 'USD 150.30', performance: [150, 151, 149, 152, 150, 151, 150, 150.3] },
            { symbol: 'NYSE: TSLA', targetDistance: '5% to target', price: 'USD 720.50', performance: [710, 715, 720, 725, 720, 715, 710, 720.5] }
        ];
    }
    else if (list.parentElement.classList.contains("crypto")) {
        stockData = [
            { symbol: 'Bitcoin', targetDistance: '20% to target', price: 'ZAC 14,400.20', performance: [14400, 14420, 14380, 14400, 14410, 14450, 14430, 14400] },
            { symbol: 'Etherium', targetDistance: '10% to target', price: 'USD 150.30', performance: [150, 151, 149, 152, 150, 151, 150, 150.3] },
            { symbol: 'NYSE: TSLA', targetDistance: '5% to target', price: 'USD 720.50', performance: [710, 715, 720, 725, 720, 715, 710, 720.5] }
        ];
    }
    else {
        stockData = []
    }

    const stockList = document.querySelector('.stock-list');

    stockData.forEach((stock, index) => {
        const li = document.createElement('li');

        const canvas = document.createElement('canvas');
        canvas.classList.add(`stockChart${index}`);
        canvas.width = 50;
        canvas.height = 50;
        li.appendChild(canvas);

        const h4 = document.createElement('h4');
        h4.textContent = stock.symbol;
        li.appendChild(h4);

        const targetDistance = document.createElement('p');
        targetDistance.className = 'buy-distance';
        targetDistance.textContent = stock.targetDistance;
        li.appendChild(targetDistance);

        const price = document.createElement('p');
        price.className = 'stock-price';
        price.textContent = stock.price;
        li.appendChild(price);

        const moreIcon = document.createElement('span');
        moreIcon.className = 'material-symbols-outlined';
        moreIcon.textContent = 'more_vert';
        li.appendChild(moreIcon);

        list.appendChild(li);

        const ctx = document.querySelector(`.stockChart${index}`).getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM'],
                datasets: [{
                    label: 'Stock Performance',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    data: stock.performance
                }]
            },
            options: {
                responsive: false,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        display: false
                    },
                    y: {
                        display: false
                    }
                },
                elements: {
                    point: {
                        radius: 0
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    });
    update_li();
}

update();
document.querySelectorAll(".budget_nav button").forEach(object => {
    object.addEventListener("click", function () {
        document.querySelectorAll(".budget_nav button").forEach(object2 => {
            object2.classList.remove("chosen-nav");
        });
        object.classList.add("chosen-nav");
        if (object.textContent == "Stocks") {
            document.querySelector(".stocks").classList.remove("not-budget");
            document.querySelector(".crypto").classList.add("not-budget");
            document.querySelector(".realestate").classList.add("not-budget");
        }
        else if (object.textContent == "Crypto") {
            document.querySelector(".crypto").classList.remove("not-budget");
            document.querySelector(".stocks").classList.add("not-budget");
            document.querySelector(".realestate").classList.add("not-budget");
        }
        else if (object.textContent == "Real Estate") {
            document.querySelector(".crypto").classList.add("not-budget");
            document.querySelector(".stocks").classList.add("not-budget");
            document.querySelector(".realestate").classList.remove("not-budget");
        }
        else if (object.textContent == "Overview") {
            document.querySelector(".overview").classList.remove("not-budget");
            document.querySelector(".add").classList.add("not-budget");
            document.querySelector(".edit").classList.add("not-budget");
        }
        else if (object.textContent == "Add") {
            document.querySelector(".overview").classList.add("not-budget");
            document.querySelector(".add").classList.remove("not-budget");
            document.querySelector(".edit").classList.add("not-budget");
        }
        else if (object.textContent == "Edit") {
            document.querySelector(".overview").classList.add("not-budget");
            document.querySelector(".add").classList.add("not-budget");
            document.querySelector(".edit").classList.remove("not-budget");
        }
        update();
    });
});

function update_li() {
    document.querySelectorAll(".stock-list li").forEach(object => {
        object.addEventListener("click", function () {
            document.querySelectorAll(".stock-list li").forEach(object => {
                object.classList.remove("chosen-li");
            });
            object.classList.add("chosen-li");
        });
    });
}

document.querySelectorAll("input[type='checkbox']").forEach(object => {
    object.addEventListener("click", function () {
        document.querySelectorAll("input[type='checkbox']").forEach(object2 => {
            if (object != object2) {
                object2.checked = false;
            }
        });
        object.cheked = true;
    });
});