### Document

**Description:** _Contains information about a document, including name, url, and file id._

**Referenced By (1):**
- [Option Grant Documents](option_grant_documents.md)

**Example:**
```json
{
  "fileId": "cfa1313f-3607-4a52-9f9b-908dc94af6ee"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `fileId` | `STRING` | The file identifier of the document.  Files must be uploaded first through the [Upload File](https://docs.carta.com/carta/reference/v1alpha1filesuploadfile) endpoint before their file identifiers can be referenced here. <br/>**Constraints:** Max length: 50 | - |
| `name` | `STRING` | The name of the document.  This is an output-only field and values provided by clients will be ignored when creating. <br/>**Constraints:** Min length: 1, Max length: 256 | - |
| `url` | `STRING` | The URL of the document.  This is an output-only field and values provided by clients will be ignored when creating. <br/>**Constraints:** Max length: 2048 | - |