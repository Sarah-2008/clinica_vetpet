from app.database import engine, SessionLocal
from app.crud import inserir_tutor, inserir_animal, inserir_atendimento
from app import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()


# TUTORES
tutor1 = inserir_tutor(
    db,
    "Sarah Vitoria",
    "61999999999",
    "sarah@email.com"
)

tutor2 = inserir_tutor(
    db,
    "toin",
    "61988888888",
    "toin@email.com"
)

print("Tutores inseridos com sucesso!")


# ANIMAIS
animal1 = inserir_animal(
    db,
    "Mel",
    "cão",
    "Golden Retriever",
    25.5,
    tutor1.id
)

animal2 = inserir_animal(
    db,
    "Mimi",
    "gato",
    "Siamês",
    4.2,
    tutor1.id
)

animal3 = inserir_animal(
    db,
    "Lola",
    "ave",
    "Calopsita",
    0.1,
    tutor2.id
)

print("Animais inseridos com sucesso!")


# ATENDIMENTOS
atendimento1 = inserir_atendimento(
    db,
    "07/10/2026",
    "Vacina anual V8",
    120.00,
    animal1.id
)

atendimento2 = inserir_atendimento(
    db,
    "07/10/2026",
    "Consulta veterinária",
    100.00,
    animal2.id
)

atendimento3 = inserir_atendimento(
    db,
    "07/10/2026",
    "Avaliação de saúde",
    80.00,
    animal3.id
)

print("Atendimentos inseridos com sucesso!")
print("Banco de dados criado e preenchido com sucesso!")

db.close()