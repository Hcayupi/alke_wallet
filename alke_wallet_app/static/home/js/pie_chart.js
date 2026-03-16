document.addEventListener("DOMContentLoaded", function () {
  cargarPieChart();
});

function cargarPieChart() {
  fetch("/api/distribucion/")
    .then((response) => response.json())
    .then((data) => {
      renderizarPieChart(data);
    })
    .catch((error) => {
      console.error("Error cargando gráfico:", error);
    });
}

function renderizarPieChart(data) {
  const ctx = document.getElementById("distribucion-chart");
  
  if (!ctx) return;

  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: data.labels,
      datasets: [
        {
          data: data.data,
          backgroundColor: ["#0d6efd", "#20c997", "#ffc107", "#dc3545"],
          borderColor: "#ffffff",
          borderWidth: 2,
        },
      ],
    },
    options: getPieChartOptions(),
  });
}

function getPieChartOptions() {
  return {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "left",
      },
    },
  };
}
