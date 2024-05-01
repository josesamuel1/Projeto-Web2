// Importa o componente Link do react-router-dom para navegação entre rotas.
import { Link } from 'react-router-dom'

// Importa o arquivo de estilo CSS.
import './navbar.css'


function Navbar() {
    return (
        <header>
            <nav className="navigation">
                <a href="#" className="logo"><span>Estoque</span>Center</a>
                <ul className="nav-menu">
                    <li className="nav-item">
                    <Link to={`/inicio/`} className="produto-link-name">Inicio</Link>
                    </li>
                    <li className="nav-item">
                    <Link to={`/produto/`} className="produto-link-name">Estoque</Link>
                    </li>
                    <li className="nav-item"><a href="#">Clientes</a></li>
                    <li className="nav-item"><a href="#">Relatorio</a></li>
                    <i className='bx bx-search'></i>
                </ul>
            </nav>
        </header>
        )
    }
    export default Navbar
