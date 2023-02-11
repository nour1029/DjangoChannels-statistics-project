

const slug = document.getElementById('dashboard-slug').textContent.trim();
const user = document.getElementById('user').textContent.trim();

const dataItem = document.getElementById('dataitem');
const submitBtn = document.getElementById('submit-btn');

const dataBox = document.getElementById('data-box');


const socket = new WebSocket('ws://' + window.location.host + `/ws/${slug}/`);
console.log(socket);





socket.onmessage = function(e) {
    console.log('Server: ' + e.data)
    const {sender, message} = JSON.parse(e.data)

    dataBox.innerHTML += `<p>${sender} : ${message}</p>`
    updateChart()
};




submitBtn.addEventListener('click', ()=> {
    let dataItemValue = dataItem.value
    socket.send(JSON.stringify({
        'message' : dataItemValue,
        'sender' : user,
    }));
});




const fetchChartData = async() => {
    const response = await fetch(window.location.href + 'chart/');
    const data = await response.json()
    return data
}

let chart;

const ctx = document.getElementById('myChart');

const drawChart = async () => {
    const data = await fetchChartData();
    const {chart_labels, chart_data} = data;



    chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: chart_labels,
            datasets: [{
            label: '# of Votes',
            data: chart_data,
            borderWidth: 1
        }]
        },
        options: {
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
    });
}


const updateChart = async() => {
    console.log(chart);
    if (chart){
        chart.destroy()
    }

    await drawChart()
}

drawChart()