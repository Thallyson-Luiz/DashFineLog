document.getElementById('coinpage').classList.add('active');

// obtendo o gráfico cripto
const coinView = document.getElementById("coinView").getContext("2d");

// Função assíncrona para obter os dados de data e preço do bitcoin
async function getDailyBids(ticker, days) {
    try {
        // Monta a URL da API
        const url = `https://economia.awesomeapi.com.br/json/daily/${ticker}/${days}`;
        console.log(url);
        
        // Faz a requisição
        const response = await fetch(url);
        if (!response.ok) throw new Error('Erro na requisição da API');
        
        // Converte para JSON
        const data = await response.json();
        
        // Extrai os valores de bid
        const bids = data.map(item => parseFloat(item.bid));

        // Retorna do último para o primeiro
        return bids.reverse();
        
    } catch (error) {
        console.error(error);
        return [];
    }
}

// ____________________________________________________________________________________________________________________________________________________

// Função para obter os dias da semana
function getDaysWeek(qtdDias = 1) {
    // Lista com nomes dos dias da semana (começando em segunda)
    const diasSemana = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"];
    
    const hoje = new Date();
    const resultado = [];
    
    for (let i = 0; i < qtdDias; i++) {
        const data = new Date(hoje);
        data.setDate(hoje.getDate() - i); // Subtrai i dias de hoje
        const indice = (data.getDay() + 6) % 7; // Ajuste para segunda=0, domingo=6
        resultado.push(diasSemana[indice]);
    }
    
    return resultado;
}

// ____________________________________________________________________________________________________________________________________________________

let coinChart = null; // gráfico coinView
// função async para inicializar o gráfico
async function initChart_criptoView(request) {
    let [coin_prices, labels_var] = request; // Obtendo dados do backend
    
    // verificando se a api esta ativa
    if (labels_var == null) labels_var = ["seg", "ter", "qua", "qui", "sex", "sab"];
    if (coin_prices == null) coin_prices = [0, 0, 0, 0, 0, 0];
    
    // revertendo os arrays
    labels_var.reverse();
    
    // Criando o gráfico
    if (!coinChart) {
        coinChart = new Chart(coinView, {
            type: "line",
            data: {
                labels: labels_var,
                datasets: [
                    {
                        label: "Vendas",
                        data: coin_prices,
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
                maintainAspectRatio: false,
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
        coinChart.data.labels = labels_var; // Definindo as labels
        coinChart.data.datasets[0].data = coin_prices; // Definindo os dados
        coinChart.update(); // Atualizando o gráfico
    }
}

// Função para direcionar

// ____________________________________________________________________________________________________________________________________________________

// Modal
const modal = document.getElementById('coin-modal');

// Definindo o conteudo do modal
modal.addEventListener('show.bs.modal', async (event) => {
    const triggerModal = event.relatedTarget; // Elemento que acionou o modal
    
    // Definindo o nome da moeda
    const coinname = triggerModal.querySelector('#coinname').textContent.trim(); // Nome da moeda
    modal.querySelector('#modalLabel').textContent = coinname; // Definindo o nome da moeda
    
    // Definindo a variação da moeda
    const variationCoinDay = triggerModal.querySelector('#coinvariation'); // elemento de variação do card
    const modalInfoVariation = modal.querySelector('#modalvariation'); // elemento da variacao do modal
    modalInfoVariation.innerHTML = variationCoinDay.innerHTML; // Definindo a variação
    modalInfoVariation.classList = variationCoinDay.classList; // Definindo a cor da variação
    
    // Definindo o preço
    const priceCoin = triggerModal.querySelector('#coinprice').textContent.trim();
    modal.querySelector('#modalprice').textContent = priceCoin; // Definindo o preço

    // Criando o gráfico
    const coinTicker = coinname.replace("/", "-"); // Criando o ticker
    const selectCoinPrice = await getDailyBids(coinTicker, 7); // Obtendo os preços da moeda
    const daysWeek = getDaysWeek(7); // Obtendo as datas
    const coinPriceAndDaysList = [selectCoinPrice, daysWeek]; // Transformando em uma lista
    initChart_criptoView(coinPriceAndDaysList); // Inicializando o gráfico

    // Definindo o link de exclusão
    const link = modal.querySelector('#exclude-coin');
    link.href = "/my-coins/exclude-coin/" + coinname.replace("/", "-") + "/";
});

// Modal de adicionar moedas
const modalAddCoin = document.querySelector('#add-coin-modal');

// Definindo o conteudo do modal
modalAddCoin.addEventListener('show.bs.modal', async (event) => {
    const triggerModal = event.relatedTarget; // Elemento que acionou o modal

    const btnModalAddCoin = modalAddCoin.querySelector('.btn-modal-coin'); // Botão de adicionar

    // Definindo o link de exclusão
    btnModalAddCoin.addEventListener('click', async () => {
        const ticker = modalAddCoin.querySelector('#ticker').value; // Ticker da moeda
        const tradingPair = modalAddCoin.querySelector('#trading_pair').value; // Trading Pair da moeda

        // adiciona o link ao botão
        btnModalAddCoin.setAttribute('href', `/my-coins/add-coin/${ticker}/${tradingPair}`);

        // aciona o botão
        btnModalAddCoin.click();
    })    
});