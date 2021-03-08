from core.service import open_csv
from datetime import datetime, timedelta

def criar_eventos(service, empresas):
    resultados = open_csv()
    for e in resultados:
      for index in range(len(empresas)):
        if e['empresa'] == empresas[index]:
          primeiro_tri = e['resultados']['primeiro_tri']
          segundo_tri = e['resultados']['segundo_tri']
          terceiro_tri = e['resultados']['terceiro_tri']
          post_do_evento(service, e['empresa'],[primeiro_tri, segundo_tri, terceiro_tri])


def deletar_evento(service, eventId):
    service.events().delete(calendarId='primary', eventId=eventId).execute()
    return f'{eventId} Deletado com sucesso'


def post_do_evento(service, empresa, lista):
  for x in range(len(lista)):
    data = lista[x].split('/')
    mes = int(data[0])
    dia = int(data[1])
    ano = int(data[2])
    start_time = datetime(ano, dia, mes, 8, 00, 0)
    end_time = start_time + timedelta(hours=1)
    timezone = 'America/Sao_Paulo'
    event = {
        'summary': empresa,
        'location': 'São Paulo',
        'description': f'Resultados da {empresa}',
        'start': {
          'dateTime': start_time.strftime(f"%Y-%m-%dT%H:%M:%S"),
          'timeZone': timezone,
        },
        'end': {
          'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
          'timeZone': timezone,
        },
        'reminders': {
          'useDefault': False,
          'overrides': [
            {'method': 'popup', 'minutes': 12 * 60},
          ],
        },
      }
    print(event["summary"], ' criado com sucesso')
    service.events().insert(calendarId='primary', body=event).execute()
