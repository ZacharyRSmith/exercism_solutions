def create_entry(date, description, change):
    return tuple([tuple(list(date.split('-'))), description, change])


def make_header(locale):
    if locale == 'en_US':
        return 'Date       | Description               | Change       '
    if locale == 'nl_NL':
        return 'Datum      | Omschrijving              | Verandering  '
    return ''


def make_date(locale, year, month, day):
    if locale == 'en_US':
        return f'{month}/{day}/{year}'
    if locale == 'nl_NL':
        return f'{day}-{month}-{year}'
    return ''


def make_description(description):
    return description if len(description) <= 25 \
        else description[:22] + '...'


def make_money(locale, currency, change):
    if locale == 'en_US' and currency == 'USD':
        absolute = f'${abs(change)/100:,.2f}'
        return f'({absolute})' if change < 0 else f' {absolute} '
    if locale == 'en_US' and currency == 'EUR':
        absolute = f'€{abs(change)/100:,.2f}'
        return f'({absolute})' if change < 0 else f' {absolute} '
    if locale == 'nl_NL' and currency == 'USD':
        return f'$ {change/100:,.2f} '.translate(
            str.maketrans({',': '.', '.': ','}))
    if locale == 'nl_NL' and currency == 'EUR':
        absolute = f'€ {abs(change)/100:,.2f}'.translate(
            str.maketrans({',': '.', '.': ','}))
        return f'({absolute})' if change < 0 else f' {absolute} '
    return ''


def format_entries(currency, locale, entries):
    lines = []
    lines.append(make_header(locale))

    entries = sorted(entries)
    for entry in entries:
        (year, month, day), description, change = entry
        date = make_date(locale, year, month, day)
        description = make_description(description)
        money = make_money(locale, currency, change)
        lines.append(f'{date: <10} | {description: <25} | {money: >13}')
    return '\n'.join(lines)
