# Olá meus caros!

Gostaria de apresentar meu mais último novo projeto, a qual realizei para uma Massoterapeuta, que 
iria exibir em live no seu instagram um sorteio para suas seguidoras, a mesma queria uma interface gráfica
personalizada com sua logo e as regras a serem seguidas para participar e eventualmente ganhar os prêmios.

Veja o resultado final:

![image](https://github.com/Henrique-de-Souza/interface-gr-fica-para-sorteio-/assets/148600312/2e340943-6989-4f85-be5b-a3bff0a474e5)

# Como funciona? 
--------------------------------------------------------------------------------------------------------------------------
Uma vez clicado no botão SORTEAR, veremos uma pequena janela com uma barra de progressão, simulando um carregamento!
Após o seu término a pessoa é sorteada e uma janela de parabenização com um texto personalizado é brevente exibida na tela

Vejam o seu funcionamento neste video: 

https://github.com/Henrique-de-Souza/interface-gr-fica-para-sorteio-/assets/148600312/7bc7771c-eac4-4071-be86-8fb29d736aa5


# Como foi Desenvolvido? 

(Vale ressaltar que desenvolvi todo o projeto em Python e utilizei do Canvas para artes gráficas).

Primeiramente tive que acessar o meu próprio instagram com login e senha, em seguida otbive a postagem por seu shortcode; Agora, bastou 
extrair todos os comentários do post e adicioná-los à uma lista, a mesma pela qual o sistema sortearia uma pessoa. 

Veja o código dessa primeira parte abaixo: 



```ruby
import instaloader

# Criei uma instância do Instaloader
loader = instaloader.Instaloader()

# Substitua 'username' e 'password' pelas suas credenciais do Instagram
username = 'enriquedesu'
password = '***********'

# Efetue o login
loader.context.login(username, password)

# Obtenha a postagem usando o shortcode da URL
post_shortcode = "C1sVIWpLZKJ"
post = instaloader.Post.from_shortcode(loader.context, post_shortcode)

# declarar uma lista vazia para ser preenchida com todos os comentários do post
lista_comentarios = []

# Obter e imprimir os comentários
comments = post.get_comments()
for comment in comments:
    # para cada comentário, adicione a lista somente o username
    lista_comentarios.append(comment.owner.username)

# Printe todos os comentários obtidos    
print(lista_comentarios)

```

Com todos os comentários extraídos em uma lista ordenada alfabeticamente, os transferi para dentro de minha interface gráfica,
o qual vemos funcionando em video e que poderá ser consultado no arquivo interface.py

----------------------------------------------------------------------------------------------------------------

contato: 

Email: enriquedesuu@gmail.com

telefone: (14) 99626-2918

instagram: @enriquedesu




