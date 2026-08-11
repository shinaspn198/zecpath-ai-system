import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import time
import tracemalloc

from parsers.resume_parser import extract_text, parse_resume


FILE_PATH = "data/uploads/CAND-82624710.pdf"


def benchmark(function, name):
    print(f"\n--- {name} ---")

    tracemalloc.start()

    start = time.perf_counter()

    result = function(FILE_PATH)

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print(f"Time taken : {end - start:.4f} seconds")
    print(f"Memory used: {current / 1024:.2f} KB")
    print(f"Peak memory: {peak / 1024:.2f} KB")

    return result


if __name__ == "__main__":

    print("Zecpath AI ATS Performance Benchmark")
    print("=" * 45)

    raw_text = benchmark(
        extract_text,
        "Resume Text Extraction"
    )

    parsed_resume = benchmark(
        parse_resume,
        "Complete Resume Parsing"
    )

    print("\nExtracted characters:", len(raw_text))

    print("Candidate name:",
          parsed_resume.get("name", ""))

    print("Skills:",
          len(parsed_resume.get("skills", [])))

    print("Experience:",
          len(parsed_resume.get("experience", [])))

    print("Education:",
          len(parsed_resume.get("education", [])))

    print("Projects:",
          len(parsed_resume.get("projects", [])))

    print("Certifications:",
          len(parsed_resume.get("certifications", [])))