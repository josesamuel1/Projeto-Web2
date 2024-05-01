// Importa o hook useState do React para gerenciar o estado e o hook useNavigate do react-router-dom para navegação entre rotas
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGooglePlusG, faFacebookF } from '@fortawesome/free-brands-svg-icons';


import api from '../api'
import 'bootstrap/dist/css/bootstrap.min.css';

// Importa o arquivo de estilo CSS
import '../styles/Login.css'

// Define o componente Login
function Login() {
  // Define estados para o nome de usuário e senha
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  // Obtém a função de navegação do hook useNavigate
  const navigate = useNavigate()

  // Função para lidar com o envio do formulário de login
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      // Faz uma solicitação POST para a API para obter o token de acesso
      const response = await api.post(`/token/`, { username, password })
      // Armazena o token de acesso no localStorage
      localStorage.setItem('token', response.data.access)
      // Redireciona para a página de listagem de posts após o login bem-sucedido
      navigate('/inicio/')
    } catch (error) {
      // Registra qualquer erro ocorrido ao fazer login
      console.error('Erro ao fazer login:', error)
    }
  }
  // Retorna a interface do componente Login
  return (
    <div>
    <div className="container center">
      <div className="form-container sign-in">
        <form onSubmit={handleSubmit}>
          <h1>Entrar</h1>
          <div className="social-icons">
            <a href="#" className="icon"><FontAwesomeIcon icon={faGooglePlusG} /></a>
            <a href="#" className="icon"><FontAwesomeIcon icon={faFacebookF} /></a>
          </div>
          <span>use seu email e senha</span>
          <input type="text" placeholder="Usuário" value={username} onChange={(e) => setUsername(e.target.value)} />
          <input type="password" placeholder="Senha" value={password} onChange={(e) => setPassword(e.target.value)} />
          <button type="submit">Entrar</button>
        </form>
      </div>
      <div className="toggle-container">
            <div className="toggle">
                <div className="toggle-panel toggle-left">
                    <h1>Olá, bem vindo de volta ao Estoque Center!</h1>
                    <p>Insira seus dados pessoais para usar todos os recursos do site</p>
                    <button href="" id="login">Entrar</button>             
                </div>
                <div className="toggle-panel toggle-right">
                    <h1>Olá, amigo, bem vindo ao Estoque Center!</h1>
                    <p>Registre-se com seus dados pessoais para usar todos os recursos do site</p>
                </div>
            </div>
        </div>
    </div>
    </div>
  )
}
// Exporta o componente Login
export default Login
