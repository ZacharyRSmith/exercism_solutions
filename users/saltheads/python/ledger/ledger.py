# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


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
    else:  # locale == 'nl_NL' and currency == 'EUR'
        absolute = f'€ {abs(change)/100:,.2f}'.translate(
            str.maketrans({',': '.', '.': ','}))
        money = f'({absolute})' if change < 0 else f' {absolute} '
    return money


class Entry(ABC):

    @classmethod
    def make(cls, entry, locale, currency):
        if locale == 'en_US':
            return EnUSEntry(entry, locale, currency)
        elif locale == 'nl_NL':
            return NlNLEntry(entry, locale, currency)

    def __init__(self, entry, locale, currency):
        date, description, change = entry
        description = description \
            if len(description) <= 25 else description[:22] + '...'

        self._str = f'{self._fmt_date(date)} | {description: <25} | {_fmt_change(change, locale, currency): >13}'

    def __str__(self):
        return self._str

    @abstractmethod
    def _fmt_date(self):
        raise NotImplemented()

class NlNLEntry(Entry):
    def _fmt_date(self, date):
        y, m, d = date
        return f'{d}-{m}-{y}'
class EnUSEntry(Entry):
    def _fmt_date(self, date):
        y, m, d = date
        return f'{m}/{d}/{y}'


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

    for entry in entries:
        entry = Entry.make(entry, locale, currency)
        lines.append(str(entry))

    return '\n'.join(lines)
