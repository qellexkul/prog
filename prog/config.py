from vkbottle import API, Bot
from vkbottle.bot import BotLabeler


TOKEN = "vk1.a.q8xvFsuYgPyiTbuq97H3lZPCb9mRyrb5ZjtMWFHrygPNO4ibZPcLH0DsNR6cpJrf3aeKZnW-MTPAW7DbFVlPabpjF8egQLhCKNSb2xosHIyPO5GqM86DRDaRSoisEyIRVeA1_KRfAE6cMKieIayxCR8sF3hgGQwOiOmjuONEiwxl367mVEg0-c6RoLHu40ozUPoblpnsngS_byHBM2g7LA"

api = API(TOKEN)
labeler = BotLabeler()

bot = Bot(
    api=api,
    labeler=labeler,
)

# db config
DB_NAME="progVK"
DB_USER="postgres"
DB_PASSWORD='postgres'
DB_HOST="db"
DB_PORT=5432
# MIGRATE_DATABASE=postgres://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=disable

