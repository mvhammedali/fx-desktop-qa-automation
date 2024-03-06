from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class AboutPrefs:
    """Page Object Model for about:preferences"""

    # Categories
    category_search = (By.ID, "category-search")

    # Category: Search elements
    search_engine_dropdown = (By.ID, "defaultEngine")
    search_engine_option = lambda engine_name: (
        By.CSS_SELECTOR,
        f"menuitem[label='{engine_name}']",
    )

    # Misc
    any_dropdown_active = (By.CSS_SELECTOR, "menuitem[_moz-menuactive='true']")


@dataclass
class AboutGlean:
    """Page Object Model for about:glean"""

    # Elements
    ping_id_input = (By.ID, "tag-pings")
    submit_button = (By.ID, "controls-submit")


@dataclass
class Navigation:
    """Page Object Model for nav buttons and AwesomeBar"""

    awesome_bar = (By.ID, "urlbar-input")

    # Tab-to-search
    tab_to_search_text_span = (
        By.CLASS_NAME,
        "urlbarView-dynamic-onboardTabToSearch-text-container",
    )
    search_mode_span = (By.ID, "urlbar-search-mode-indicator-title")

    # "Refresh Firefox" incl. Intervention Card
    # quick_actions_refresh_button = (By.CSS_SELECTOR, '[id="urlbarView-row-3-label-0"][text^="Refresh"]')
    quick_actions_refresh_button = (By.ID, "urlbarView-row-3-label-0")
    refresh_intervention_card = (
        By.CSS_SELECTOR,
        'div[tip-type="intervention_refresh"]',
    )
    fx_refresh_text = (
        By.CSS_SELECTOR,
        'span[data-l10n-id="intervention-refresh-profile"]',
    )
    fx_refresh_button = (
        By.CSS_SELECTOR,
        'span[role="button"][data-l10n-id="intervention-refresh-profile-confirm"]',
    )
    fx_refresh_menu = (
        By.CSS_SELECTOR,
        'span[data-l10n-id="urlbar-result-menu-button"][title="Open menu"]',
    )
    fx_refresh_menu_get_help_item = (
        By.CSS_SELECTOR,
        'menuitem[data-l10n-id="urlbar-result-menu-tip-get-help"]',
    )


# Endnotes:
#  - If you're looking for about:logins, that page has so many shadow DOMs
#    that all elements exist in shadow_dom.py.
