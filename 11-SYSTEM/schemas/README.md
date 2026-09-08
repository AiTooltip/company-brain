# Schemas

These JSON Schemas define the required metadata for core records. Markdown records keep metadata in YAML front matter; tools may parse that front matter into an object and validate it against the matching schema.

Core record schemas cover projects, approved decisions, products, team members, research, and goals. Configuration and update manifests have their own framework schemas.

Schemas catch missing or malformed fields. They cannot prove that a claim is true or that a human actually approved it. Approval still requires evidence and human responsibility.
