import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Transposer from "./pages/Transposer";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/transposer/:mode" element={<Transposer />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
