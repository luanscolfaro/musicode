import { useParams } from "react-router-dom";
import { useState } from "react";
import "./Transposer.css";
import { useNavigate } from "react-router-dom";
import Footer from "../components/Footer";

const NOTES = [
  "C",
  "C#",
  "Db",
  "D",
  "D#",
  "Eb",
  "E",
  "F",
  "F#",
  "Gb",
  "G",
  "G#",
  "Ab",
  "A",
  "A#",
  "Bb",
  "B",
];

function Transposer() {
  const { mode } = useParams();
  const navigate = useNavigate();

  const [original, setOriginal] = useState("C");
  const [target, setTarget] = useState("C");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const calculate = async () => {
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("https://musicode-6u9c.onrender.com/api/calculate/", {
      // const response = await fetch("http://127.0.0.1:8000/api/calculate/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ original, target }),
      });

      const data = await response.json();
      setResult(data);
    } catch {
      alert("Erro ao conectar com o servidor");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="page"
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
      }}
    >
    <div className="bnt-voltar" onClick={() => navigate("https://musicode-frontend.onrender.com")}>voltar</div>
      <div
        style={{
          flex: 1,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div className="card-box">
          <h1>
            {mode === "teclado"
              ? "🎹 Transposer do Teclado"
              : "🎸 Capotraste do Violão"}
          </h1>

          <div className="label">Nota original</div>
          <select value={original} onChange={(e) => setOriginal(e.target.value)}>
            {NOTES.map((note) => (
              <option key={note} value={note}>
                {note}
              </option>
            ))}
          </select>

          <div className="label">Nota desejada</div>
          <select value={target} onChange={(e) => setTarget(e.target.value)}>
            {NOTES.map((note) => (
              <option key={note} value={note}>
                {note}
              </option>
            ))}
          </select>

          <button onClick={calculate} disabled={loading}>
            {loading ? "Calculando..." : "Calcular"}
          </button>

          {result && (
            <div className="result">
              {mode === "teclado" && (
                <h2>
                  {result.transposer > 0
                    ? `+${result.transposer}`
                    : result.transposer}
                </h2>
              )}

              {mode === "violao" && <h2>Casa {result.capo}</h2>}

              <p>
                {result.semitons === 0
                  ? "Não é necessário transpor"
                  : `Você está ${
                      result.semitons > 0 ? "subindo" : "descendo"
                    } ${Math.abs(result.semitons)} semitons`}
              </p>

              <p>
                <strong>Tonalidade resultante:</strong> {result.new_key}
              </p>
            </div>
          )}
        </div>
      </div>

      <Footer />
    </div>
  );
}

export default Transposer;
