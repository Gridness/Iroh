from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle

buttons = {
    "Play" : manage_components.create_button(
        style=ButtonStyle.green,
        label="Играть"
    ),
    "Pause" : manage_components.create_button(
        style=ButtonStyle.blue,
        label="Пауза"
    ),
    "Stop" : manage_components.create_button(
        style=ButtonStyle.red,
        label="Стоп"
    ),
    "Skip" : manage_components.create_button(
        style=ButtonStyle.gray,
        label="Пропустить"
    )
}