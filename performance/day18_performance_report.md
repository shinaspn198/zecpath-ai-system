\# Day 18 – Performance Benchmark \& Profiling Report



\## Objective



Measure the performance of the Zecpath AI resume parsing pipeline and identify the stages that require optimization.



\## Test Resume



\*\*File:\*\* `CAND-82624710.pdf`



\*\*Pages:\*\* 2



\*\*Extracted Characters:\*\* 5305



\## Performance Benchmark



The resume parsing pipeline was executed multiple times to obtain a more reliable performance baseline.



\### Resume Text Extraction



| Metric         |         Result |

| -------------- | -------------: |

| Number of runs |              5 |

| Average time   | 0.4756 seconds |

| Minimum time   | 0.3323 seconds |

| Maximum time   | 0.6313 seconds |



\### Complete Resume Parsing



| Metric         |         Result |

| -------------- | -------------: |

| Number of runs |              5 |

| Average time   | 0.3501 seconds |

| Minimum time   | 0.3165 seconds |

| Maximum time   | 0.3976 seconds |



\## Parser Stage Profiling



Individual pipeline stages were also profiled.



| Pipeline Stage       |             Average Observed Time |

| -------------------- | --------------------------------: |

| PDF Text Extraction  | \~2.2 seconds during profiling run |

| Text Cleaning        |                    \~0.001 seconds |

| Section Detection    |                    \~0.001 seconds |

| Candidate Extraction |                    \~0.001 seconds |



The profiling results show that PDF processing is the dominant computational stage, while text cleaning, section detection, and candidate extraction require very little processing time.



\## Memory Usage



The initial memory benchmark recorded approximately:



\*\*Peak memory:\*\* \~11.6 MB



The memory usage is acceptable for the current resume parsing workload.



\## Parser Output



The parser successfully extracted the following structured information:



| Field          |     Result |

| -------------- | ---------: |

| Candidate Name | SHIN AS PN |

| Skills         |          8 |

| Experience     |         25 |

| Education      |          2 |

| Projects       |         27 |

| Certifications |          4 |



\## Candidate Name Verification



The parser returned:



`SHIN AS PN`



This value was manually verified against the original PDF.



The PDF itself contains the candidate name as:



`SHIN AS PN`



Therefore, the parser output is correct and no correction was applied.



\## Findings



\### 1. PDF extraction is the main processing stage



PDF text extraction requires significantly more processing time than the remaining parsing stages.



\### 2. Text cleaning is lightweight



The text-cleaning stage completes in approximately 0.001 seconds.



\### 3. Section detection is efficient



Section detection completes in approximately 0.001 seconds and successfully identifies the major resume sections.



\### 4. Candidate extraction is efficient



Candidate extraction also requires approximately 0.001 seconds.



\### 5. Repeated benchmarking provides a better baseline



A five-run benchmark produced an average PDF extraction time of approximately 0.48 seconds and an average complete parsing time of approximately 0.35 seconds.



The repeated benchmark provides a more representative baseline than relying on a single execution.



\## Optimization Decision



No major optimization was applied during Day 18.



The current PDF extraction implementation is simple and functional. Optimization should only be introduced after testing alternative extraction approaches and confirming that extraction accuracy is not reduced.



Future optimization can focus on PDF extraction if larger documents or high-volume resume processing create a performance bottleneck.



\## Conclusion



Day 18 established a performance baseline for the Zecpath AI resume parsing pipeline.



The repeated benchmark demonstrated that the current parser can process the test resume in well under one second on average during repeated execution.



The parser correctly identifies the candidate information and major resume sections.



The main area for future performance optimization is PDF text extraction, while the remaining parsing stages are already lightweight and efficient.



