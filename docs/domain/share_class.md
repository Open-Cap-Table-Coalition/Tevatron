# Share Class

A class of stock issued by an issuer.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/shareClasses` — list


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
