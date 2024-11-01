import random
from django.core.management.base import BaseCommand
from faker import Faker
from eventin.models import Event, Participant, Register
from validate_docbr import CPF

class Command(BaseCommand):
    help = 'Popula o banco de dados com informações fictícias para eventos e participantes'

    def handle(self, *args, **kwargs):
        faker = Faker()
        cpf_validator = CPF()

        events_title = [
            'Conferência de Desenvolvimento Web',
            'Workshop de Análise de Dados',
            'Seminário de Inteligência Artificial',
            'Palestra sobre Marketing Digital',
            'Curso de Gestão de Projetos',
            'Aulas de Programação em Python',
            'Evento de Segurança da Informação',
            'Exposição de Design Gráfico',
            'Hackaton de Desenvolvimento Mobile',
            'Fórum de Banco de Dados'
        ]

        events = []

        for _ in range(10):
            event = Event(
                title=random.choice(events_title),
                description=faker.text(max_nb_chars=200),
                local=faker.city,
                date_event=faker.date_time_between(start_date='now', end_date='+60d'),
                capacity=random.randint(50, 200)
            )
            events.append(event)

        Event.objects.bulk_create(events)

        participants = []

        for _ in range(50):
            cpf = cpf_validator.generate()
            participant = Participant(
                name=faker.name(),
                cpf=cpf,
                email=faker.unique.email(),
                phone=faker.phone_number()
            )
            participants.append(participant)

        Participant.objects.bulk_create(participants)

        participants_ids = Participant.objects.values_list('id', flat=True)
        events_ids = Event.objects.values_list('id', flat=True)
        registers = []

        for participant_id in participants_ids:
            for _ in range(1, 3):
                register = Register(
                    event_id=random.choice(events_ids),
                    participant_id=participant_id
                )
                registers.append(register)
        
        Register.objects.bulk_create(registers)

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso.'))


