// Importa os hooks useState e useEffect do React para gerenciar o estado e efeitos colaterais, respectivamente,
// o hook useParams do react-router-dom para obter parâmetros da URL,
// e o módulo api para fazer solicitações HTTP.
import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import api from '../api'

// Importa o arquivo de estilo CSS.
import '../styles/ProdutoRead.css'

function ProdutoRead() {
  const { produtoId } = useParams()
  const [nome, setNome] = useState('')
  const [quantidade, setQuantidade] = useState('')
  const [tamanho, setTamanho] = useState('')
  const [descricao, setDescricao] = useState('')

  useEffect(() => {
    // Carrega os detalhes do produto
    api.get(`/produto/${produtoId}/`)
      .then(response => {
        setNome(response.data.nome)
        setQuantidade(response.data.quantidade)
        setTamanho(response.data.tamanho)
        setDescricao(response.data.descricao)
      })
      .catch(error => {
        console.error('Erro ao buscar detalhes do produto:', error)
      })
  }, [produtoId])

  return (
    <div className="read-produto-container">
      <h1>Detalhes do Produto</h1>
      <Link to="/produto" >
        <button type="button" className="back-button">Voltar para Listagem</button>
      </Link>
      <h2>Nome: {nome}</h2>
      <p>Quantidade: {quantidade}</p>
      <p>Tamanho: {tamanho}</p>
      <p>Descrição: {descricao}</p>
    </div>
  )
}

// Exporta o componente ProdutoRead
export default ProdutoRead
