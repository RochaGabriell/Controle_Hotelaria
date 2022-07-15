
# Sistema de Domínio

_Desafio proposto como ultima nota do Curso de Ads._

Desenvolva um sistema de domínio para um sistema de controle de hotelaria de acordo com os seguintes fatos:

- O hotel aluga quartos de diversas categorias (simples, duplo, casal, luxo etc.). O valor dos quartos varia de acordo com a categoria.
- Os quartos do hotel podem ser reservados previamente antes de os hóspedes virem ocupá-los. Para isso, é necessário informar os dados do cliente que os está reservando, a data da reserva e a provável data em que um quarto será desocupado.
- Cada hóspede precisa ser identificado no momento em que ocupa um quarto, mesmo que este seja pago por outro cliente. Caso seu cadastro ainda não exista ou seus dados tenham mudado, será necessário cadastrá-lo.
- Um hóspede pode alugar muitos quartos, em um mesmo momento ou em momentos diferentes, e um quarto pode ser alugado por muitos hóspedes, em momentos diferentes, naturalmente.
- Dependendo da categoria do quarto, terá uma determinada quantidade de itens, tanto no quarto propriamente dito como no frigobar.
Um hóspede pode consumir itens do frigobar. Cada item tem valores e quantidades diferentes. É preciso registrar o consumo do hóspede para posterior cobrança. Um hóspede pode solicitar serviços do hotel, como passar roupas ou lavanderia. Da mesma forma que o consumo, cada serviço solicitado precisa ser registrado. 
- Cada quarto ocupado gera diárias sempre ao meio-dia. Uma diária deve ser paga exclusivamente por um determinado hóspede (ou pelo cliente que fez a reserva), mas um hóspede pode pagar muitas diárias.
- É necessário saber qual funcionário foi responsável pela locação e/ou encerramento de cada locação de um quarto.
O sistema deve utilizar funções e salvar as informações em arquivos (txt ou json).