# Supporting Types

Supporting type schemas referenced by API objects. These define the structure of nested fields and common data types used throughout the API.

## Common Types

Fundamental data types used throughout the API:

- [Date](date.md) - Date representation
- [Decimal](decimal.md) - High-precision decimal numbers
- [Money](money.md) - Monetary amounts with currency
- [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) - ISO 8601 date format
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) - ISO 8601 datetime format
- [Iso3166 Set1 Alpha3 Code](iso3166_set1_alpha3_code.md) - ISO 3166 country codes (alpha-3)
- [Iso3166 Set2 Code](iso3166_set2_code.md) - ISO 3166 subdivision codes
- [Iso4217 Currency Alpha Code](iso4217_currency_alpha_code.md) - ISO 4217 currency codes
- [Jurisdiction](jurisdiction.md) - Legal jurisdiction information
- [Document](document.md) - Document references

## Response Types

### GET Responses
- [Get Capitalization Table Response](get_capitalization_table_response.md)
- [Get Certificate Response](get_certificate_response.md)
- [Get Compensation Benchmark Attributes Response](get_compensation_benchmark_attributes_response.md)
- [Get Compensation Benchmarks Response](get_compensation_benchmarks_response.md)
- [Get Convertible Note Response](get_convertible_note_response.md)
- [Get Draft Option Grant Response](get_draft_option_grant_response.md)
- [Get Issuer Response](get_issuer_response.md)
- [Get Option Grant Response](get_option_grant_response.md)
- [Get Restricted Stock Award Response](get_restricted_stock_award_response.md)
- [Get Restricted Stock Unit Response](get_restricted_stock_unit_response.md)
- [Get Stakeholder Capitalization Table Response](get_stakeholder_capitalization_table_response.md)
- [Get Stakeholder Response](get_stakeholder_response.md)

### LIST Responses
- [List Certificates Response](list_certificates_response.md)
- [List Convertible Notes Response](list_convertible_notes_response.md)
- [List Corporations Response](list_corporations_response.md)
- [List Fair Market Values Response](list_fair_market_values_response.md)
- [List Interests Response](list_interests_response.md)
- [List Issuers Response](list_issuers_response.md)
- [List Option Exercises Response](list_option_exercises_response.md)
- [List Option Grants Response](list_option_grants_response.md)
- [List Points Of Contact Response](list_points_of_contact_response.md)
- [List Restricted Stock Awards Response](list_restricted_stock_awards_response.md)
- [List Restricted Stock Units Response](list_restricted_stock_units_response.md)
- [List Share Classes Response](list_share_classes_response.md)
- [List Stakeholders Response](list_stakeholders_response.md)
- [List Vesting Schedule Templates Response](list_vesting_schedule_templates_response.md)

### Other Responses
- [Create Draft Option Grant Response](create_draft_option_grant_response.md)
- [Update Money Movement Response](update_money_movement_response.md)
- [Update Tax Withholding Response](update_tax_withholding_response.md)
- [Rpc Status](rpc_status.md)
- [Protobuf Any](protobuf_any.md)

## Capitalization Table Types

- [Capitalization Table](capitalization_table.md)
- [Capitalization Table Summary](capitalization_table_summary.md)
- [Stakeholder Capitalization Table](stakeholder_capitalization_table.md)
- [Stakeholder Capitalization Table Summary](stakeholder_capitalization_table_summary.md)

## Share Class Types

- [Share Class Type](share_class_type.md)
- [Share Class Valuation](share_class_valuation.md)
- [Share Class Summary](share_class_summary.md)
- [Share Class Dividend Details](share_class_dividend_details.md)
- [Share Class Rights And Preferences](share_class_rights_and_preferences.md)
- [Preferred Share Class Details](preferred_share_class_details.md)

## Stakeholder Types

- [Stakeholder Type](stakeholder_type.md)
- [Stakeholder Entity Type](stakeholder_entity_type.md)
- [Stakeholder Address](stakeholder_address.md)
- [Stakeholder Group](stakeholder_group.md)
- [Stakeholder Note Block Summary](stakeholder_note_block_summary.md)
- [Stakeholder Option Pool Summary](stakeholder_option_pool_summary.md)
- [Stakeholder Share Class Summary](stakeholder_share_class_summary.md)
- [Stakeholder Warrant Block Summary](stakeholder_warrant_block_summary.md)
- [Issuerscapitalization Stakeholder](issuerscapitalization_stakeholder.md)
- [Issuersdraftsecurities Stakeholder](issuersdraftsecurities_stakeholder.md)
- [Issuersdraftsecurities Stakeholder Relationship](issuersdraftsecurities_stakeholder_relationship.md)
- [Publicapiissuers Stakeholder Relationship](publicapiissuers_stakeholder_relationship.md)

## Option Grant Types

- [Draft Option Grant](draft_option_grant.md)
- [Option Grant Documents](option_grant_documents.md)
- [Option Grant Vesting Event](option_grant_vesting_event.md)
- [Issuersdraftsecurities Stock Option Type](issuersdraftsecurities_stock_option_type.md)
- [Issuerssecurities Stock Option Type](issuerssecurities_stock_option_type.md)
- [Securitiesoptionexercises Stock Option Type](securitiesoptionexercises_stock_option_type.md)
- [Grant Reason](grant_reason.md)

## Option Exercise Types

- [Exercise](exercise.md)
- [Exercise Type](exercise_type.md)
- [Exercise Status](exercise_status.md)
- [Option Exercise Type](option_exercise_type.md)
- [Option Exercise State](option_exercise_state.md)
- [Option Exercise Money Movement](option_exercise_money_movement.md)
- [Option Exercise Tax Withholding Line Item](option_exercise_tax_withholding_line_item.md)
- [Option Pool Summary](option_pool_summary.md)

## Vesting Types

- [Vesting](vesting.md)
- [Vesting Schedule Type](vesting_schedule_type.md)
- [Issuersinterests Vesting Schedule](issuersinterests_vesting_schedule.md)
- [Issuerssecurities Vesting Schedule](issuerssecurities_vesting_schedule.md)
- [Restricted Stock Award Vesting Event](restricted_stock_award_vesting_event.md)
- [Restricted Stock Unit Vesting Event](restricted_stock_unit_vesting_event.md)

## Exercise Period Types

- [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md)
- [Issuersdraftsecurities Exercise Periods](issuersdraftsecurities_exercise_periods.md)
- [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md)
- [Issuerssecurities Exercise Periods](issuerssecurities_exercise_periods.md)

## Convertible Note Types

- [Note Block](note_block.md)
- [Note Block Status](note_block_status.md)
- [Note Block Summary](note_block_summary.md)
- [Note Type](note_type.md)
- [Interest Accrual Period](interest_accrual_period.md)
- [Interest Compounding Period](interest_compounding_period.md)
- [Day Count Basis](day_count_basis.md)
- [Dividend Accrual Period](dividend_accrual_period.md)
- [Dividend Accrual Type](dividend_accrual_type.md)
- [Dividend Details](dividend_details.md)
- [Dividend Interest Type](dividend_interest_type.md)
- [Dividend Type](dividend_type.md)

## Restricted Stock Unit Types

- [Restricted Stock Unit Settlement](restricted_stock_unit_settlement.md)

## Benchmark Types

- [Benchmark Value](benchmark_value.md)
- [Benchmarks Metadata](benchmarks_metadata.md)

## Compliance & Regulatory Types

- [Access](access.md)
- [Compliance](compliance.md)
- [Board Approval](board_approval.md)
- [Federal Exemption](federal_exemption.md)
- [Threshold Details](threshold_details.md)
- [Threshold Details Threshold Type](threshold_details_threshold_type.md)

## Point of Contact Types

- [Point Of Contact Type](point_of_contact_type.md)

## Draft Security Types

- [Draft Security State](draft_security_state.md)

## Other Types

- [Acceleration](acceleration.md)
- [Warrant Block Summary](warrant_block_summary.md)

---

[← Back to Home](../index.md) | [View API Objects →](../objects/index.md)
