import re
from playwright.sync_api import Page, expect

def test_has_title (page: Page ):
    page.goto('https://symbiosaas.com/')

    expect(page.locator('h1')).to_contain_text('CLOUD MIGRATION IS NOT THE END!!')

def test_click (page: Page):
    page.goto('https://symbiosaas.com/')
    page.click('text=GET STARTED TODAY')

    expect(page.get_by_role('heading', name='Solutions')).to_contain_text('Solutions')

def test_with_inputs (page: Page):
    page.goto('https://symbiosaas.com/')
    page.fill('#forminator-field-first-name-1_65bbb6dc31dbd-label','Marco Antonio')
    page.fill('#forminator-field-last-name-1_65bbb6dc31dbd','Murgueitio Blandón')
    page.click('text=Send Message')

def test_assertions (page: Page):
    page.goto('https://symbiosaas.com/')
    page.click('text=About us')
    expect(page).to_have_url('https://symbiosaas.com/contact/')
    expect(page).to_have_title('About us – Symbiosaas')

""" def test_selectors (page: Page):
    #Text
    page.click('text=some text')

    # Css Selectors
    page.click('button')
    page.click ('#id')
    page.click('.class')

    #Only visible Css Selector
    page.click('.sumit-button:visible')

    #Combinations
    page.click('#username .first')

    #XPath
    page.click('//button') """