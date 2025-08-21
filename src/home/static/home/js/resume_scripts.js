// AITVANDO RESUME PAGE

const resume = document.getElementById("resumepage");
resume.classList.add("active");

// GRAFICOS

const DOLAR = document.getElementById("dolarview").getContext("2d");

const myChart = new Chart(DOLAR, {
    type: "line",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
            {
                label: "Vendas",
                data: [10, 12, 15, 13, 17, 20], 
                borderColor: "#4e9aff", 
                backgroundColor: "rgba(78, 154, 255, 0.2)", 
                fill: true,
                tension: 0.4, 
                pointBackgroundColor: "#4e9aff", 
                pointRadius: 5,
            },
        ],
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false, 
            },
        },
        scales: {
            x: {
                grid: {
                    display: false, 
                },
                ticks: {
                    color: "white", 
                },
            },
            y: {
                grid: {
                    color: "rgba(255, 255, 255, 0.1)", 
                },
                ticks: {
                    color: "white",
                },
            },
        },
    },
});

// ______________________________________________________________________________________________________________________________________________________

const SELIC = document.getElementById("taxaselicview");

new Chart(SELIC, {
    type: "bar",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
            {
                label: "Série 1",
                data: [150, 250, 280, 300, 350, 370],
                backgroundColor: "#4285F4", 
                borderRadius: 8,
            },
            {
                label: "Série 2",
                data: [140, 160, 200, 210, 250, 260],
                backgroundColor: "#FB8C00", 
                borderRadius: 8,
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false, 
        plugins: {
            legend: {
                display: false, 
            },
        },
        scales: {
            x: {
                grid: {
                    display: false,
                },
                ticks: {
                    color: "#fff",
                },
            },
            y: {
                beginAtZero: true,
                ticks: {
                    color: "#fff",
                },
                grid: {
                    color: "rgba(255,255,255,0.2)", 
                },
            },
        },
    },
});

// ______________________________________________________________________________________________________________________________________________________

const BITCOIN = document.getElementById("bitcoinview");

new Chart(BITCOIN, {
    type: "line",
    data: {
        labels: ["Jan", "Feb", "Mar", "Jun"], 
        datasets: [
            {
                label: "Balance Over Time",
                data: [6000, 8000, 8500, 10000, 11000], 
                borderColor: "#4e9cff",
                backgroundColor: "rgba(78, 154, 255, 0.2)",
                fill: true,
                tension: 0.4, 
                pointRadius: 5,
                pointBackgroundColor: "#4e9cff",
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false, 
            },
            title: {
                display: true,
                text: "Balance Over Time",
                color: "#fff",
                font: {
                    size: 18,
                },
            },
        },
        scales: {
            x: {
                ticks: { color: "#fff" },
                grid: { color: "rgba(255,255,255,0.1)" },
            },
            y: {
                ticks: { color: "#fff" },
                grid: { color: "rgba(255,255,255,0.1)" },
                beginAtZero: true,
            },
        },
    },
});

const ctx = document.getElementById("budgetChart").getContext("2d");
new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["Rent", "Groceries", "Entertainment", "Utilities"],
        datasets: [
            {
                data: [25, 15, 30, 30], 
                backgroundColor: [
                    "rgba(54, 162, 235, 0.8)", 
                    "rgba(255, 159, 64, 0.8)", 
                    "rgba(75, 192, 192, 0.8)", 
                    "rgba(54, 162, 235, 0.5)", 
                ],
                borderColor: ["rgba(255, 255, 255, 0)"],
                borderWidth: 1,
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "right",
                labels: {
                    color: "white", 
                },
            },
        },
    },
});

// adjusts

// Seleciona os dois graficos
const graficOne = document.querySelector(".grafic_one");
const graficTwo = document.querySelector(".grafic_two");

// Reseta a altura para evitar erros de layout
graficOne.style.height = "auto";
graficTwo.style.height = "auto";

// Calcula a altura máxima
const maxHeight = Math.max(graficOne.offsetHeight, graficTwo.offsetHeight);

// Aplica a altura máxima aos dois
graficOne.style.height = maxHeight + "px";
graficTwo.style.height = maxHeight + "px";
