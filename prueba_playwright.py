import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        print("Conectando a WordPress local...")
        await page.goto("http://lacomet-pruebas-local.local/wp-login.php")
        
        # Espera a que el campo de usuario esté visible
        await page.wait_for_selector('input[name="log"]')
        
        # Ingreso de credenciales reales
        await page.fill('input[name="log"]', "pasante_qa")
        await page.fill('input[name="pwd"]', "Pasante1234*")
        
        # Clic en Iniciar sesión
        await page.click('input[type="submit"]')
        
        print("¡Login enviado! Esperando 5 segundos para verificar el Escritorio...")
        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())