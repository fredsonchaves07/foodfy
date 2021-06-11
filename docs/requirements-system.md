## Sessão

### Logout
- [ ] Somente usuário autenticado poderá realizar logout
- [ ] Deverá ser redirecionado para página principal

### Login
- [ ] Usuário deverá informar um email válido
- [ ] Usuário deverá informar uma senha válida
- [ ] Deverá ter link para recuperação de senha

### Esqueceu a senha
- [ ] Deverá informar o mesmo email já cadastrado no sistema para recuperação de senha
- [ ] O link de recuperação conterá um token de 1 dia para acessar a página de recuperação


## Usuário

### Cadastro
- [ ] Somente usuário admin poderá realizar o cadastro de usuários no sistema
- [ ] Deverá preencher o email válido
- [ ] Não é possível cadastrar com email já cadastrado no sistema
- [ ] Quando administrador cadastrar usuário, será enviado um link com token para acessar a pagina de perfil do usuário e alterar a senha
- [ ] Deve possuir a opção se o usuário é administrador

### Perfil
- [ ] Somente usuário autenticado poderá visualizar detalhes de sua conta
- [ ] Somente usuário comum poderá atualizar a sua senha
- [ ] Será possível editar o nome do usuário
- [ ] Será possível possível editar o email do usuário
- [ ] Só é possível alterar o email se não existir o email já cadastrado
- [ ] Será possível editar o cep da cidade
- [ ] Será possível editar o endereço completo
- [ ] Somente o usuário administrador poderá excluir a conta
- [ ] Usuário administrador não pode exlcuir sua própria conta

### Listagem de usuários
- [ ] Somente usuários administradores poderão visualizar informações de outros usuários


## Chefs

### Cadastro de chef
- [ ] Somente usuaŕio administrador poderá cadastrar o chef
- [ ] Somente usuário administrador poderá excluir o chef
- [ ] Deverá ser informado o nome do chef
- [ ] Deverá ser enviado a foto avatar do chef

### Edição do chef
- [ ] Somente usuaŕio administrador poderá atualizar o chef
- [ ] Somente usuário administrador poderá excluir o chef
- [ ] Será possível editar o nome do chef
- [ ] Será possível atualizar a imagem avatar do chef

### Visualização do chef
- [ ] Somente usuário autenticado poderá visualizar o chef
- [ ] Deverá conter a imagem avatar do chef
- [ ] Deverá conter o nome do chef
- [ ] Deverá conter as receitas vinculadas

### Listagem de chefs
- [ ] Somente usuário autenticado poderá visualizar a lista de chefs cadastrados
- [ ] Deverá conter o link para acesso a detalhes do chef
- [ ] Deverá conter a imagem avatar do chef
- [ ] Deverá conter o nome do chef


## Pedidos

### Meus Pedidos
- [ ] Somente usuário autenticado poderá visualizar seus próprios pedidos
- [ ] Caso não tenha nenhum pedido, deverá ser exibido o botão para procurar produto
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter o preço do produto
- [ ] Deverá conter a data do pedido
- [ ] Se estiver aberto, deverá apresentar informação que o pedido está em aberto
- [ ] Se estiver vendido, deverá apresentar informação que o pedido está realizado
- [ ] Se estiver cancelado pelo vendedor, deverá apresentar informação que o pedido está cancelado
- [ ] Deverá conter o link para informações do pedido

## Informações do pedido
- [ ] Somente usuário autenticado poderá visualizar seus próprio pedido
- [ ] Deverá conter o nome do comprador
- [ ] Deverá conter o email do comprador
- [ ] Deverá conter o endereço do comprador
- [ ] Deverá conter o cpf do comprador
- [ ] Deverá conter o nome do vendedor
- [ ] Deverá conter o email do vendedor
- [ ] Deverá conter o endereço do vendedor
- [ ] Deverá conter o cpf do vendedor
- [ ] Deverá conter a data e hora da realização do pedido
- [ ] Deverá conter o status do pedido
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter o preço do produto
- [ ] Deverá conter a quantidade do produto
- [ ] Deverá conter o total do pedido

## Vendas

### Minhas Vendas
- [ ] Somente usuário autenticado poderá visualizar suas próprias vendas realizadas
- [ ] Caso não tenha nenhuma venda, deverá exibir o botão para cadastrar anúncio
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter o preço do produto
- [ ] Deverá conter a data do pedido
- [ ] Deverá conter o total de vendas realizadas no final da página
- [ ] Se estiver aberto, deverá apresentar informação que a venda está em aberto
- [ ] Se estiver vendido, deverá apresentar informação que o pedido está realizado
- [ ] Se estiver cancelado deverá apresentar informação que o pedido está cancelado
- [ ] Deverá conter o link para informações do pedido
- [ ] Será possível cancelar a venda somente se não foi vendido ainda
- [ ] Será possível realizar venda somente se não foi vendido ainda 

## Produtos da Loja

### Últimos produtos cadastrados (página principal)
- [ ] Poderá ser visualizada sem autenticação
- [ ] Deverá conter 3 últimos produtos cadastrados
- [ ] Deverá conter a foto principal do produto
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter o preço atual do produto
- [ ] Deverá conter  o link para visualizar informações do produto

### Buscar Produto
- [ ] Poderá ser visualizada sem autenticação
- [ ] Será possível realizar a busca de produto por nome
- [ ] Deverá conter a foto principal do produto
- [ ] Deverá conter o preço atual do produto
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter a quantidade de resultados da busca
- [ ] Deverá conter a palavra pesquisada
- [ ] Deverá conter a categoria(s) da busca realizada
- [ ] Deverá apresentar o link para informações do produto

## Visualizar produto
- [ ] Poderá ser visualizada sem autenticação
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter a data e hora de publicação
- [ ] Deverá conter as fotos do produto
- [ ] Deverá conter a descrição do produto
- [ ] Deverá conter o preço atual do produto
- [ ] Deverá conter o preço antigo do produto
- [ ] Deverá apresentar o link para adicionar ao carrinho caso não seja vendedor do produto

## Carrinho de compra

## Informações do carrinho de compra
- [ ] Poderá ser visualizada sem autenticação
- [ ] Deverá conter o nome do produto
- [ ] Deverá conter a foto principal do produto
- [ ] Deverá conter o preço atual do produto
- [ ] Deverá conter a quantidade do produto
- [ ] Deverá conter o preço total do carrinho no final
- [ ] Usuário poderá selecionar varias quantidades de acordo com a disponibilidade do produto
- [ ] É possível excluir o item do carrinho
- [ ] Se estiver vazio deverá conter uma mensagem de que o carrinho está vazio
- [ ] Se estiver vazio deverá conter um link para realizar a compra (redirecionar para bussca)
- [ ] Deverá conter o link 'Continuar comprando' onde será redirecionado para página de busca
- [ ] Deverá conter o link 'Realizar pedido' onde será redirecionado para página de pedidos

## Realizar pedido
- [ ] Somente usuário autenticado poderá realizar o pedido
- [ ] Se disponível, deverá apresentar a informação que o pedido foi realizado
- [ ] Deverá conter o link 'Continuar comprando'
- [ ] Deverá conter a mensagem para aguardar resposta do vendedor


## Testes
vendedor
carlie96@gmail.com


comprador
fleta77@hotmail.com