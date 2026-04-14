# Share Class

A class of stock issued by an issuer.

## OCF Equivalent

Maps to OCF's `StockClass` — same concept (common, preferred series, etc.).


- [`StockClass`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/StockClass/) — object

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/shareClasses` — list


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1ShareClass`](../objects/share_class.md)

_A class of stock issued by an issuer._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `issuerId` | string |  |
| `name` | string |  |
| `prefix` | string |  |
| `type` | [`v1alpha1ShareClassType`](../types/share_class_type.md) |  |
| `authorizedShareCount` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `parValue` | [`v1alpha1Money`](../types/money.md) |  |
| `seniority` | integer (int32) |  |
| `pariPassu` | boolean |  |
| `preferredShareClassDetails` | [`v1alpha1PreferredShareClassDetails`](../types/preferred_share_class_details.md) |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`StockClass`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/StockClass/)

_Object describing a class of stock issued by the issuer_

| Property | Type | Required |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constant:** `STOCK_CLASS`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| name | `STRING` | `REQUIRED` |
| class_type | `Enum - Stock Class Type`</br></br>_Description:_ Enumeration of stock class types</br></br>**ONE OF:** </br>&bull; COMMON </br>&bull; PREFERRED | `REQUIRED` |
| default_id_prefix | `STRING` | `REQUIRED` |
| initial_shares_authorized | **ONE OF the Following Types/Objs:**</br>&bull; `Enum - Authorized Shares Types`</br></br>_Description:_ Enumeration of authorized shares types</br></br>**ONE OF:** </br>&bull; NOT APPLICABLE </br>&bull; UNLIMITED</br>&bull; [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | `REQUIRED` |
| board_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| stockholder_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| votes_per_share | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | `REQUIRED` |
| par_value | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | - |
| price_per_share | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | - |
| seniority | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | `REQUIRED` |
| conversion_rights | [ [schema/types/conversion_rights/StockClassConversionRight](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_rights/StockClassConversionRight/) ] | - |
| liquidation_preference_multiple | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | - |
| participation_cap_multiple | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | - |
</div>
</div>


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the share class. |
| `issuerId` | string |  | The identifier of the issuer to which this share class belongs. |
| `name` | string |  | The name of the share class. |
| `prefix` | string |  | The prefix used to identify the share class. Can only be numbers and letters. For example, CS for Common, PS for Series Seed Preferred, and PA for Series A Preferred. |
| `type` | [`v1alpha1ShareClassType`](../types/share_class_type.md) |  | The type of the share class. |
| `authorizedShareCount` | [`v1alpha1Decimal`](../types/decimal.md) |  | The maximum number of shares allowed to be issued to investors, as laid out in the articles of incorporation. |
| `parValue` | [`v1alpha1Money`](../types/money.md) |  | The minimum price per share at which the shares must be issued. Is usually set at $0.001 or $0.0001 per share, as stated in the corporate charter. |
| `seniority` | integer (int32) |  | Indicates the order in which share holders will get paid. Seniority ranks high to low, with 1 being the highest and will be paid out first. The higher the number, the less seniority the corresponding share class has. |
| `pariPassu` | boolean |  | Indicates whether this share class has equal seniority to an existing share class. |
| `preferredShareClassDetails` | [`v1alpha1PreferredShareClassDetails`](../types/preferred_share_class_details.md) |  | Preferred share class details when share class type is set to preferred. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1ShareClass`](../objects/share_class.md)_


[← Back to Domain Index](index.md)
