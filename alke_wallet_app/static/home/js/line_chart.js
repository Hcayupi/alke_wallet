document.addEventListener("DOMContentLoaded", function () {
  cargarEvolucionLineChart();
});

function cargarEvolucionLineChart() {
  fetch("/api/evolucion/")
    .then((response) => response.json())
    .then((data) => {
      renderizarLineChart(data);
    })
    .catch((error) => {
      console.error("Error cargando gráfico:", error);
    });
}

function renderizarLineChart(data) {
  const ctx = document.getElementById("evolucion-chart");

  if (!ctx) return;

  new Chart(ctx, {
    type: "line",
    data: {
      labels: data.labels,
      datasets: [
        {
          label: "Ingresos",
          data: data.ingresos,
          borderColor: "#0d6efd",
          backgroundColor: "rgba(13,110,253,0.1)",
          tension: 0.4,
          fill: true,
        },
        {
          label: "Gastos",
          data: data.gastos,
          borderColor: "#dc3545",
          backgroundColor: "rgba(220,53,69,0.1)",
          tension: 0.4,
          fill: true,
        },
      ],
    },
    options: getLineChartOptions(),
  });
}

function getLineChartOptions() {
  return {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: "index",
      intersect: false,
    },
    plugins: {
      legend: {
        position: "top",
      },
    },
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };
}
