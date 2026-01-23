import "./Footer.css";
import { FaLinkedin, FaGithub, FaInstagram } from "react-icons/fa";

function Footer() {
  return (
    <footer className="footer">
      <span className="author">Desenvolvido por Luan Scolfaro</span>
      <a
        href="https://www.linkedin.com/in/luan-scolfaro-124498336/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <FaLinkedin size={20} />
      </a>
      <a
        href="https://github.com/luanscolfaro"
        target="_blank"
        rel="noopener noreferrer"
      >
        <FaGithub size={20} />
      </a>
      <a
        href="https://www.instagram.com/seu_usuario_aqui/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <FaInstagram size={20} />
      </a>
    </footer>
  );
}

export default Footer;
