
document.querySelector(".gl").querySelectorAll("td").forEach(object => {
    if (object.textContent == "" && !object.parentElement.classList.contains("bf")) {
        object.style.background = "transparent";
        object.style.border = "none";
    }
});

document.querySelectorAll(".budget_nav button").forEach(object => {
    object.addEventListener("click", function () {
        document.querySelectorAll(".budget_nav button").forEach(object2 => {
            object2.classList.remove("chosen-nav");
        });
        object.classList.add("chosen-nav");
        if (object.textContent == "General Ledger") {
            document.querySelector(".gl").classList.remove("not-budget");
            document.querySelector(".journal").classList.add("not-budget");
        }
        else if (object.textContent == "CRJ") {
            document.querySelector(".gl").classList.add("not-budget");
            document.querySelector(".journal").classList.add("not-budget");
            document.querySelector(".crj").classList.remove("not-budget");
        }
        else if (object.textContent == "CPJ") {
            document.querySelector(".gl").classList.add("not-budget");
            document.querySelector(".journal").classList.add("not-budget");
            document.querySelector(".cpj").classList.remove("not-budget");
        }
    });
});

document.querySelectorAll(".activities_nav button").forEach(object => {
    object.addEventListener("click", function () {
        document.querySelectorAll(".activities_nav button").forEach(object2 => {
            object2.classList.remove("chosen-nav");
        });
        object.classList.add("chosen-nav");
        if (object.textContent == "Favourite") {
            document.querySelector(".recent-activities").classList.remove("not-budget");
            document.querySelector(".categories").classList.add("not-budget");
        }
        else {
            document.querySelector(".recent-activities").classList.add("not-budget");
            document.querySelector(".categories").classList.remove("not-budget");
        }
    });
});