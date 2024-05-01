// Importa os hooks useState e useEffect do React para gerenciar o estado e efeitos colaterais, respectivamente,
// e o módulo api para fazer solicitações HTTP.
import { useState, useEffect } from 'react'
import api from '../api'

// Importa o componente Link do react-router-dom para navegação entre rotas.
import { Link } from 'react-router-dom'

// Importa o arquivo de estilo CSS.
import '../styles/ProdutoList.css'
import Navbar from './navbar/Navbar'

// Define o componente ProdutoList como uma função
function ProdutoList() {
  // Define o estado produtos com useState, inicializado como um array vazio
  const [produtos, setProdutos] = useState([])

  // Função para lidar com a exclusão de um produto
  const handleDelete = async (produtoId) => {
    try {
      // Faz uma solicitação DELETE para a API para excluir o produto com o ID fornecido
      await api.delete(`/produto/${produtoId}/`)
      
      // Atualiza o estado dos produtos, removendo o produto excluído
      const updatedProdutos = produtos.filter(produto => produto.id !== produtoId);
      setProdutos(updatedProdutos);
    } catch (error) {
      // Registra qualquer erro ocorrido durante a exclusão do produto
      console.error('Erro ao deletar produto:', error)
    }
  }

  // Efeito useEffect que é executado após a renderização inicial do componente
  useEffect(() => {
    // Faz uma solicitação GET para a API para obter a lista de produtos
    api.get(`/produto/`)
      .then(response => {
        // Atualiza o estado dos produtos com os dados recebidos da API
        setProdutos(response.data.results)
      })
      .catch(error => {
        // Registra qualquer erro ocorrido ao buscar os produtos
        console.error('Erro ao buscar produtos:', error)
      })
  }, [])
  // Retorna a interface do componente ProdutoList
  return (
    <div>
      <Navbar></Navbar>
      <div className="header">
      </div>
        <h1>Lista de Produtos</h1>
        <Link to="/produto/create" className="create-button">Criar Novo Produto</Link>
      <ul>
        {produtos.map((produto) => (
          <li key={produto.id} className="produto-item">
            <Link to={`/produto/${produto.id}/detail`} className="produto-link-name">{produto.nome}</Link>
            <div className="actions">
              <Link to={`/produto/${produto.id}/edit`} className="produto-link">Editar</Link>
              <button onClick={() => handleDelete(produto.id)} className="delete-button">Deletar</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}

// Exporta o componente ProdutoList
export default ProdutoList