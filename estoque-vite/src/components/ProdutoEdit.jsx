// Importa os hooks useState, useEffect, useNavigate e useParams do React para gerenciar estado, efeitos colaterais, navegação e parâmetros da URL
import { useState, useEffect } from 'react'
import { useNavigate, useParams, Link } from 'react-router-dom'

// Importa o axios para fazer solicitações HTTP
import api from '../api'

// Importa o arquivo de estilo CSS.
import '../styles/ProdutoEdit.css'

// Define o componente ProdutoEdit como uma função
function ProdutoEdit() {
  // Obtém o parâmetro produtoId da URL
  const { produtoId } = useParams()

  // Utiliza o hook useNavigate para navegar entre rotas
  const navigate = useNavigate()

  // Define estados para o nome, quantidade, tamanho, descrição e preço do produto
  const [nome, setNome] = useState('')
  const [quantidade, setQuantidade] = useState('')
  const [tamanho, setTamanho] = useState('')
  const [descricao, setDescricao] = useState('')
  const [preco, setPreco] = useState('')

  // Efeito useEffect que é executado sempre que o produtoId é alterado
  useEffect(() => {
    // Verifica se produtoId está definido
    if (!produtoId) return

    // Carrega os detalhes do produto com base no produtoId fornecido
    api.get(`/produto/${produtoId}/`)
      .then(response => {
        // Atualiza os estados com os detalhes do produto recebidos da API
        setNome(response.data.nome)
        setQuantidade(response.data.quantidade)
        setTamanho(response.data.tamanho)
        setDescricao(response.data.descricao)
        setPreco(response.data.preco)
      })
      .catch(error => {
        // Registra qualquer erro ocorrido ao buscar os detalhes do produto
        console.error('Erro ao buscar detalhes do produto:', error)
      })
  }, [produtoId])

  // Função para lidar com o envio do formulário
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      // Cria um objeto FormData para enviar os dados do formulário, incluindo a imagem, se houver
      const formData = new FormData()
      formData.append('nome', nome)
      formData.append('quantidade', quantidade)
      formData.append('tamanho', tamanho)
      formData.append('descricao', descricao)
      formData.append('preco', preco)

      // Determina se é uma atualização ou criação de um produto
      if (produtoId) {
        // Se for uma atualização, faz uma solicitação PUT para atualizar o produto
        await api.put(`/produto/${produtoId}/`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        // Exibe um alerta de sucesso
        alert('Produto atualizado com sucesso!')
      } else {
        // Se for uma criação, faz uma solicitação POST para criar o produto
        await api.post(`/produto/`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
      }
      // Redireciona para a página de listagem de produtos após o sucesso da operação
      navigate('/produto')
    } catch (error) {
      // Registra qualquer erro ocorrido ao salvar o produto
      console.error('Erro ao salvar produto:', error)
    }
  }

  // Retorna a interface do componente ProdutoEdit
  return (
    <div className="edit-produto-container">
      {/* Título dinâmico com base na existência do produtoId */}
      <h1>{produtoId ? 'Editar Produto' : 'Criar Novo Produto'}</h1>
      {/* Formulário para editar ou criar um produto */}
      <form onSubmit={handleSubmit}>
        {/* Inputs para o nome, quantidade, tamanho, descricao e preço do produto */}
        <input type="text" placeholder="Nome" value={nome} onChange={(e) => setNome(e.target.value)} />
        <input type="number" placeholder="Quantidade" value={quantidade} onChange={(e) => setQuantidade(e.target.value)} />
        <input type="selected" placeholder="Tamanho" value={tamanho} onChange={(e) => setTamanho(e.target.value)} />
        <input type="number" step="0.01" placeholder="Preço" value={preco} onChange={(e) => setPreco(e.target.value)} />
        <textarea placeholder="Descrição" value={descricao} onChange={(e) => setDescricao(e.target.value)} />
        {/* Botão para salvar o produto */}
        <button className="save-button" type="submit">{produtoId ? 'Salvar' : 'Criar'}</button>
        {/* Link para voltar para a listagem de produtos */}
        <Link to="/produto" >
          <button type="button" className="back-button">Voltar para Listagem</button>
        </Link>
      </form>
    </div>
  )
}

// Exporta o componente ProdutoEdit
export default ProdutoEdit
