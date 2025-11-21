### Jurisdiction

**Description:** _Jurisdiction used to calculate tax withholding is calculated.
Either the name of the city, country subdivision, or country used to calculate tax withholding._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `city` | `STRING` | The city used to calculate tax withholding. <br/>**Constraints:** Max length: 256 | - |
| `country` | [Iso3166 Set1 Alpha3 Code](iso3166_set1_alpha3_code.md) | The country used to calculate tax withholding. | - |
| `countrySubdivision` | [Iso3166 Set2 Code](iso3166_set2_code.md) | The country subdivision used to calculate tax withholding. | - |