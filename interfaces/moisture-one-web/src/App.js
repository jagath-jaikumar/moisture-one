import "./App.css";

import { SpeedInsights } from "@vercel/speed-insights/next";
import logo from "./logo.svg";

function App() {
  return (
    <div className="App">
      <SpeedInsights />
      <header className="App-header">
        <p>Moisture one</p>
      </header>
    </div>
  );
}

export default App;
