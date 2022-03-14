# -*- coding: utf-8 -*-

def _fmt_date(date, locale):
    y, m, d = date
    if locale == 'en_US':
        return f'{m}/{d}/{y}'
    elif locale == 'nl_NL':
        return f'{d}-{m}-{y}'


def _fmt_change(change, locale, currency):
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
    return money


def create_entry(date, description, change):
    return tuple([tuple(list(date.split('-'))), description, change])


def format_entries(currency, locale, entries):
    if locale not in ('en_US', 'nl_NL'):
        raise ValueError("BOOM!")
    entries = sorted(entries)
    lines = []
    if locale == 'en_US':
        lines.append('Date       | Description               | Change       ')
    elif locale == 'nl_NL':
        lines.append('Datum      | Omschrijving              | Verandering  ')
    else:
        pass
    for entry in entries:
        date, description, change = entry
        description = description \
            if len(description) <= 25 else description[:22] + '...'

        lines.append(f'{_fmt_date(date, locale)} | {description: <25} | {_fmt_change(change, locale, currency): >13}')
    return '\n'.join(lines)
