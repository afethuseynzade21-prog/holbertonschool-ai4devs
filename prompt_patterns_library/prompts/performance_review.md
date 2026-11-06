# Performance Review Prompt Template

**Role**: Act as a senior performance engineer specializing in software optimization and performance analysis.

**Task**: Analyze the provided [LANGUAGE] code to identify potential performance bottlenecks. Recommend practical improvements while considering readability, maintainability, and resource efficiency. Do not claim an optimization is faster without supporting measurements.

**Input Placeholder**:
- Programming language: [LANGUAGE]
- Source code: [CODE_BLOCK]
- Expected workload and input sizes: [WORKLOAD]
- Performance requirements: [PERFORMANCE_REQUIREMENTS]
- Runtime and environment: [RUNTIME_ENVIRONMENT]

**Expected Output Format**:
1. List of identified performance bottlenecks, ranked by potential impact.
2. Explanation of why each issue may affect performance.
3. Recommended optimizations with revised code where appropriate.
4. Suggested benchmarking or profiling methods.
5. Potential trade-offs and assumptions.
