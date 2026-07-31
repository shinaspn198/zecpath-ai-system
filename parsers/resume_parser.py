import pdfplumber
from docx import Document

from parsers.text_cleaner import TextCleaner
from parsers.section_detector import SectionDetector
from parsers.candidate_extractor import CandidateExtractor


def extract_text(file_path):

    if file_path.lower().endswith(".pdf"):

        text = ""

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

        return text

    elif file_path.lower().endswith(".docx"):

        document = Document(file_path)

        return "\n".join([paragraph.text for paragraph in document.paragraphs])

    else:

        raise ValueError("Unsupported File")


def parse_resume(file_path):

    raw_text = extract_text(file_path)

    cleaned_text = TextCleaner.clean(raw_text)

    detector = SectionDetector()

    sections = detector.detect_sections(cleaned_text)

    candidate = CandidateExtractor.extract(sections)

    return candidate