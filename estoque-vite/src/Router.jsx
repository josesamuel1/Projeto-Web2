// Este código define um componente chamado AppRouter que representa as rotas da aplicação. Ele utiliza o Router do React Router para envolver a aplicação e fornecer a navegação baseada em rotas. As rotas são definidas dentro do componente Routes.

// Importa os componentes necessários do react-router-dom e os componentes da aplicação
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './components/Login'
import Inicio from './components/Inicio/Inicio'
import PrivateRoute from './components/PrivateRoute'
import ProdutoEdit from './components/ProdutoEdit'
import CreatePost from './components/ProdutoEdit'
import ProdutoList from './components/ProdutoList'
import ProdutoRead from './components/ProdutoRead'

// Define o componente AppRouter que contém as rotas da aplicação
function AppRouter() {
  return (
    // Define o componente Router para envolver a aplicação e fornecer navegação baseada em rotas
    <Router>
      {/* Define as rotas da aplicação */}
      <Routes>
        {/* Rota para a página de login (pública) */}
        <Route path="/" element={<Login />} />
        {/* Rotas protegidas que requerem autenticação */}
        <Route element={<PrivateRoute />}>
          <Route path="/inicio" element={<Inicio />} />
          {/* Rota para a listagem de produtos */}
          <Route path="/produto" element={<ProdutoList />} />
          {/* Rota para criar um novo produto */}
          <Route path="/produto/create" element={<CreatePost />} />
          {/* Rota para editar um produto existente */}
          <Route path="/produto/:produtoId/edit" element={<ProdutoEdit />} />
          {/* Rota para visualizar os detalhes de um produto */}
          <Route path="/produto/:produtoId/detail" element={<ProdutoRead />} />
        </Route>
      </Routes>
    </Router>
  )
}

// Exporta o componente AppRouter
export default AppRouter