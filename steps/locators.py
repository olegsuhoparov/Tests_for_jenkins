from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LINK_YA = (By.CSS_SELECTOR, "[role='form'] .i-bem")
    LOGIN_FORM = (By.CSS_SELECTOR, ".passp-auth>:nth-child(1)")
    LOGIN_FIELD = (By.CSS_SELECTOR, "[name='login']")
    BUTTON_LOG = (By.CSS_SELECTOR, "[type='submit']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#passp-field-passwd")
    USER_ICON = (By.CSS_SELECTOR, ".mail-User-Name")
    EXIT_MENU = (By.CSS_SELECTOR, ".b-user-dropdown-content>:nth-child(7)")
    CREATE_POST = (By.CSS_SELECTOR, "div>.desk-notif-card__login-mail-promo")
    WRONG_LOG_PASS = (By.CSS_SELECTOR, ".passp-form-field__error")

class BasePageLocators():
    GEOLINK = (By.CSS_SELECTOR, ".headline__item .geolink__reg")
    SET_CITY = (By.CSS_SELECTOR, ".input__box .input__control")
    LINK_WAIT = (By.CSS_SELECTOR, ".b-autocomplete-item__reg")
    MORE = (By.CSS_SELECTOR, "[data-statlog='tabs.more']")
    MORE_T = (By.CSS_SELECTOR, ".popup2 .home-tabs3__more")

class ExtraLocators():
    VIDEO = (By.CSS_SELECTOR, "[data-id='video']")
    IMAGES = (By.CSS_SELECTOR, "[data-id='images']")
    NEWS = (By.CSS_SELECTOR, "[data-id='news']")
    MAPS = (By.CSS_SELECTOR, "[data-id='maps']")
    MARKET = (By.CSS_SELECTOR, "[data-id='market']")
    TRANSLATE = (By.CSS_SELECTOR, "[data-id='translate']")
    MUSIC = (By.CSS_SELECTOR, "[data-id='music']")
    LANGS_CHANGE = (By.CSS_SELECTOR, ".b-langs .dropdown2")
    LANGS_MORE = (By.CSS_SELECTOR, "[data-statlog='head.lang.more']")
    SELECT_LANG = (By.CSS_SELECTOR, "[type='button']")
    LANG_ENG = (By.CSS_SELECTOR, ".popup__content :nth-child(6)")
    LANG_SAVE = (By.CSS_SELECTOR, ".form__save")
