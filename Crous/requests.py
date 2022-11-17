from .objects import Menu, Info

from utils.data import restos_data, coords

from aiohttp import ClientSession



async def get_crous_menu(
    session: ClientSession,
    ru: str, 
    dt: str,
):
    data = {
        "ru": ru,
        "dt": dt    
    }
        
    async with session.post(f"https://ent-1.univ-reims.fr/esup-crous/action/getMenu.php", data=data) as response:
        text = await response.text()
        return Menu(text, restos_data.get(ru, {}).get('format'))


def get_crous_info(
    ru: str,
):
    return Info(restos_data[ru], coords[ru])