import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function LineChart() {
  const data = {
    labels: ["10AM", "11AM", "12PM", "1PM", "2PM"],
    datasets: [
      {
        label: "Violations",
        data: [1, 3, 5, 2, 6],
        borderColor: "red",
        tension: 0.4
      }
    ]
  };

  return <Line data={data} />;
}
