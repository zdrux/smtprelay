import asyncio
import aiosmtpd.controller
import aiosmtplib
from aiosmtpd.handlers import AsyncMessage
import toml


class RelayHandler(AsyncMessage):
    async def handle_message(self, message):
        # read SMTP configuration from TOML file
        with open('config.toml') as f:
            config = toml.load(f)['smtp']

        # create a new SMTP connection
        smtp_client = aiosmtplib.SMTP(hostname=config['server'], port=config['port'])
        await smtp_client.connect()
        await smtp_client.starttls()
        await smtp_client.login(config['username'], config['password'])

        # send the received email
        await smtp_client.send_message(message)

        # close the SMTP connection
        await smtp_client.quit()


if __name__ == '__main__':
    port = 8080
    controller = aiosmtpd.controller.Controller(RelayHandler(), hostname='127.0.0.1', port=port)
    controller.start()
    print(f'SMTP relay listening on port {port}')
    asyncio.get_event_loop().run_forever()
