import time
import statistics

from parsers.resume_parser import extract_text, parse_resume


FILE_PATH = "data/uploads/CAND-82624710.pdf"
RUNS = 5


def benchmark(function, name):

    times = []

    print(f"\n--- {name} ---")

    for i in range(RUNS):

        start = time.perf_counter()

        result = function(FILE_PATH)

        end = time.perf_counter()

        elapsed = end - start

        times.append(elapsed)

        print(f"Run {i + 1}: {elapsed:.4f} seconds")

    print(f"Average: {statistics.mean(times):.4f} seconds")
    print(f"Minimum: {min(times):.4f} seconds")
    print(f"Maximum: {max(times):.4f} seconds")

    return result


if __name__ == "__main__":

    print("Zecpath AI ATS Repeated Performance Benchmark")
    print("=" * 50)

    raw_text = benchmark(
        extract_text,
        "Resume Text Extraction"
    )

    parsed_resume = benchmark(
        parse_resume,
        "Complete Resume Parsing"
    )

    print("\n=============================================")
    print("FINAL OUTPUT")
    print("=============================================")

    print("Extracted characters:", len(raw_text))

    print(
        "Candidate name:",
        parsed_resume.get("name", "")
    )

    print(
        "Skills:",
        len(parsed_resume.get("skills", []))
    )

    print(
        "Experience:",
        len(parsed_resume.get("experience", []))
    )

    print(
        "Education:",
        len(parsed_resume.get("education", []))
    )

    print(
        "Projects:",
        len(parsed_resume.get("projects", []))
    )

    print(
        "Certifications:",
        len(parsed_resume.get("certifications", []))
    )