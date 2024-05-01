import Navbar from '../navbar/Navbar'
import './inicio.css'

const Inicio = () => {
    return (
        <div>
            <Navbar></Navbar>
        <section className="home">
            <div className="home-text">
                <h4 className="text-h4">Olá! Bem Vindo, ao Estoque Center</h4>
                <h1 className="text-h1">Controle de Estoque</h1>
                <p>Gerencie eficientemente o estoque da sua empresa, evitando desperdícios e falta de produtos. Preveja vendas,controle logística e organize entrada e saída de mercadorias.</p> 
            </div>
            <div className="home-img">
                <img src="/public/imagens/logo.png" alt="logo"></img>
            </div>
        </section>
    </div>
    )
}

export default Inicio