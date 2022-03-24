# bNaming_API
Api de um sistema para auxiliara a avaliar a qualidade de um nome de uma marca.

-----------------------------------------------------------------------------------

A API está hospedada no Heroku no seguinte link:

https://bnaming-api.herokuapp.com

-----------------------------------------------------------------------------------

Há uma rota disponível para 2 métodos HTTP, a rota é ‘/evaluation’.

-> Para o método GET ela retorna a seguinte mensagem: “Utilize o metodo POST e envie o nome e o segmento em um JSON para que possamos realizar a avaliacao do nome.”

-> Para utilizar o método POST deve passar um JSON no request com o seguinte formato:
    {
        "nome": <nome_para_ser_avaliado>,
        "segmento":<segmento_do_nome_para_ser_avaliado>,
    }
Os segmentos disponíveis são:
    - alimentos/bebidas
    - automotivo
    - bens de consumo
    - energia/combustível
    - entretenimento
    - financeiro
    - logistica'
    - serviços
    - tecnologia
    - varejo
