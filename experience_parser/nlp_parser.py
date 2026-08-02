import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")


def extract_organizations(text):
    """
    Extract company/organization names from text.
    """
    doc = nlp(text)

    organizations = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            organizations.append(ent.text)

    # Remove duplicates while preserving order
    organizations = list(dict.fromkeys(organizations))

    return organizations