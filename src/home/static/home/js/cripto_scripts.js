document.querySelector('#criptopage').classList.add('active'); // Ativando aba cripto

// obtendo o gráfico cripto
const criptocoin = document.getElementById("criptoView").getContext("2d");

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

let criptoChart = null; // gráfico criptocoin
// função async para inicializar o gráfico
async function initChart_criptoView(request) {
    let [cripto_prices, labels_var] = request; // Obtendo dados do backend
    
    // verificando se a api esta ativa
    if (labels_var == null) labels_var = ["seg", "ter", "qua", "qui", "sex", "sab"];
    if (cripto_prices == null) cripto_prices = [0, 0, 0, 0, 0, 0];
    
    // revertendo os arrays
    labels_var.reverse();
    
    // Criando o gráfico
    if (!criptoChart) {
        criptoChart = new Chart(criptocoin, {
            type: "line",
            data: {
                labels: labels_var,
                datasets: [
                    {
                        label: "Vendas",
                        data: cripto_prices,
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
        criptoChart.data.labels = labels_var; // Definindo as labels
        criptoChart.data.datasets[0].data = cripto_prices; // Definindo os dados
        criptoChart.update(); // Atualizando o gráfico
    }
}

// ____________________________________________________________________________________________________________________________________________________

// Modal de criptomoedas
const modalCrypto = document.getElementById('cripto-modal');

// Definindo o conteudo do modal
modalCrypto.addEventListener('show.bs.modal', async (event) => {
    const triggerModal = event.relatedTarget; // Elemento que acionou o modal
    
    const coinname = triggerModal.querySelector('h3').textContent; // Nome da moeda
    modalCrypto.querySelector('#modalLabel').textContent = coinname; // Definindo o nome da moeda
    const [coinprice, coinvariation] = triggerModal.querySelectorAll('p'); // Preço e variação da moeda
    modalCrypto.querySelector('#modalprice').textContent = coinprice.textContent; // Definindo o preço
    modalCrypto.querySelector('#modalvariation').innerHTML = coinvariation.innerHTML; // Definindo a variação
    modalCrypto.querySelector('#modalvariation').classList.add(...coinvariation.classList); // Definindo a cor da variação

    // Criando o gráfico
    const coinTicker = coinname.replace("/", "-"); // Criando o ticker
    const criptoCoinPrice = await getDailyBids(coinTicker, 7); // Obtendo os preços da moeda
    const daysWeek = getDaysWeek(7); // Obtendo as datas
    const criptoPriceAndDaysList = [criptoCoinPrice, daysWeek]; // Transformando em uma lista
    initChart_criptoView(criptoPriceAndDaysList); // Inicializando o gráfico

    const btnAddCoin = modalCrypto.querySelector('#btnAddCoin'); // Botão de adicionar
    btnAddCoin.setAttribute('href', `/my-coins/add-coin/${coinname}`);
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