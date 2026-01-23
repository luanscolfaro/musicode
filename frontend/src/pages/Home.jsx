import { useNavigate } from "react-router-dom";
import "./Home.css";
import Footer from "../components/Footer";

function Home() {
  const navigate = useNavigate();

  return (
    <>
      <div className="container">
        <div
          className="card teclado"
          onClick={() => navigate("/transposer/teclado")}
        >
          <h1>🎹 Teclado</h1>
          <p>Usar transposer</p>
        </div>

        <div
          className="card violao"
          onClick={() => navigate("/transposer/violao")}
        >
          <h1>🎸 Violão</h1>
          <p>Usar capotraste</p>
        </div>
      </div>

      <Footer />
    </>
  );
}

export default Home;
