### Issuerstransactions Stock Option Type

**Description:** _The tax classification assigned to an option grant at issuance.
Determines the tax treatment of the grant based on the jurisdiction and plan type.

 - STOCK_OPTION_TYPE_ISO: US — Incentive Stock Option (IRC §422). Eligible for favorable capital gains tax treatment if holding period requirements are met.
 - STOCK_OPTION_TYPE_NSO: US — Non-Qualified Stock Option. Taxed as ordinary income at exercise.
 - STOCK_OPTION_TYPE_INTL: International — General classification for stock options in non-US jurisdictions without a more specific type.
 - STOCK_OPTION_TYPE_EMI: UK — Enterprise Management Incentive. Tax-advantaged options for employees of qualifying small companies.
 - STOCK_OPTION_TYPE_CSOP: UK — Company Share Option Plan. HMRC-approved tax-advantaged scheme with a £30,000 individual limit.
 - STOCK_OPTION_TYPE_SPR: UK — Share Purchase Rights. Rights to purchase shares under a share purchase arrangement.
 - STOCK_OPTION_TYPE_CAPITAL_GAINS_TRACK_102: Israel — Section 102 Capital Gains Track. Options held in trust with favorable capital gains tax treatment.
 - STOCK_OPTION_TYPE_ORDINARY_INCOME_TRACK_102: Israel — Section 102 Ordinary Income Track. Options held in trust taxed as ordinary income.
 - STOCK_OPTION_TYPE_NON_TRUSTEE: Israel — Section 102 Non-Trustee arrangement. Options not held in trust.
 - STOCK_OPTION_TYPE_THREE_I: Israel — Section 3(i) grant. Options granted to non-employees or under Section 3(i) of the Income Tax Ordinance.
 - STOCK_OPTION_TYPE_UNAPPROVED: UK — Unapproved option scheme. Options not under an HMRC-approved plan.
 - STOCK_OPTION_TYPE_BSPCE: France — Bons de Souscription de Parts de Créateur d'Entreprise. Tax-advantaged startup equity instrument.
 - STOCK_OPTION_TYPE_OSA: Canada — Option Stock Award. Stock options under Canadian tax rules.
 - STOCK_OPTION_TYPE_AGA: France — Attribution Gratuite d'Actions. Free share allocation under French tax-favored regime.
 - STOCK_OPTION_TYPE_BSA: France — Bon de Souscription d'Actions. Stock subscription warrants under French law.
 - STOCK_OPTION_TYPE_STARTUP_CONCESSIONS: Australia — Employee Share Scheme with startup concessions (Division 83A, Subdivision 83A-E).
 - STOCK_OPTION_TYPE_NON_CONCESSIONAL: Australia — Employee Share Scheme without concessional tax treatment.
 - STOCK_OPTION_TYPE_EU_WARRANT: EU — European Union warrant or option instrument.
 - STOCK_OPTION_TYPE_ZEPO: Zero Exercise Price Option. Options with a $0 exercise price, commonly used in some international jurisdictions._

**Referenced By (2):**
- [Option Exercise Transaction](option_exercise_transaction.md)
- [Option Issuance Transaction](option_issuance_transaction.md)

**Type:** `STRING`

**Allowed Values:**
- `STOCK_OPTION_TYPE_ISO`
- `STOCK_OPTION_TYPE_NSO`
- `STOCK_OPTION_TYPE_INTL`
- `STOCK_OPTION_TYPE_EMI`
- `STOCK_OPTION_TYPE_CSOP`
- `STOCK_OPTION_TYPE_SPR`
- `STOCK_OPTION_TYPE_CAPITAL_GAINS_TRACK_102`
- `STOCK_OPTION_TYPE_ORDINARY_INCOME_TRACK_102`
- `STOCK_OPTION_TYPE_NON_TRUSTEE`
- `STOCK_OPTION_TYPE_THREE_I`
- `STOCK_OPTION_TYPE_UNAPPROVED`
- `STOCK_OPTION_TYPE_BSPCE`
- `STOCK_OPTION_TYPE_OSA`
- `STOCK_OPTION_TYPE_AGA`
- `STOCK_OPTION_TYPE_BSA`
- `STOCK_OPTION_TYPE_STARTUP_CONCESSIONS`
- `STOCK_OPTION_TYPE_NON_CONCESSIONAL`
- `STOCK_OPTION_TYPE_EU_WARRANT`
- `STOCK_OPTION_TYPE_ZEPO`