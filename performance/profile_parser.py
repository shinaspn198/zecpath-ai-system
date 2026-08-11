import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import time
import tracemalloc

from parsers.resume_parser import extract_text
from parsers.text_cleaner import TextCleaner
from parsers.section_detector import SectionDetector
from parsers.candidate_extractor import CandidateExtractor


FILE_PATH = "data/uploads/CAND-82624710.pdf"


def measure(name, function):

    tracemalloc.start()

    start = time.perf_counter()

    result = function()

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print(f"\n--- {name} ---")
    print(f"Time taken : {end - start:.4f} seconds")
    print(f"Current memory : {current / 1024:.2f} KB")
    print(f"Peak memory : {peak / 1024:.2f} KB")

    return result


if __name__ == "__main__":

    print("Zecpath AI Parser Stage Profiling")
    print("=" * 45)

    raw_text = measure(
        "1. PDF Text Extraction",
        lambda: extract_text(FILE_PATH)
    )

    cleaned_text = measure(
        "2. Text Cleaning",
        lambda: TextCleaner.clean(raw_text)
    )

    detector = SectionDetector()

    sections = measure(
        "3. Section Detection",
        lambda: detector.detect_sections(cleaned_text)
    )

    candidate = measure(
        "4. Candidate Extraction",
        lambda: CandidateExtractor.extract(sections)
    )

    print("\n" + "=" * 45)
    print("DETECTED SECTIONS")
    print("=" * 45)

    for section, content in sections.items():
        print(f"\n{section}: {len(content)} items")

    print("\n" + "=" * 45)
    print("CANDIDATE SUMMARY")
    print("=" * 45)

    print("Name:", candidate.get("name"))
    print("Skills:", len(candidate.get("skills", [])))
    print("Experience:", len(candidate.get("experience", [])))
    print("Education:", len(candidate.get("education", [])))
    print("Projects:", len(candidate.get("projects", [])))
    print("Certifications:", len(candidate.get("certifications", [])))