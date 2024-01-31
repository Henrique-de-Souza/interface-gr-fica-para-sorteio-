import instaloader

# Crie uma instância do Instaloader
loader = instaloader.Instaloader()

# Substitua 'username' e 'password' pelas suas credenciais do Instagram
username = 'enriquedesu'
password = 'Rick454260*'

# Efetue o login
loader.context.login(username, password)

# Obtenha a postagem usando o shortcode da URL
post_shortcode = "C1sVIWpLZKJ"
post = instaloader.Post.from_shortcode(loader.context, post_shortcode)

# declarar uma lista vazia
lista_comentarios = []

# Obter e imprimir os comentários
comments = post.get_comments()

for comment in comments:
    # para cada comentário, adicione à lista o username
    lista_comentarios.append(comment.owner.username)

    print(f"{comment.owner.username} => {comment.text}")
    print()
    
print(lista_comentarios)

loader.context.logout()
