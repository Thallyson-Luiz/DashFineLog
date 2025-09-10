// AITVANDO RESUME PAGE

const resume = document.getElementById("resumepage");
resume.classList.add("active");


// função async para obter os dados de data e preço do dolar
// para o gráfico dolarview
async function get_data_week_coin(url, days = 6) {
    try {
        const response = await fetch(url + days);
        if (!response.ok) throw new Error("Erro ao obter os dados do backend" + response.status);

        const data = await response.json();

        return Object.values(data);
    } catch (error) {
        return null;
    }
}

// obtendo o gráfico dolarview
const DOLAR = document.getElementById("dolarview").getContext("2d");

let dolarChart = null; // gráfico dolarview

// função async para inicializar o gráfico
async function initChart_DolarView(requestDolarApi) {
    let [dolar_prices, labels_var] = requestDolarApi; // Obtendo dados do backend
    
    // verificando se a api esta ativa
    if (labels_var == null) labels_var = ["seg", "ter", "qua", "qui", "sex", "sab"];
    if (dolar_prices == null) dolar_prices = [0, 0, 0, 0, 0, 0];
    
    // revertendo os arrays
    dolar_prices.reverse();
    labels_var.reverse();
    
    // Criando o gráfico
    if (!dolarChart) {
        dolarChart = new Chart(DOLAR, {
            type: "line",
            data: {
                labels: labels_var,
                datasets: [
                    {
                        label: "Vendas",
                        data: dolar_prices,
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
                    legend: { display: false },
                },
                scales: {
                    x: { grid: { display: false }, ticks: { color: "white" } },
                    y: { grid: { color: "rgba(255, 255, 255, 0.1)" }, ticks: { color: "white" } },
                },
            },
        });
    }
    // se o grafico ja existir, ele apenas o atualizara,
    // sem precisar ser criado novamente
    else {
        dolarChart.data.labels = labels_var; // Definindo as labels
        dolarChart.data.datasets[0].data = dolar_prices; // Definindo os dados
        dolarChart.update(); // Atualizando o gráfico
    }
}

// ______________________________________________________________________________________________________________________________________________________

// função async para obter os dados de data e preço do bitcoin
// para o gráfico bitcoinview

const BITCOIN = document.getElementById("bitcoinview").getContext("2d");
let bitcoinChart = null; // gráfico bitcoinview

async function initChart_BitcoinView(requestBitcoinApi) {
    let [bitcoin_prices, days_week] = requestBitcoinApi; // Obtendo dados do backend
    
    // verificando se a api esta ativa
    if (days_week == null) days_week = ["seg", "ter", "qua", "qui"];
    if (bitcoin_prices == null) bitcoin_prices = [0, 0, 0, 0, 0];
    
    // revertendo os arrays
    bitcoin_prices.reverse();
    days_week.reverse();
    
    // Criando o gráfico
    if (!bitcoinChart) {
        bitcoinChart = new Chart(BITCOIN, {
            type: "line",
            data: {
                labels: days_week,
                datasets: [
                    {
                        label: "Balance Over Time",
                        data: bitcoin_prices,
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
                        beginAtZero: false,
                    },
                },
            },
        });
    }
    // se o grafico ja existir, ele apenas o atualizara,
    // sem precisar ser criado novamente
    else {
        bitcoinChart.data.labels = days_week; // Definindo as labels
        bitcoinChart.data.datasets[0].data = bitcoin_prices; // Definindo os dados
        bitcoinChart.update(); // Atualizando o gráfico
    }
}

// ______________________________________________________________________________________________________________________________________________________

const INFLACAO = document.getElementById("inflacaoview").getContext("2d");

// Inicializando grafico inflacao
let inflacaoChart = null;

// Criando o gráfico
async function initChart_InflacaoView(requestIpcaApi, requestInpcApi) {
    let [ipca_avarage, months] = requestIpcaApi; // Obtendo dados backend do ipca
    
    let [inpc_avarage] = requestInpcApi; // Obtendo dados backend do inpc
    
    // verificando se a api esta ativa
    if (ipca_avarage == null) ipca_avarage = [0, 0, 0, 0, 0, 0];
    if (inpc_avarage == null) inpc_avarage = [0, 0, 0, 0, 0, 0];
    if (months == null) months = ["abr", "mai", "jun", "jul", "ago", "set"];
    
    // revertendo os arrays
    ipca_avarage.reverse();
    inpc_avarage.reverse();
    months.reverse();
    
    // Criando o gráfico
    if (!inflacaoChart) {
        inflacaoChart = new Chart(INFLACAO, {
            type: "bar",
            data: {
                labels: months,
                datasets: [
                    {
                        label: "IPCA",
                        data: ipca_avarage,
                        backgroundColor: "#4285F4",
                        borderRadius: 8,
                    },
                    {
                        label: "IPNC",
                        data: inpc_avarage,
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
    }
    // se o grafico ja existir, ele apenas o atualizara,
    // sem precisar ser criado novamente
    else {
        inflacaoChart.data.labels = months; // Definindo as labels
        inflacaoChart.data.datasets[0].data = ipca_avarage; // Definindo os dados
        inflacaoChart.update(); // Atualizando o gráfico
    }
}

// ______________________________________________________________________________________________________________________________________________________

const selicview = document.getElementById("selicview").getContext("2d");
let selicChart = null; // variavel para armazenar o grafico

async function initChart_SelicView(requestSelicApi) {
    let [selic_prices, months] = requestSelicApi; // Obtendo dados do backend
    
    // verificando se a api esta ativa
    if (selic_prices == null) selic_prices = [0, 0, 0, 0];
    if (months == null) months = ["abr", "mai", "jun", "jul"];
    
    // revertendo os arrays
    months.reverse();
    
    // Criando o gráfico
    if (!selicChart) {
        selicChart = new Chart(selicview, {
            type: "bar",
            data: {
                labels: months,
                datasets: [
                    {
                        data: selic_prices,
                        backgroundColor: [
                            "rgba(54, 163, 235, 1)",
                            "rgba(255, 141, 27, 1)",
                            "rgba(75, 192, 192, 1)",
                            "rgba(54, 163, 235, 1)",
                        ],
                        borderColor: ["rgba(255, 255, 255, 0)"],
                        borderWidth: 1,
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
                        labels: {
                            color: "white",
                        },
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
    }
    // se o grafico ja existir, ele apenas o atualizara,
    // sem precisar ser criado novamente
    else {
        selicChart.data.labels = ["Rent", "Groceries", "Entertainment", "Utilities"]; // Definindo as labels
        selicChart.data.datasets[0].data = [25, 15, 30, 30]; // Definindo os dados
        selicChart.update(); // Atualizando o gráfico
    }
}

// Inicializando os gráficos
const hostGrafics = window.API_BASE_URL || 'http://127.0.0.1:8000'

async function initCharts() {
    try {
        
        // Obtendo os dados do backend
        const requestSelicApi = await get_data_week_coin(`${hostGrafics}/api/get/selic/months/`, 4);
        const requestIpcaApi = await get_data_week_coin(`${hostGrafics}/api/get/ipca/months/`, 6);
        const requestInpcApi = await get_data_week_coin(`${hostGrafics}/api/get/inpc/months/`, 6);
        const requestBitcoinApi = await get_data_week_coin(`${hostGrafics}/api/get/bitcoin/days/`, 5);
        const requestDolarApi = await get_data_week_coin(`${hostGrafics}/api/get/dolar/days/`, 4);
        
        // Iniciando os gráficos
        initChart_InflacaoView(requestIpcaApi, requestInpcApi);
        initChart_SelicView(requestSelicApi);
        initChart_BitcoinView(requestBitcoinApi);
        initChart_DolarView(requestDolarApi);
    } catch (error) {
        alert("Ocorreu um erro ao carregar os gráficos. Por favor, tente novamente mais tarde.");
    }
    
    // mostra a pagina
    loader.style.display = 'none'; // esconde loader
    document.querySelector('.finelog-title').classList.add('slide-in-left');
    document.querySelector('#navbarNav').classList.add('slide-in-top');
    document.querySelector('.btn-person').classList.add('slide-in-right');
}

initCharts();

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

// Sessão para atualizar graficos

const intervalo = 1000 * 60 * 5; // 5 minutos

setInterval(initChart_DolarView, intervalo);
setInterval(initChart_BitcoinView, intervalo);
setInterval(initChart_InflacaoView, intervalo);
setInterval(initChart_SelicView, intervalo);
