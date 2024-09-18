from petshop_1.Cachorro import Cachorro
from petshop_1.Gato import Gato

#cadastrar os pets
pet1 = Cachorro("Rex", 4, "Puddle")
pet2 = Cachorro("Lulu", 2, "Golden")
pet3 = Cachorro("Zeus", 2, "Pitbull")
pet4 = Cachorro("Raimundin", 2, "Caramelo")
pet5 = Gato("Zidaninho", 4, "Orange cat")
pet6 = Gato("Zidane", 3, "Siamês")
pet7 = Gato("Nerfado", 2, "Persa")
pet8 = Gato("Charlote", 2, "Caramelo")

#lista de pets
pets = [
    pet1,
    pet2,
    pet3,
    pet4,
    pet5,
    pet6,
    pet7,
    pet8
]

#gerar os pets cadastrados
for pet in pets:
    print(
        f'--------Dados do Pet--------\n'
        f'Nome:{pet.nome}\n' 
        f'Idade:{pet.idade}\n'
        f'Raca:{pet.raca}\n'
    )

#remove pet da lista
pets.pop(4)

for pet in pets:
    print(
        f'--------Dados do Pet--------\n'
        f'Nome:{pet.nome}\n' 
        f'Idade:{pet.idade}\n'
        f'Raca:{pet.raca}\n'
    )
