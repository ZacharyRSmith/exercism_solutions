# -*- coding: utf-8 -*-

def create_entry(date, description, change):
    return tuple([tuple(list(date.split('-'))), description, change])


def format_entries(currency, locale, entries):
    entries = sorted(entries)
    lines = []
    if locale == 'en_US':
        lines.append('Date       | Description               | Change       ')
    elif locale == 'nl_NL':
        lines.append('Datum      | Omschrijving              | Verandering  ')
    else:
        pass
    for entry in entries:
        (y, m, d), description, change = entry
        description = description \
            if len(description) <= 25 else description[:22] + '...'
        if locale == 'en_US':
            date = f'{m}/{d}/{y}'
        elif locale == 'nl_NL':
            date = f'{d}-{m}-{y}'
        else:
            pass
        if locale == 'en_US' and currency == 'USD':
            absolute = f'${abs(change)/100:,.2f}'
            money = f'({absolute})' if change < 0 else f' {absolute} '
        elif locale == 'en_US' and currency == 'EUR':
            absolute = f'€{abs(change)/100:,.2f}'
            money = f'({absolute})' if change < 0 else f' {absolute} '
        elif locale == 'nl_NL' and currency == 'USD':
            money = f'$ {change/100:,.2f} '.translate(
                str.maketrans({',': '.', '.': ','}))
        elif locale == 'nl_NL' and currency == 'EUR':
            absolute = f'€ {abs(change)/100:,.2f}'.translate(
                str.maketrans({',': '.', '.': ','}))
            money = f'({absolute})' if change < 0 else f' {absolute} '
        else:
            pass
        lines.append(f'{date: <10} | {description: <25} | {money: >13}')
    return '\n'.join(lines)
