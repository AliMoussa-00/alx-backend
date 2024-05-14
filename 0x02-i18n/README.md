# i18n

[tasks](https://drive.google.com/file/d/1AwwgMTnoAYtDlO_IxNG-0XC3WYrqk2Dh/view?usp=drive_link)

[i18n tutorial]([The Flask Mega-Tutorial, Part XIII: I18n and L10n - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n))

[babel](https://python-babel.github.io/flask-babel/#configuration)

---

`i18n` and `l10n` are both abbreviations related to software development, particularly in the context of making software accessible and usable to people from different linguistic and cultural backgrounds.

1. **i18n**:
  
  - **Internationalization**: The term "i18n" stands for "internationalization." It refers to the process of designing and developing software in a way that it can be easily adapted to various languages and regions without the need for engineering changes to the core codebase.
  - Internationalization involves techniques such as:
    - Designing user interfaces to accommodate text expansion and contraction when translating into different languages.
    - Separating text content from the codebase, typically by using external files or databases.
    - Supporting various character encodings and text directionality.
  - The goal of internationalization is to make it easier to localize the software for different languages and regions.
2. **l10n**:
  
  - **Localization**: The term "l10n" stands for "localization." It refers to the process of adapting software to a specific language or region by translating text, modifying graphics and design elements, and making other necessary adjustments to accommodate cultural differences.
  - Localization involves tasks such as:
    - Translating user interfaces, error messages, and documentation into the target language(s).
    - Adapting date, time, currency, and other formats to the conventions of the target region.
    - Modifying graphics, icons, and other visual elements to be culturally appropriate.
  - The goal of localization is to make the software feel native to users in the target region, improving user experience and accessibility.

In summary, `i18n` focuses on making software adaptable to different languages and regions from a technical perspective, while `l10n` focuses on the actual adaptation and translation of the software to specific languages and cultures. Both processes are essential for creating software that can reach and be used by a global audience.

---

## Translation

requirements

```shell
(venv) $ pip install flask flask-babel
```

- Initialize your translations with
  

```shell
(venv) pybabel extract -F babel.cfg -o messages.pot .

# dictionaries of langiages [en | fr]
(venv) $ pybabel init -i messages.pot -d translations -l en
(venv) $ pybabel init -i messages.pot -d translations -l fr

# compile your dictionaries with
(venv) $ pybabel compile -d translations
```

- updating Traslation
  

```shell
(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
(venv) $ pybabel update -i messages.pot -d app/translations
(venv) $ pybabel compile -d translations
```